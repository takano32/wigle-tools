#!/usr/bin/env python3
#

import os
from sys import argv

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

WIGLE_API_NAME = os.environ.get("WIGLE_API_NAME") or ""
WIGLE_API_TOKEN = os.environ.get("WIGLE_API_TOKEN") or ""


def upload(file_path) -> requests.Response:
    url = "https://api.wigle.net/api/v2/file/upload"
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(WIGLE_API_NAME, WIGLE_API_TOKEN)

    file_name = os.path.basename(file_path)
    file = open(file_path, "rb")
    file_data = file.read()
    file.close()
    files = {"file": (file_name, file_data)}

    data = {"donate": False}
    response = requests.post(url, headers=headers, auth=auth, files=files, data=data)
    return response


file_paths = argv[1:]
for file_path in file_paths:
    response = upload(file_path)
    print("--")
    print("status code:" + str(response.status_code))
    print(response.content)
