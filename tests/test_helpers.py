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

