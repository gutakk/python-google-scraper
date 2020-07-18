from database import db_session
from flask import request
from models.user import User
from utils import app, generate_jwt
from werkzeug.security import generate_password_hash


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
            password = generate_password_hash(request_body["password"])
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
            User.email == request_body["email"],
            User.password == request_body["password"]
        ).first()
        if not result:
            return "Email or Password incorrect", 400
        return generate_jwt(result[0]), 200
