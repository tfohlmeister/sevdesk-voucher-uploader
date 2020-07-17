SevDesk Voucher Uploader
===

Simple Python script for uploading vouchers to sevDesk using their API.


Install Dependencies
---

Only `requests` package is needed:
```
pip3 install requests
```
If you get permission errros on your system, try again with `--user` option:

```
pip3 install requests --user
```

Usage
---

1. To get your API key go to https://my.sevdesk.de and navigate to settings –> user –> specific user
2. Run the program:
    
    ```
    python3 sevdesk-uploader.py --token SEVDESK_TOKEN path_to_filename
    ```

3. (optionally) If you provide your token as an environmental variable you don't need to add it as an argument:

    ```
    export SEVDESK_TOKEN=yourtoken
    python3 sevdesk-uploader.py path_to_filename
    ```