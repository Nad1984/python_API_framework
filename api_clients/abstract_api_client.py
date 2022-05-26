from abc import ABC

import pytest
import requests
import json


class AbstractApiClient(ABC):
    def __init__(self):
        self.__api_session = requests.Session()
        self.__url = "https://petstore3.swagger.io/api/v3/"
        self.__api_session.headers.update(
            {
                'accept': 'application/json',
                'Content-Type': 'application/json'
            }
        )

    # wrapper
    def __form_url(self, endpoint: str):
        return self.__url + endpoint

    def get(self, endpoint: str, **kwargs):
        return self.__api_session.get(self.__form_url(endpoint), params=kwargs)

    def _get_pet_store(self, endpoint, **kwargs):
        req_args = dict(kwargs)
        url = f"https://petstore3.swagger.io/api/v3/{endpoint}?{'&'.join([f'{i}={j}' for i, j in zip(req_args.keys(), req_args.values())])}"
        res = self.__api_session.get(url)
        return res

    def post(self, endpoint: str, request_body: dict = None):
        request_body = dict() if not request_body else request_body
        return self.__api_session.post(self.__form_url(endpoint), json=request_body)

    def put(self, endpoint: str, request_body: dict = None):
        request_body = dict() if not request_body else request_body
        return self.__api_session.put(self.__form_url(endpoint), json=request_body)

    def session_close(self):
        self.__api_session.close()

    def __del__(self):
        self.__api_session.close()
        return f"session is closed"
