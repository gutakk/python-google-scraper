import os
import time

import jwt

import psycopg2
from bs4 import BeautifulSoup
from celery import Celery
from flask import Flask, jsonify, request
from flask_cors import CORS
from selenium import webdriver

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config['SECRET_KEY']
CORS(app)

client = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
client.conf.update(app.config)

pg_host = os.environ['POSTGRES_HOST']
pg_user = os.environ['POSTGRES_USER']
pg_password = os.environ['POSTGRES_PASSWORD']
pg_db = os.environ['POSTGRES_DB']


def init_cnx():
    return psycopg2.connect(dbname=pg_db, user=pg_user, password=pg_password, host=pg_host)
    

@app.route('/')
def index():
    return 'Index Page'


@app.route('/user', methods=['POST'])
def user():
    if request.method == 'POST':
        request_body = request.json
        cnx = init_cnx()
        cur = cnx.cursor()
        try:
            cur.execute("SELECT * FROM users WHERE email=%s", [request_body['email']])
            result = cur.fetchone()
            if result:
                return "Email already exist", 400
            cur.execute("""
                INSERT INTO users (email, password)
                VALUES (%s, crypt(%s, gen_salt('bf')));
            """, [request_body['email'], request_body['password']])
            cnx.commit()
            return generate_jwt(request_body['email']), 201
        except Exception as e:
            cnx.rollback()
            raise(e)
        finally:
            cur.close()
            cnx.close()


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        request_body = request.json
        cnx = init_cnx()
        cur = cnx.cursor()
        try:
            cur.execute("SELECT * FROM users WHERE email=%s AND password=crypt(%s, password);", [request_body['email'], request_body['password']])
            result = cur.fetchone()
            if not result:
                return "Email or Password incorrect", 400
            return generate_jwt(request_body['email']), 200
        except Exception as e:
            cnx.rollback()
            raise(e)
        finally:
            cur.close()
            cnx.close()


@client.task
def scrape_data_from_google(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(f"https://www.google.com/search?q={keyword}")
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    results = soup.find(id="result-stats")
    print(keyword)
    print(results.text)


@app.route('/upload-keywords', methods=['POST'])
def process_keywords():
    if request.method == 'POST':
        request_body = request.json
        for keyword in request_body["keywords"]:
            scrape_data_from_google.apply_async(args=[keyword])
        return "Upload Completed", 200


def generate_jwt(email):
    return jwt.encode({'email': email}, os.environ['JWT_SECRET'], algorithm='HS256')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
