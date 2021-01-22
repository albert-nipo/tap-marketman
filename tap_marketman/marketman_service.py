import requests
import json
from dotenv import load_dotenv
import os
import pprint
import singer
from singer import Transformer
from datetime import date, datetime, timezone, timedelta
from collections import defaultdict


pp = pprint.PrettyPrinter(indent=4, depth=3)

# This code is for production.
# args = singer.utils.parse_args(["user", "password"])
# USER = args.config['user']
# PASSWORD = args.config['password']

# The code below is for testing with Pytest.
load_dotenv()
APIKey = json.loads(os.getenv("gregorys"))['APIKey']
APIPassword = json.loads(os.getenv("gregorys"))['APIPassword']

client = requests.Session()


def get_token():
    url = "https://api.marketman.com/v3/buyers/auth/GetToken"

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


session_token = get_token()


def get_inventory_items():
    url = "https://api.marketman.com/v3/buyers/inventory/GetInventoryItems"

    payload_dict = {
        'BuyerGuid': 'string'
    }

    payload = json.dumps(payload_dict)
    headers = {
        'Content-Type': 'application/json',
        'AUTH_TOKEN': session_token
    }

    response = client.post(url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def get_inventory_counts():
    url = "https://api.marketman.com/v3/buyers/inventory/GetInventoryCounts"

    payload_dict = {
        'BuyerGuid': 'string',
        'DateTimeFromUTC': 'utc time',
        'DateTimeToUTC': 'utc time'
    }

    payload = json.dumps(payload_dict)
    headers = {
        'Content-Type': 'application/json',
        'AUTH_TOKEN': session_token
    }

    response = client.post(url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def get_menu_items():
    url = "https://api.marketman.com/v3/buyers/inventory/GetMenuItems"

    payload_dict = {
        'BuyerGuid': 'string'
    }

    payload = json.dumps(payload_dict)
    headers = {
        'Content-Type': 'application/json',
        'AUTH_TOKEN': session_token
    }

    response = client.post(url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def get_preps():
    url = "https://api.marketman.com/v3/buyers/inventory/GetPreps"

    payload_dict = {
        'BuyerGuid': 'string'
    }

    payload = json.dumps(payload_dict)
    headers = {
        'Content-Type': 'application/json',
        'AUTH_TOKEN': session_token
    }

    response = client.post(url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def get_transfers():
    url = "https://api.marketman.com/v3/buyers/inventory/GetTransfers"

    payload_dict = {
        'BuyerGuid': 'string',
        'DateTimeFromUTC': 'utc time',
        'DateTimeToUTC': 'utc time'
    }

    payload = json.dumps(payload_dict)
    headers = {
        'Content-Type': 'application/json',
        'AUTH_TOKEN': session_token
    }

    response = client.post(url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def get_waste_events():
    url = "https://api.marketman.com/v3/buyers/inventory/GetWasteEvents"

    payload_dict = {
        'BuyerGuid': 'string',
        'DateTimeFromUTC': 'utc time',
        'DateTimeToUTC': 'utc time'
    }

    payload = json.dumps(payload_dict)
    headers = {
        'Content-Type': 'application/json',
        'AUTH_TOKEN': session_token
    }

    response = client.post(url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def get_vendors():
    url = "https://api.marketman.com/v3/vendors/partneraccounts/GetAuthorisedAccounts"

    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'AUTH_TOKEN': session_token
    }

    response = client.post(url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def get_orders_by_sent_date():
    url = "https://api.marketman.com/v3/buyers/orders/GetOrdersBySentDate"

    payload_dict = {
        'BuyerGuid': 'string',
        'DateTimeFromUTC': 'utc time',
        'DateTimeToUTC': 'utc time'
    }

    payload = json.dumps(payload_dict)
    headers = {
        'AUTH_TOKEN': session_token,
        'Content-Type': 'application/json'
    }

    response = client.post(url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
