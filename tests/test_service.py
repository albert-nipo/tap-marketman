import pytest
import pytest_cov
import pytest_vcr
from tap_marketman.service import *

def test_environment_variables():
    assert isinstance(APIKey, str)
    assert isinstance(APIPassword, str)


def test_create_session():
    client = create_session()

    assert isinstance(client, requests.sessions.Session)


@pytest.mark.vcr()
def test_get_token():
    token = get_token()

    assert isinstance(token, str)
