import requests
import json
from dotenv import load_dotenv
import os


# This code is for production.
# args = singer.utils.parse_args(["user", "password"])
# USER = args.config['user']
# PASSWORD = args.config['password']

# The code below is for testing with Pytest.
load_dotenv()
APIKey = os.getenv('APIKey')
APIPassword = os.getenv('APIPassword')


def create_session():
    return requests.Session()


def get_token():
    url = "https://api.marketman.com/v3/buyers/auth/GetToken"
    client = create_session()

    payload_dict = {
        'APIKey': APIKey,
        'APIPassword': APIPassword
    }

    payload = json.dumps(payload_dict)
    headers = {
        'Content-Type': 'application/json'
    }

    response = client.post(url, headers=headers, data=payload)
    new_token = response.json()['Token']

    return new_token

