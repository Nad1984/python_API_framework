import pytest


from api_clients.pet_api_client import PetApiClient
from api_clients.user_api_client import UserApiClient


@pytest.fixture
def pet_api_client():
    pet_client = PetApiClient

    yield pet_client

    del pet_client


@pytest.fixture
def user_api_client():
    user_client = UserApiClient

    yield user_client

    del user_client


