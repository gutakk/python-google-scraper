import os
import time

from bs4 import BeautifulSoup
from celery import Celery
from database import db_session
from models.data import Data
from selenium import webdriver
from utils import app

client = Celery(app.name, broker=os.environ["CELERY_BROKER_URL"])
client.conf.update(app.config)

@client.task()
def scrape_data_from_google(file_id, keyword):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")
        
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(f"https://www.google.com/search?q={keyword}")

        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        total_adword = count_adword(soup)
        total_link = count_link(soup)
        total_search_result = get_total_search_result(soup)
    finally:
        driver.close()

    new_data = Data(
        file_id = file_id,
        keyword = keyword,
        total_adword = total_adword,
        total_link = total_link,
        total_search_result = total_search_result,
        html_code = soup.prettify()
    )
    db_session.add(new_data)
    db_session.commit()
    time.sleep(int(os.environ["SCRAPING_DELAY"]))


def count_adword(soup):
    results = soup.find_all("div", class_="ad_cclk")
    return len(results)


def count_link(soup):
    results = soup.find_all(href=True)
    return len(results)


def get_total_search_result(soup):
    results = soup.find(id="result-stats")
    if results:
        return results.text
    return
