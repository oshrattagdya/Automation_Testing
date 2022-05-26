import requests
import pytest

class TestLogin:
#1
    def test_valid_login(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email":"oshrattagadya@gmail.com","password":"10203040"}
        response = requests.post(URL,data=body)
        assert response.status_code == 200

#2
    def test_invalid_when_email_incorrect(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email":"uy@gmail.com","password" :"10203040"}
        response = requests.post(URL,data=body)
        assert response.status_code == 400

#3
    def test_invalid_when_pass_incorrect(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email":"oshrattagadya@gmail.com","password":"123456789"}
        response = requests.post(URL,data=body)
        assert response.status_code == 400

#4
    def test_invalid_when_email_null(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email":"","password":"123456789"}
        response = requests.post(URL,data=body)
        assert response.status_code == 400

#5
    def test_invalid_when_pass_null(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email": "oshrattagadya@gmail.com","password": ""}
        response = requests.post(URL,data=body)
        assert response.status_code == 400

#6
    def test_invalid_when_both_field_null(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email": "", "password": ""}
        response = requests.post(URL,data=body)
        assert response.status_code == 400

#7
    def test_invalid_when_emailfiled_contains_num(self):
        URL = "https://trip-yoetz.herokuapp.com/auth/login"
        body = {"email": "123455657@10", "password": "10203040"}
        response = requests.post(URL,data=body)
        assert response.status_code == 400

#8
    # def test_invalid_when_







