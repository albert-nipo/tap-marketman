import pytest
import pytest_cov
import pytest_vcr
from tap_marketman.helpers import *
from tap_marketman.endpoints import get_guid


@pytest.mark.vcr()
def test_create_guid_list():
    guid_data = get_guid()
    guid_list = create_guid_list(guid_data)

    assert isinstance(guid_list, list)
    assert len(guid_list) > 0
    assert isinstance(guid_list[0], str)


@pytest.mark.vcr()
def test_extract_guid_buyers():
    guid_data = get_guid()
    guid_list = extract_guid_buyers(guid_data)

    assert isinstance(guid_list, list)


@pytest.mark.vcr()
def test_extract_guid_vendors():
    guid_data = get_guid()
    guid_list = extract_guid_vendors(guid_data)

    assert isinstance(guid_list, list)


@pytest.mark.vcr()
def test_extract_guid_chains():
    guid_data = get_guid()
    guid_list = extract_guid_chains(guid_data)

    assert isinstance(guid_list, list)

