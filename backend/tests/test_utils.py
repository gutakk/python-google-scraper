import unittest

from utils import generate_jwt, validate_jwt


class TestUtils(unittest.TestCase):
    def test_generate_jwt_should_generate_correctly(self):
        result = generate_jwt("test@email.com")
        assert result == b"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0QGVtYWlsLmNvbSJ9.LoWRlX0n5tcoif-uvhodG52GXF4ZTSYPZezT3dj7BTU"


    def test_validate_jwt_should_validate_correctly_when_jwt_is_correct(self):
        result = validate_jwt("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAZW1haWwuY29tIn0.cIR8ekgjACLB6K96qlLWx1CBtrnQw8f0MmHcErJnEV4")
        assert result == {"email": "test@email.com"}


    def test_validate_jwt_should_validate_failed_when_jwt_is_not_correct(self):
        result = validate_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
        assert result == 401
