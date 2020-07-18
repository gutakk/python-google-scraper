import json
import unittest
from unittest.mock import ANY

import jwt

from models.user import User
from tests import NimbleBaseTestCase
from utils import app


class TestUser(NimbleBaseTestCase):
    def setUp(self):
        super().setUp()
        self.email = "test@e.c"
        self.password = "1234"

        self.new_user = User(
            email = self.email,
            password = self.password
        )
        self.db_session.add(self.new_user)
        self.db_session.commit()


    def test_post_user_should_return_400_when_email_exist(self):
        body = {
            "email": self.email,
            "password": self.password
        }
        with app.test_client() as client:
            result = client.post(
                '/user',
                json=body
            )
            assert result.status_code == 400

    
    def test_post_user_should_return_201_when_success(self):
        body = {
            "email": "newemail@e.c",
            "password": self.password
        }
        with app.test_client() as client:
            result = client.post(
                '/user',
                json=body
            )
            assert result.status_code == 201


    def test_login_should_return_400_when_email_incorrect(self):
        body = {
            "email": "xxxxx",
            "password": self.password
        }
        with app.test_client() as client:
            result = client.post(
                '/login',
                json=body
            )
            assert result.status_code == 400


    def test_login_should_return_400_when_password_incorrect(self):
        body = {
            "email": self.email,
            "password": "xxxxx"
        }
        with app.test_client() as client:
            result = client.post(
                '/login',
                json=body
            )
            assert result.status_code == 400


    def test_login_should_return_200_when_password_incorrect(self):
        body = {
            "email": self.email,
            "password": self.password
        }
        with app.test_client() as client:
            result = client.post(
                '/login',
                json=body
            )
            assert result.status_code == 200
