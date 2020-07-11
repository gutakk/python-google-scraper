import os
import unittest

import psycopg2
from app import (count_adword, count_link, generate_jwt,
                 get_total_search_result, scrape_data_from_google,
                 validate_jwt)
from bs4 import BeautifulSoup


class TestApp(unittest.TestCase):
    def setUp(self):
        self.pg_host = os.environ['POSTGRES_HOST']
        self.pg_user = os.environ['POSTGRES_USER']
        self.pg_password = os.environ['POSTGRES_PASSWORD']
        self.pg_db = os.environ['POSTGRES_DB']


    def test_generate_jwt_should_generate_correctly(self):
        result = generate_jwt("test@email.com")
        assert result == b"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAZW1haWwuY29tIn0.cIR8ekgjACLB6K96qlLWx1CBtrnQw8f0MmHcErJnEV4"


    def test_validate_jwt_should_validate_correctly_when_jwt_is_correct(self):
        result = validate_jwt("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAZW1haWwuY29tIn0.cIR8ekgjACLB6K96qlLWx1CBtrnQw8f0MmHcErJnEV4")
        assert result == {"email": "test@email.com"}


    def test_validate_jwt_should_validate_failed_when_jwt_is_not_correct(self):
        result = validate_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
        assert result == 401


    def test_count_adword_should_return_count_correctly_when_no_adword(self):
        content = """
        <html>
            <body>
                <div>hello world</div>
            </body>
        </html>
        """
        soup = BeautifulSoup(content, "html.parser")
        result = count_adword(soup)
        assert result == 0


    def test_count_adword_should_return_count_correctly_when_has_one_adword(self):
        content = """
        <html>
            <body>
                <div>hello world</div>
                <div class="ad_cclk">Ad</div>
            </body>
        </html>
        """
        soup = BeautifulSoup(content, "html.parser")
        result = count_adword(soup)
        assert result == 1


    def test_count_adword_should_return_count_correctly_when_has_more_than_one_adwords(self):
        content = """
        <html>
            <body>
                <div>hello world</div>
                <div class="ad_cclk">Ad</div>
                <div class="ad_cclk">Ad</div>
                <div class="ad_cclk">Ad</div>
            </body>
        </html>
        """
        soup = BeautifulSoup(content, "html.parser")
        result = count_adword(soup)
        assert result == 3


    def test_count_link_should_return_count_correctly_when_no_link(self):
        content = """
        <html>
            <body>
                <a>hello world</a>
            </body>
        </html>
        """
        soup = BeautifulSoup(content, "html.parser")
        result = count_link(soup)
        assert result == 0


    def test_count_link_should_return_count_correctly_when_has_one_link(self):
        content = """
        <html>
            <body>
                <div>hello world</div>
                <a href="https://www.google.com">LINK</a>
            </body>
        </html>
        """
        soup = BeautifulSoup(content, "html.parser")
        result = count_link(soup)
        assert result == 1


    def test_count_link_should_return_count_correctly_when_has_more_than_one_links(self):
        content = """
        <html>
            <body>
                <div>hello world</div>
                <a href="https://www.google.com">LINK</a>
                <a href="link">LINK</a>
                <a href="dsdsd">LINK</a>
            </body>
        </html>
        """
        soup = BeautifulSoup(content, "html.parser")
        result = count_link(soup)
        assert result == 3


    def test_get_total_search_result_should_return_result_correctly_when_has_text(self):
        content = """
        <html>
            <body>
                <div id="result-stats">RESULT STATS</div>
            </body>
        </html>
        """
        soup = BeautifulSoup(content, "html.parser")
        result = get_total_search_result(soup)
        assert result == "RESULT STATS"


    def test_get_total_search_result_should_return_result_correctly_when_no_text(self):
        content = """
        <html>
            <body>
                <div id="result-stats"></div>
            </body>
        </html>
        """
        soup = BeautifulSoup(content, "html.parser")
        result = get_total_search_result(soup)
        assert result == ""


    def test_get_total_search_result_should_return_result_correctly_when_no_result_stat(self):
        content = """
        <html>
            <body>
                <div>RESULT STATS</div>
            </body>
        </html>
        """
        soup = BeautifulSoup(content, "html.parser")
        result = get_total_search_result(soup)
        assert result == None


    def test_scrape_data_from_google_should_insert_data_correctly_when_has_no_keyword(self):
        cnx = psycopg2.connect(dbname=self.pg_db, user=self.pg_user, password=self.pg_password, host=self.pg_host)
        cur = cnx.cursor()
        try:
            file_id = "file-id-1"
            filename = "test-file.csv"
            cur.execute("INSERT INTO file (file_id, filename, keywords) VALUES (%s, %s, %s)", [file_id, filename, 1])
            cnx.commit()
            cur.execute("SELECT file_id, keyword FROM data WHERE file_id=%s;", [file_id])
            result = cur.fetchall()
            assert result == []
            cur.execute("DELETE FROM data WHERE file_id=%s;", [file_id])
            cur.execute("DELETE FROM file WHERE file_id=%s;", [file_id])
            cnx.commit()
        except Exception as e:
            cnx.rollback()
            raise(e)
        finally:
            cur.close()
            cnx.close()   

    
    def test_scrape_data_from_google_should_insert_data_correctly_when_has_one_keyword(self):
        cnx = psycopg2.connect(dbname=self.pg_db, user=self.pg_user, password=self.pg_password, host=self.pg_host)
        cur = cnx.cursor()
        try:
            file_id = "file-id-1"
            filename = "test-file.csv"
            cur.execute("INSERT INTO file (file_id, filename, keywords) VALUES (%s, %s, %s)", [file_id, filename, 1])
            cnx.commit()
            scrape_data_from_google(file_id, "hello world")
            cur.execute("SELECT file_id, keyword FROM data WHERE file_id=%s;", [file_id])
            result = cur.fetchall()
            assert result == [(file_id, "hello world")]
            cur.execute("DELETE FROM data WHERE file_id=%s;", [file_id])
            cur.execute("DELETE FROM file WHERE file_id=%s;", [file_id])
            cnx.commit()
        except Exception as e:
            cnx.rollback()
            raise(e)
        finally:
            cur.close()
            cnx.close()
        

    def test_scrape_data_from_google_should_insert_data_correctly_when_has_more_than_one_keyword(self):
        cnx = psycopg2.connect(dbname=self.pg_db, user=self.pg_user, password=self.pg_password, host=self.pg_host)
        cur = cnx.cursor()
        try:
            file_id = "file-id-1"
            filename = "test-file.csv"
            cur.execute("INSERT INTO file (file_id, filename, keywords) VALUES (%s, %s, %s)", [file_id, filename, 1])
            cnx.commit()
            scrape_data_from_google(file_id, "hello world")
            scrape_data_from_google(file_id, "acer")
            scrape_data_from_google(file_id, "dell")
            cur.execute("SELECT file_id, keyword FROM data WHERE file_id=%s ORDER BY keyword ASC;", [file_id])
            result = cur.fetchall()
            assert result == [(file_id, "acer"), (file_id, "dell"), (file_id, "hello world")]
            cur.execute("DELETE FROM data WHERE file_id=%s;", [file_id])
            cur.execute("DELETE FROM file WHERE file_id=%s;", [file_id])
            cnx.commit()
        except Exception as e:
            cnx.rollback()
            raise(e)
        finally:
            cur.close()
            cnx.close()    