import json
import unittest
from unittest.mock import ANY

import jwt

from models.data import Data
from models.file import File
from models.user import User
from tests import NimbleBaseTestCase
from utils import app, generate_jwt


class TestFile(NimbleBaseTestCase):
    def setUp(self):
        super().setUp()
        self.user_id = 1
        self.email = "test@e.c"
        self.password = "1234"

        self.file_id = 1
        self.filename = "test-file.csv"
        self.keywords = 1

        self.new_user = User(
            id = self.user_id,
            email = self.email,
            password = self.password
        )
        self.db_session.add(self.new_user)
        self.db_session.commit()

        self.new_file = File(
            user_id = self.user_id,
            id = self.file_id,
            filename = self.filename,
            keywords = self.keywords
        )
        self.db_session.add(self.new_file)
        self.db_session.commit()

    
    def test_process_csv_should_return_401_if_no_autorization_headers(self):
        with app.test_client() as client:
            result = client.get('/csv')
            assert result.status_code == 401


    def test_process_csv_should_return_401_if_wrong_authorization(self):
        token = jwt.encode({'sub': self.user_id}, "wrong_secret", algorithm='HS256')
        with app.test_client() as client:
            result = client.get(
                '/csv',
                headers={"Authorization": token}
            )
            assert result.status_code == 401


    def test_get_csv_should_return_404_when_correct_authorization_but_no_data_for_user_id(self):
        user_id = 2
        token = generate_jwt(user_id)
        with app.test_client() as client:
            result = client.get(
                '/csv',
                headers={"Authorization": token}
            )
            assert result.status_code == 404


    def test_get_csv_should_return_200_when_correct_authorization_and_have_data_for_user_id_and_status_is_false_when_no_data(self):
        token = generate_jwt(self.user_id)
        with app.test_client() as client:
            result = client.get(
                '/csv',
                headers={"Authorization": token}
            )
            assert result.status_code == 200

            expected_result = [
                [self.file_id, self.filename, self.keywords, ANY, False]
            ]
            assert json.loads(result.data) == expected_result


    def test_get_csv_should_return_200_when_correct_authorization_and_have_data_for_user_id_and_status_is_true_when_have_data(self):
        token = generate_jwt(self.user_id)

        data_id = 1
        keyword = "test-keyword"
        total_adword = 1
        total_link = 1
        total_search_result = "about 1,000"
        html_code = "test-html-code"

        new_data = Data(
            file_id = self.file_id,
            id = data_id,
            keyword = keyword,
            total_adword = total_adword,
            total_link = total_link,
            total_search_result = total_search_result,
            html_code = html_code
        )
        self.db_session.add(new_data)
        self.db_session.commit()

        with app.test_client() as client:
            result = client.get(
                '/csv',
                headers={"Authorization": token}
            )
            assert result.status_code == 200

            expected_result = [
                [self.file_id, self.filename, self.keywords, ANY, True]
            ]
            assert json.loads(result.data) == expected_result


    def test_post_csv_should_return_200_when_correct_authorization(self):
        self.cur.execute("""
            DELETE FROM data;
            DELETE FROM file;
        """)
        self.cnx.commit()

        token = generate_jwt(self.user_id)
        body = {
            "filename": self.filename,
            "keywords": [1, 2, 3, 4]
        }
        with app.test_client() as client:
            result = client.post(
                '/csv',
                headers={"Authorization": token},
                json=body
            )
            assert result.status_code == 200
