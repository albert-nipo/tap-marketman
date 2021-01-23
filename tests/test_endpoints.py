import pytest
import pytest_cov
import pytest_vcr
from tap_marketman.endpoints import *


def test_create_session():
    client = create_session()

    assert isinstance(client, requests.sessions.Session)


@pytest.mark.vcr()
def test_get_token():
    token = get_token()

    assert isinstance(token, str)


@pytest.mark.vcr()
def test_get_guid():
    guid_list = get_guid()

    assert isinstance(guid_list['Buyers'], list)
    assert isinstance(guid_list['Vendors'], list)
    assert isinstance(guid_list['Chains'], list)
