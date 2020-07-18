import json
import unittest

from models.data import Data
from models.file import File
from models.user import User
from utils import app

# set our application to testing mode
# app.testing = True


class TestData(unittest.TestCase):
    def setUp(self):
        super().setUp()
        # self.new_user = User(
        #     id = 9999,
        #     email = "test@e.c",
        #     password = "1234"
        # )
        # self.db_session.add(self.new_user)
        # self.db_session.commit()

        # self.new_file = File(
        #     user_id = 9999,
        #     id = 9999,
        #     filename = "test-file.csv",
        #     keywords = "1"
        # )
        # self.db_session.add(self.new_file)
        # self.db_session.commit()

        # self.new_data = Data(
        #     file_id = 9999,
        #     keyword = "test-keyword",
        #     total_adword = 1,
        #     total_link = 1,
        #     total_search_result = "about 1,000",
        #     html_code = "test-heml-code"
        # )
        # self.db_session.add(self.new_data)
        # self.db_session.commit()


    def test_get_data_report_should_return_404_when_no_file_id_not_exist(self):
        with app.test_client() as client:
            result = client.get('/data-report/test-file-zzz')
            assert result.status_code == 404


    def test_get_data_report_should_return_200_when_file_id_exist(self):
        # adapter = app.url_map.bind('')
        # import pdb; pdb.set_trace()
        # assert True==True
        with app.test_client() as client:
            result = client.get('/csv')
            import pdb; pdb.set_trace()
            assert result.status_code == 200