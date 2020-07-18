import json
import unittest

from models.data import Data
from models.file import File
from models.user import User
from utils import app
from tests import NimbleBaseTestCase


class TestData(NimbleBaseTestCase):
    def setUp(self):
        super().setUp()
        self.user_id = 1
        self.email = "test@e.c"
        self.password = "1234"

        self.file_id = 1
        self.filename = "test-file.csv"
        self.keywords = 1

        self.data_id = 1
        self.keyword = "test-keyword"
        self.total_adword = 1
        self.total_link = 1
        self.total_search_result = "about 1,000"
        self.html_code = "test-html-code"

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

        self.new_data = Data(
            file_id = self.file_id,
            id = self.data_id,
            keyword = self.keyword,
            total_adword = self.total_adword,
            total_link = self.total_link,
            total_search_result = self.total_search_result,
            html_code = self.html_code
        )
        self.db_session.add(self.new_data)
        self.db_session.commit()

    
    def test_get_data_report_should_return_404_when_file_id_not_exist(self):
        with app.test_client() as client:
            result = client.get('/data-report/9999')
            assert result.status_code == 404


    def test_get_data_report_should_return_200_when_file_id_exist(self):
        data_id = 2
        keyword = "test-keyword-2"
        self.new_data = Data(
            file_id = self.file_id,
            id = data_id,
            keyword = keyword,
            total_adword = self.total_adword,
            total_link = self.total_link,
            total_search_result = self.total_search_result,
            html_code = self.html_code
        )
        self.db_session.add(self.new_data)
        self.db_session.commit()
        with app.test_client() as client:
            result = client.get('/data-report/1')
            assert result.status_code == 200

            expected_data = [
                [self.keyword, self.total_adword, self.total_link, self.total_search_result, self.html_code, self.file_id],
                [keyword, self.total_adword, self.total_link, self.total_search_result, self.html_code, self.file_id]
            ]
            assert (json.loads(result.data), expected_data)


    def test_get_html_code_should_return_404_when_file_id_not_exist(self):
        with app.test_client() as client:
            result = client.get(f'/html-code/9999/{self.keyword}')
            assert result.status_code == 404


    def test_get_html_code_should_return_404_when_keyword_not_exist(self):
        with app.test_client() as client:
            result = client.get(f'/html-code/{self.file_id}/hello-world')
            assert result.status_code == 404


    def test_get_html_code_should_return_404_when_both_file_id_and_keyword_not_exist(self):
        with app.test_client() as client:
            result = client.get(f'/html-code/9999/hello-world')
            assert result.status_code == 404


    def test_get_html_code_should_return_200_when_both_file_id_and_keyword_exist(self):
        with app.test_client() as client:
            result = client.get(f'/html-code/{self.file_id}/{self.keyword}')
            assert result.status_code == 200
            assert json.loads(result.data) == self.html_code