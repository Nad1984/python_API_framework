import json
import re
import pytest
import pytest_check as check

from api_clients.pet_api_client import PetApiClient
from fixtures.utils import is_json, get_json_value
from test_data.test_data_pet import test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11


@pytest.mark.petstore
@pytest.mark.parametrize("status", test1)
def test_find_pet_by_status(status):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.find_by_status(status)

    check.is_true(
        pets_response_body.ok), f"Expected status code 200 OK, actual status code is {pets_response_body.status_code}"
    check.is_true(is_json(pets_response_body.text)), f"Response body: \n{pets_response_body.text}"
    code = pets_response_body.status_code
    check.equal(code, 200), f"Expected status code is 200, but got {pets_response_body.status_code}"


@pytest.mark.petstore
@pytest.mark.parametrize("status", test7)
def test_find_pet_by_status_negative(status):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.find_by_status(status)
    code = pets_response_body.status_code
    check.equal(code, 400), f"Expected status code is 400, but got {pets_response_body.status_code}"


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
def test_add_a_new_pet_to_the_store_returns_expected_result(pet_data):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.pet(pet_data)
    code = pets_response_body.status_code
    check.equal(code, 200), f"Expected response is 201.Created, but got {code}"
    assert pets_response_body.json(), f"Expected JSON in response body, but got\n{pets_response_body.text}\nShould be: " \
                                      f"{json.dumps(pet_data)}"


# post two same responses, result shouldn`t be the same.
@pytest.mark.petstore
def test_add_a_new_pet_to_the_store_idempotency_check():
    pass


@pytest.mark.petstore
@pytest.mark.parametrize("pet_data", test9)
def test_add_a_new_pet_to_the_store_expected_error_when_send_empty_pet_id(pet_data):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.pet(pet_data)
    code = pets_response_body.status_code
    check.equal(code, 500), f"When send empty pet Id, then get 500 server error."
    assert "There was an error processing your request. It has been logged" in pets_response_body.text


@pytest.mark.petstore
@pytest.mark.parametrize("pet_data", test10)
def test_add_a_new_pet_to_the_store_expected_bad_request_when_send_string_with_symbols_or_boolean_as_pet_id(pet_data):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.pet(pet_data)
    code = pets_response_body.status_code
    check.equal(code, 400), f"Expected 400 Bad Request, but got {code}."
    assert "unable to convert input to io.swagger.petstore.model.Pet" in pets_response_body.text


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
    check.equal(code,
                expected_status_code), f"Expected status code is {expected_status_code}, but got {pets_response_body.status_code}"


@pytest.mark.petstore
@pytest.mark.parametrize("pet_id, pet_name, categoryId, petCategoryName, petTagsId, petTagsName, photoUrls, petStatus",
                         test5)
def test_find_pet_by_id(pet_id, pet_name, categoryId, petCategoryName, petTagsId, petTagsName, photoUrls, petStatus):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.find_by_id(pet_id)
    code = pets_response_body.status_code
    check.equal(code, 200), f"Expected status code is 200, but got {pets_response_body.status_code}"
    check.is_true(is_json(pets_response_body.text)), f"Response body: \n{pets_response_body.text}"
    response = dict(pets_response_body.json())
    assert pet_name in response.values(), f"Expected {pet_name} in response body, but got {response.values()}"
    # assert photoUrls in response.values(), f"Expected {photoUrls} in response body, but got {response.values()}"
    data = pets_response_body.json()
    pet_category_id = get_json_value(data, 'category/id')
    check.equal(pet_category_id, categoryId), f"Expected pet category ID is {categoryId}, but got {pet_category_id}"
    pet_category_name = get_json_value(data, 'category/name')
    check.equal(pet_category_name,
                petCategoryName), f"Expected pet category name is {petCategoryName}, but got {pet_category_name}"
    pet_tags_id = get_json_value(data, 'tags/[0]/id')
    check.equal(pet_tags_id, petTagsId), f"Expected pet tags ID is {petTagsId}, but got {pet_tags_id}"
    pet_tags_name = get_json_value(data, 'tags/[0]/name')
    check.equal(pet_tags_name, petTagsName), f"Expected pet tags name is {petTagsName}, but got {pet_tags_name}"
    pet_photo_urls = get_json_value(data, 'photoUrls')
    check.equal(pet_photo_urls, photoUrls), f"Expected pet photo urls {photoUrls}, but got {pet_photo_urls}"
    pet_status = get_json_value(data, 'status')
    check.equal(pet_status, petStatus), f"Expected pest status {petStatus}, but got {pet_status}"


@pytest.mark.petstore
@pytest.mark.parametrize("tags", test6)
def test_find_pet_by_tags_returns_expected_result(tags):
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.find_by_tags(tags)
    code = pets_response_body.status_code
    check.equal(code, 200), f"Expected status code is 200, but got {pets_response_body.status_code}"
    check.is_true(is_json(pets_response_body.text)), f"Response body: \n{pets_response_body.text}"


@pytest.mark.petstore
def test_find_pet_by_tags_returns_empty_array_when_no_such_tag():
    pet_api_client = PetApiClient()
    pets_response_body = pet_api_client.find_by_tags("aaaard")
    code = pets_response_body.status_code
    check.equal(code, 200), f"Expected status code is 200, but got {pets_response_body.status_code}"
    check.is_true(is_json(pets_response_body.text)), f"Response body: \n{pets_response_body.text}"
    data = pets_response_body.json()
    check.equal(len(data), 0, "Result should be empty")
