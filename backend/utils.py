import os

import jwt

import psycopg2
from flask import Flask
from models.user import User

app = Flask(__name__)


def generate_jwt(user_id):
    return jwt.encode({'sub': user_id}, os.environ['JWT_SECRET'], algorithm='HS256')


def validate_jwt(token):
    try:
        return jwt.decode(token, os.environ['JWT_SECRET'], algorithms=["HS256"], verify=True)
    except Exception as e:
        return 401


def find_user(user_id):
    result = User.query.filter(
        User.id == user_id
    ).first()
    if result:
        return True
    return False
