import pytest
import requests
import tap_marketman.service as service


def test_environment_variables():
    assert isinstance(service.APIKey, str)
    assert isinstance(service.APIPassword, str)


def test_create_session():
    client = service.create_session()

    assert isinstance(client, requests.sessions.Session)


@pytest.mark.vcr()
def test_get_token():
    token = service.get_token()

    assert isinstance(token, str)
