import json
import requests
from tap_marketman.helpers import create_guid_list

class MarketManClient:
    BASE_URL = 'https://api.marketman.com/v3'

    def __init__(self, apikey, apipassword):
        self._client = requests.Session()
        self.auth_token = self.get_auth_token(apikey, apipassword)
        self._client.headers.update({
            'Content-Type': 'application/json',
            'AUTH_TOKEN': self.auth_token
        })
        self.guid = self.get_guid()


    def get_auth_token(self, apikey, apipassword):
        url = f'{self.BASE_URL}/buyers/auth/GetToken'
        payload_dict = {
            'APIKey': apikey,
            'APIPassword': apipassword
        }

        payload = json.dumps(payload_dict)
        headers = {
            'Content-Type': 'application/json'
        }

        return self._client.post(url, headers=headers, data=payload).json()['Token']


    def get_guid(self):
        url = f'{self.BASE_URL}/buyers/partneraccounts/GetAuthorisedAccounts'

        return create_guid_list(self._client.post(url).json())


    def get_inventory_items(self, guid):
        url = f'{self.BASE_URL}/buyers/inventory/GetInventoryItems'

        payload_dict = {
            'BuyerGuid': guid
        }
        payload = json.dumps(payload_dict)

        return self._client.post(url,data=payload).json()


    def get_inventory_counts(self, guid, start_time, end_time):
        url = f'{self.BASE_URL}/buyers/inventory/GetInventoryCounts'

        payload_dict = {
            'GetLineDetails': True,
            'BuyerGuid': guid,
            'DateTimeFromUTC': start_time,
            'DateTimeToUTC': end_time
        }

        payload = json.dumps(payload_dict)

        return self._client.post(url, data=payload).json()


    def get_menu_items(self, guid):
        url = f'{self.BASE_URL}/buyers/inventory/GetMenuItems'

        payload_dict = {
            'BuyerGuid': guid
        }
        payload = json.dumps(payload_dict)

        return self._client.post(url, data=payload).json()


    def get_preps(self, guid):
        url = f'{self.BASE_URL}/buyers/inventory/GetPreps'

        payload_dict = {
            'BuyerGuid': guid
        }
        payload = json.dumps(payload_dict)

        return self._client.post(url, data=payload).json()


    def get_transfers(self, guid, start_time, end_time):
        url = f'{self.BASE_URL}/buyers/inventory/GetTransfers'

        payload_dict = {
            'BuyerGuid': guid,
            'DateTimeFromUTC': start_time,
            'DateTimeToUTC': end_time
        }
        payload = json.dumps(payload_dict)

        return self._client.post(url, data=payload).json()


    def get_waste_events(self, guid, start_time, end_time):
        url = f'{self.BASE_URL}/buyers/inventory/GetWasteEvents'

        payload_dict = {
            'BuyerGuid': guid,
            'DateTimeFromUTC': start_time,
            'DateTimeToUTC': end_time
        }
        payload = json.dumps(payload_dict)

        return self._client.post(url, data=payload).json()


    def get_orders_by_sent_date(self, guid, start_time, end_time):
        url = f'{self.BASE_URL}/buyers/orders/GetOrdersBySentDate'

        payload_dict = {
            'BuyerGuid': guid,
            'DateTimeFromUTC': start_time,
            'DateTimeToUTC': end_time
        }
        payload = json.dumps(payload_dict)

        return self._client.post(url, data=payload).json()


    def get_vendors(self):
        url = f'{self.BASE_URL}/vendors/partneraccounts/GetAuthorisedAccounts'

        return self._client.post(url).json()
