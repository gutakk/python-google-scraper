import time
import uuid

import bcrypt

from database import db_session, init_db, engine
from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Data, File, User
from utils import app, generate_jwt, validate_jwt
from worker import scrape_data_from_google
from sqlalchemy.sql import func

CORS(app)

@app.route('/')
def index():
    routes = {}
    for r in app.url_map._rules:
        routes[r.endpoint] = r.rule

    return jsonify(routes)


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



@app.route('/csv', methods=['GET', 'POST'])
def process_csv():
    token_result = validate_jwt(request.headers.get('Authorization'))
    if token_result == 401:
        return "Unauthorized", 401

    if request.method == 'GET':
        result = engine.execute("""
                SELECT 
                    id, 
                    filename, 
                    keywords,
                    created,
                    (SELECT COUNT(*) >= f.keywords FROM data WHERE file_id=f.id) AS status
                FROM file f 
                WHERE user_id=%s
                ORDER BY created DESC;
            """, [token_result["sub"]])
        return jsonify([list(row) for row in result]), 200
    elif request.method == 'POST':
        request_body = request.json
        new_file = File(
            user_id = token_result["sub"],
            filename = request_body["filename"],
            keywords = len(request_body["keywords"])
        )
        db_session.add(new_file)
        db_session.commit()
        for keyword in request_body["keywords"]:
            scrape_data_from_google.apply_async(args=[new_file.id, keyword])
        return "Upload Completed", 200


@app.route('/data-report/<file_id>', methods=['GET'])
def data_report(file_id):
    if request.method == 'GET':
        result = Data.query.with_entities(
            Data.keyword,
            Data.total_adword,
            Data.total_link,
            Data.total_search_result,
            Data.file_id
        ).filter(
            Data.file_id == file_id
        ).all()
        return jsonify(result), 200


@app.route('/html-code/<file_id>/<keyword>', methods=['GET'])
def html_code(file_id, keyword):
    if request.method == 'GET':
        result = Data.query.with_entities(
            Data.html_code
        ).filter(
            Data.file_id == file_id and Data.keyword == keyword
        ).first()
        return jsonify(result[0]), 200


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', debug=True)
