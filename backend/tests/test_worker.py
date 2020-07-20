import json
import os
import unittest

from bs4 import BeautifulSoup
from models.data import Data
from models.file import File
from models.user import User
from tests import NimbleBaseTestCase
from worker import (count_adword, count_link, get_total_search_result,
                    scrape_data_from_google)


class TestWorker(NimbleBaseTestCase):
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

        # self.new_data = Data(
        #     file_id = self.file_id,
        #     id = self.data_id,
        #     keyword = self.keyword,
        #     total_adword = self.total_adword,
        #     total_link = self.total_link,
        #     total_search_result = self.total_search_result,
        #     html_code = self.html_code
        # )
        # self.db_session.add(self.new_data)
        # self.db_session.commit()


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
        result = Data.query.with_entities(
            Data.file_id,
            Data.keyword
        ).filter(
            Data.file_id == self.file_id
        ).all()
        assert result == []

    
    def test_scrape_data_from_google_should_insert_data_correctly_when_has_one_keyword(self):
        scrape_data_from_google(self.file_id, "hello world")
        result = Data.query.with_entities(
            Data.file_id,
            Data.keyword
        ).filter(
            Data.file_id == self.file_id
        ).all()
        assert result == [(self.file_id, "hello world")]
        

    def test_scrape_data_from_google_should_insert_data_correctly_when_has_more_than_one_keyword(self):
        scrape_data_from_google(self.file_id, "hello world")
        scrape_data_from_google(self.file_id, "acer")
        scrape_data_from_google(self.file_id, "dell")
        result = Data.query.with_entities(
            Data.file_id,
            Data.keyword
        ).filter(
            Data.file_id == self.file_id
        ).order_by(
            Data.keyword.asc()
        ).all()
        assert result == [(self.file_id, "acer"), (self.file_id, "dell"), (self.file_id, "hello world")]