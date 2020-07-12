import time
import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import app, generate_jwt, init_cnx, validate_jwt
from worker import scrape_data_from_google

CORS(app)

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


@app.route('/csv', methods=['GET', 'POST'])
def process_csv():
    if request.method == 'GET':
        cnx = init_cnx()
        cur = cnx.cursor()
        try:
            file_id = str(uuid.uuid4())
            cur.execute("""
                SELECT 
                    file_id, 
                    filename, 
                    keywords, 
                    created,
                    (SELECT COUNT(*) >= f.keywords FROM data WHERE file_id=f.file_id) AS status
                FROM file f ORDER BY created DESC;
            """)
            result = cur.fetchall()
            return jsonify(result), 200
        except Exception as e:
            cnx.rollback()
            raise(e)
        finally:
            cur.close()
            cnx.close()
    elif request.method == 'POST':
        if validate_jwt(request.headers.get('Authorization')) == 401:
            return "Unauthorized", 401
        request_body = request.json
        cnx = init_cnx()
        cur = cnx.cursor()
        try:
            file_id = str(uuid.uuid4())
            cur.execute("INSERT INTO file (file_id, filename, keywords) VALUES (%s, %s, %s)", [file_id, request_body["filename"], len(request_body["keywords"])])
            cnx.commit()
        except Exception as e:
            cnx.rollback()
            raise(e)
        finally:
            cur.close()
            cnx.close()
        for keyword in request_body["keywords"]:
            scrape_data_from_google.apply_async(args=[file_id, keyword])
        return "Upload Completed", 200


@app.route('/data-report/<file_id>', methods=['GET'])
def data_report(file_id):
    if request.method == 'GET':
        cnx = init_cnx()
        cur = cnx.cursor()
        try:
            app.logger.info(file_id)
            cur.execute("SELECT keyword, total_adword, total_link, total_search_result, file_id FROM data WHERE file_id=%s ORDER BY keyword ASC;", [file_id])
            result = cur.fetchall()
            return jsonify(result), 200
        except Exception as e:
            cnx.rollback()
            raise(e)
        finally:
            cur.close()
            cnx.close()


@app.route('/html-code/<file_id>/<keyword>', methods=['GET'])
def html_code(file_id, keyword):
    if request.method == 'GET':
        cnx = init_cnx()
        cur = cnx.cursor()
        try:
            app.logger.info(file_id)
            cur.execute("SELECT html_code FROM data WHERE file_id=%s AND keyword=%s;", [file_id, keyword])
            result = cur.fetchone()
            app.logger.info(jsonify(result[0]))
            return jsonify(result[0]), 200
        except Exception as e:
            cnx.rollback()
            raise(e)
        finally:
            cur.close()
            cnx.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
