import os

import jwt

import psycopg2
from flask import Flask


app = Flask(__name__)


def generate_jwt(user_id):
    return jwt.encode({'sub': user_id}, os.environ['JWT_SECRET'], algorithm='HS256')


def validate_jwt(token):
    try:
        return jwt.decode(token, os.environ['JWT_SECRET'], algorithms=["HS256"], verify=True)
    except Exception as e:
        return 401
