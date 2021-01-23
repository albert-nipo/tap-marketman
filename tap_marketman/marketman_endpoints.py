import requests
import json
import pprint
import singer
from datetime import date, datetime, timezone, timedelta
from tap_marketman.marketman_service import create_session, get_token


client = create_session()
session_token = get_token()
headers = {
    'Content-Type': 'application/json',
    'AUTH_TOKEN': session_token
}


def get_guid():
    url = "https://api.marketman.com/v3/buyers/partneraccounts/GetAuthorisedAccounts"

    payload = {}

    response = client.post(url, headers=headers, data=payload)
    json_response = response.json()

    return json_response


def get_inventory_items():
    url = "https://api.marketman.com/v3/buyers/inventory/GetInventoryItems"

    payload_dict = {
        'BuyerGuid': 'string'
    }

    payload = json.dumps(payload_dict)

    response = client.post(url, headers=headers, data=payload)


def get_inventory_counts():
    url = "https://api.marketman.com/v3/buyers/inventory/GetInventoryCounts"

    payload_dict = {
        'BuyerGuid': 'string',
        'DateTimeFromUTC': 'utc time',
        'DateTimeToUTC': 'utc time'
    }

    payload = json.dumps(payload_dict)

    response = client.post(url, headers=headers, data=payload)


def get_menu_items():
    url = "https://api.marketman.com/v3/buyers/inventory/GetMenuItems"

    payload_dict = {
        'BuyerGuid': 'string'
    }

    payload = json.dumps(payload_dict)

    response = client.post(url, headers=headers, data=payload)


def get_preps():
    url = "https://api.marketman.com/v3/buyers/inventory/GetPreps"

    payload_dict = {
        'BuyerGuid': 'string'
    }

    payload = json.dumps(payload_dict)

    response = client.post(url, headers=headers, data=payload)


def get_transfers():
    url = "https://api.marketman.com/v3/buyers/inventory/GetTransfers"

    payload_dict = {
        'BuyerGuid': 'string',
        'DateTimeFromUTC': 'utc time',
        'DateTimeToUTC': 'utc time'
    }

    payload = json.dumps(payload_dict)

    response = client.post(url, headers=headers, data=payload)


def get_waste_events():
    url = "https://api.marketman.com/v3/buyers/inventory/GetWasteEvents"

    payload_dict = {
        'BuyerGuid': 'string',
        'DateTimeFromUTC': 'utc time',
        'DateTimeToUTC': 'utc time'
    }

    payload = json.dumps(payload_dict)

    response = client.post(url, headers=headers, data=payload)


def get_vendors():
    url = "https://api.marketman.com/v3/vendors/partneraccounts/GetAuthorisedAccounts"

    payload = {}

    response = client.post(url, headers=headers, data=payload)


def get_orders_by_sent_date():
    url = "https://api.marketman.com/v3/buyers/orders/GetOrdersBySentDate"

    payload_dict = {
        'BuyerGuid': 'string',
        'DateTimeFromUTC': 'utc time',
        'DateTimeToUTC': 'utc time'
    }

    payload = json.dumps(payload_dict)

    response = client.post(url, headers=headers, data=payload)
