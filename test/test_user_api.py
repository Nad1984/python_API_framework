import json
import re
import pytest
import pytest_check as check

from api_clients import user_api_client
from api_clients.user_api_client import UserApiClient
from fixtures.utils import is_json
from test_data.test_data_user import user1, user2, user3, user4


@pytest.mark.user
@pytest.mark.parametrize("user_data", user1)
def test_add_a_new_user(user_data):
    user_client = UserApiClient()
    response_body = user_client.create_user(user_data)
    assert response_body.ok, f"Expected response is OK, but got {response_body.status_code}"
    assert response_body.json(), f"Expected JSON in response body, but got\n{response_body.text}\nShould be: " \
                                      f"{json.dumps(user_data)}"


@pytest.mark.user
@pytest.mark.parametrize("user_data", user2)
def test_add_list_of_users(user_data):
    user_client = UserApiClient()
    response_body = user_client.create_users_list(user_data)
    assert response_body.ok, f"Expected response is OK, but got {response_body.status_code}"
    assert response_body.json(), f"Expected JSON in response body, but got\n{response_body.text}\nShould be: " \
                                      f"{json.dumps(user_data)}"


@pytest.mark.user
@pytest.mark.parametrize("user_name, user_pass", user3)
def test_user_login_to_system(user_name, user_pass):
    user_client = UserApiClient()
    response_body = user_client.user_login(user_name, user_pass)
    assert response_body.ok, f"Expected response is OK, but got {response_body.status_code}"


@pytest.mark.user
def test_user_logout():
    user_client = UserApiClient()
    response_body = user_client.user_logout()
    assert response_body.ok, f"Expected response is OK, but got {response_body.status_code}"


@pytest.mark.user
@pytest.mark.parametrize("user_name", user4)
def test_get_user_by_name(user_name):
    user_client = UserApiClient()
    response_body = user_client.find_user_by_name(user_name)
    assert response_body.ok, f"Expected response is OK, but got {response_body.status_code}"