import pytest
import pytest_cov
import pytest_vcr
from tap_marketman.marketman_endpoints import *


def test_create_session():
    client = create_session()

    assert isinstance(client, requests.sessions.Session)


@pytest.mark.vcr()
def test_get_token():
    token = get_token()

    assert isinstance(token, str)
