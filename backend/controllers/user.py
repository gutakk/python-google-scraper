import bcrypt

from database import db_session
from flask import request
from models.user import User
from utils import app, generate_jwt


@app.route('/user', methods=['POST'])
def user():
    if request.method == 'POST':
        request_body = request.json
        result = User.query.with_entities(
            User.id
        ).filter(
            User.email == request_body["email"]
        ).first()
        if result:
            return "Email already exist", 400
        new_user = User(
            email = request_body["email"],
            password = bcrypt.hashpw(request_body["password"].encode("utf-8"), bcrypt.gensalt())
        )
        db_session.add(new_user)
        db_session.commit()
        return generate_jwt(new_user.id), 201


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        request_body = request.json
        result = User.query.with_entities(
            User.id
        ).filter(
            User.email == request_body["email"] and User.password == bcrypt.hashpw(request_body["password"].encode("utf-8"), bcrypt.gensalt())
        ).first()
        if not result:
            return "Email or Password incorrect", 400
        return generate_jwt(result[0]), 200
