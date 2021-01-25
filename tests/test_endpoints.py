import pytest
import requests
import tap_marketman.endpoints as endpoints
import tap_marketman.service as service


def test_create_session():
    client = service.create_session()

    assert isinstance(client, requests.sessions.Session)


@pytest.mark.vcr()
def test_get_token():
    token = service.get_token()

    assert isinstance(token, str)


@pytest.mark.vcr()
def test_get_guid():
    guid_list = endpoints.get_guid()

    assert isinstance(guid_list['Buyers'], list)
    assert isinstance(guid_list['Vendors'], list)
    assert isinstance(guid_list['Chains'], list)


@pytest.mark.vcr()
def test_get_inventory_items():
    guid = "9a8f1b1c7ee94eb3a29be4f9a2939987"
    inventory_items = endpoints.get_inventory_items(guid)

    assert isinstance(inventory_items, list)
    assert isinstance(inventory_items[0], dict)
    assert isinstance(inventory_items[0]['Name'], str)
    assert isinstance(inventory_items[0]['ID'], str)

