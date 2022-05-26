import pytest
import requests
import random


class TestRegister:

    # 1
    def test_valid_registretion(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name": "osrat", "lastName": "tagadya", "birthDate": "2003-12-28", "email": "hokhr@mail.com",
                "image": "iouy", "password": "123123"}
        response = requests.post(URL, json=body)
        print(response.text)
        assert response.status_code == 200

    # 2
    def test_invalid_registretion_when_user_exist(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name": "osrat", "lastName": "tagadya", "birthDate": "2003-12-28", "email": "hr@mail.com",
                "image": "iouy",
                "password": "123123"}
        response = requests.post(URL, json=body)
        assert response.status_code == 400
        res = response.json()
        assert res["message"] == "user with that email already exists"
        assert res["success"] == False

    # 3
    def test_invalid_when_email_field_null(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name": "osrat", "lastName": "tagadya", "birthDate": "2003-12-28", "email": " ",
                "image": "iouy",
                "password": "123123"}
        response = requests.post(URL, json=body)
        assert response.status_code == 500
        res = response.json()
        assert res["message"] == 'User validation failed: email: Path `email` is invalid ( ).'
        assert res["success"] == False

    # 4
    def test_invalid_when_email_field_incorrect(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/register"
        body = {"name": "oat", "lastName": "tagadya", "birthDate": "2003-12-28", "email": " posdjngnfmmj",
                "image": "iouy",
                "password": "123123"}
        response = requests.post(URL, json=body)
        assert response.status_code == 500
        res = response.json()
        assert res["message"] == 'User validation failed: email: Path `email` is invalid ( posdjngnfmmj).'
        assert res["success"] == False
