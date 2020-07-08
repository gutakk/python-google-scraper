import os
import time

import jwt

import psycopg2
from celery import Celery
from flask import Flask, jsonify, request
from flask_cors import CORS

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
def print_test_celery(data):
    print(data)


@app.route('/test-celery', methods=['POST'])
def test_celery():
    if request.method == 'POST':
        print_test_celery.apply_async(args=["hello celery"])
        return "hello celery", 200


def generate_jwt(email):
    return jwt.encode({'email': email}, os.environ['JWT_SECRET'], algorithm='HS256')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
