import json
import unittest

from utils import app
from tests import NimbleBaseTestCase


class TestIndex(NimbleBaseTestCase):
    def test_get_index_should_return_correctly(self):
        with app.test_client() as client:
            result = client.get('/')
            assert result.status_code == 200
            
            expected_result = {
                "data_report": "/data-report/<file_id>",
                "html_code": "/html-code/<file_id>/<keyword>", 
                "index": "/", 
                "login": "/login", 
                "process_csv": "/csv", 
                "static": "/static/<path:filename>", 
                "user": "/user"
            }
            assert json.loads(result.data) == expected_result
