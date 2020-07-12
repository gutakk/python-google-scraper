import os

import jwt

import psycopg2
from flask import Flask

pg_host = os.environ['POSTGRES_HOST']
pg_user = os.environ['POSTGRES_USER']
pg_password = os.environ['POSTGRES_PASSWORD']
pg_db = os.environ['POSTGRES_DB']

app = Flask(__name__)


def init_cnx():
    return psycopg2.connect(dbname=pg_db, user=pg_user, password=pg_password, host=pg_host)


def generate_jwt(email):
    return jwt.encode({'email': email}, os.environ['JWT_SECRET'], algorithm='HS256')


def validate_jwt(token):
    try:
        return jwt.decode(token, os.environ['JWT_SECRET'], algorithms=["HS256"], verify=True)
    except Exception as e:
        return 401
