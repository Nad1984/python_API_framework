import json
import re
import pytest
import pytest_check as check


from api_clients.pet_api_client import PetApiClient
from fixtures.utils import is_json
from test_data.test_data_pet import test1, test2, test3, test4, test5, test6, test7, test8


@pytest.mark.petstore
@pytest.mark.parametrize("status", test1)
def test_find_pet_by_status(status):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.find_by_status(status)

    check.is_true(pets_response_body.ok), f"Expected status code 200 OK, actual status code is {pets_response_body.status_code}"
    check.is_true(is_json(pets_response_body.text)), f"Response body: \n{pets_response_body.text}"
    code = pets_response_body.status_code
    check.equal(code, 200), f"Expected status code is 200, but got {pets_response_body.status_code}"


@pytest.mark.petstore
@pytest.mark.parametrize("status", test7)
def test_find_pet_by_status_negative(status):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.find_by_status(status)
    code = pets_response_body.status_code
    check.equal(code, 400), f"Expected status code is 200, but got {pets_response_body.status_code}"


@pytest.mark.petstore
@pytest.mark.parametrize("status, json_keys", test2)
def test_find_by_status_are_there_keys_in_response(status, json_keys):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.find_by_status(status)
    # json_data = json.loads(pets_response_body.text)
    words = pets_response_body.text
    word_list = re.sub("[^\w]", " ", words).split()
    for key in json_keys:
        assert key in word_list


@pytest.mark.petstore
@pytest.mark.parametrize("pet_data", test3)
def test_add_a_new_pet_to_the_store(pet_data):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.pet(pet_data)
    # json_data = json.loads(pets_response_body.text)
    assert pets_response_body.ok, f"Expected response is OK, but got {pets_response_body.status_code}"
    assert pets_response_body.json(), f"Expected JSON in response body, but got\n{pets_response_body.text}\nShould be: " \
                                      f"{json.dumps(pet_data)}"


@pytest.mark.petstore
@pytest.mark.parametrize("pet_data", test4)
def test_update_an_existing_pet(pet_data):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.update_pet(pet_data)
    assert pets_response_body.ok, f"Expected response is OK, but got {pets_response_body.status_code}"
    assert pets_response_body.json(), f"Expected JSON in response body, but got\n{pets_response_body.text}\nShould be: " \
                                      f"{json.dumps(pet_data)}"


@pytest.mark.petstore
@pytest.mark.parametrize("pet_data, expected_status_code", test8)
def test_update_an_existing_pet_negative(pet_data, expected_status_code):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.update_pet(pet_data)
    code = pets_response_body.status_code
    check.equal(code, expected_status_code), f"Expected status code is {expected_status_code}, but got {pets_response_body.status_code}"


@pytest.mark.petstore
@pytest.mark.parametrize("pet_id, pet_name", test5)
def test_find_pet_by_id(pet_id, pet_name):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.find_by_id(pet_id)
    code = pets_response_body.status_code
    check.equal(code, 200), f"Expected status code is 200, but got {pets_response_body.status_code}"
    check.is_true(is_json(pets_response_body.text)), f"Response body: \n{pets_response_body.text}"
    response = dict(pets_response_body.json())
    assert pet_name in response.values(), f"Expected {pet_name} in response body, but got {response.values()}"


@pytest.mark.petstore
@pytest.mark.parametrize("tags", test6)
def test_find_pet_by_tags(tags):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.find_by_tags(tags)
    code = pets_response_body.status_code
    check.equal(code, 200), f"Expected status code is 200, but got {pets_response_body.status_code}"
    check.is_true(is_json(pets_response_body.text)), f"Response body: \n{pets_response_body.text}"






