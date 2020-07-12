import os

from bs4 import BeautifulSoup
from celery import Celery
from selenium import webdriver
from utils import app, init_cnx

client = Celery(app.name, broker=os.environ["CELERY_BROKER_URL"])
client.conf.update(app.config)

@client.task
def scrape_data_from_google(file_id, keyword):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(f"https://www.google.com/search?q={keyword}")
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        total_adword = count_adword(soup)
        total_link = count_link(soup)
        total_search_result = get_total_search_result(soup)
    finally:
        driver.close()

    cnx = init_cnx()
    cur = cnx.cursor()
    try:
        cur.execute("""
            INSERT INTO data (file_id, keyword, total_adword, total_link, total_search_result, html_code)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, [file_id, keyword, total_adword, total_link, total_search_result, soup.prettify()])
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        raise(e)
    finally:
        cur.close()
        cnx.close()


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
