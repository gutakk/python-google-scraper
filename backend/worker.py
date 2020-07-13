import os

from bs4 import BeautifulSoup
from celery import Celery
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils import app, init_cnx

client = Celery(app.name, broker=os.environ["CELERY_BROKER_URL"])
client.conf.update(app.config)

@client.task()
def scrape_data_from_google(file_id, keyword):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.google.com/")

        search = driver.find_element_by_name("q")
        search.send_keys(keyword)
        search.send_keys(Keys.RETURN)

        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        print(soup)

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
