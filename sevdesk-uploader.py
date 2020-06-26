import argparse
import json
import os

import requests


def env_req(key, help):
    return (
        {'default': os.environ.get(key), 'help': help} if os.environ.get(key) else {'required': True, 'help': help}
    )

def upload_file():
    url = "https://my.sevdesk.de/api/v1/Voucher/Factory/createVoucherFromFile"
    files = {'voucher': open(args.filename,'rb')}
    data = {'creditDebit': 'C'}
    response = requests.post(url, files=files, data=data, headers=headers)

    if response.status_code == 201:
        content = response.json()
        if 'objects' in content and 'id' in content['objects']:
            return content['objects']['id']
    
    print("Error uploading voucher!", response.status_code, response.content)
    return None

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="filename to be uploaded")
parser.add_argument("--token", **env_req('SEVDESK_TOKEN', 'sevDesk API token (or set using SEVDESK_TOKEN environment variable)'))

args = parser.parse_args()
headers = {'Authorization': args.token, 'Accept': 'application/json'}

id = upload_file()

if id:
    print('Successfully created voucher id {}!'.format(id))
    exit()

exit(1)
