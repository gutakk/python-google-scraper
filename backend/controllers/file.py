from database import db_session, engine
from flask import jsonify, request
from models.file import File
from utils import app, find_user, validate_jwt
from worker import scrape_data_from_google


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
        converted_result = [list(row) for row in result]
        if converted_result:
            return jsonify(converted_result), 200
        return "Not Found", 404
    elif request.method == 'POST':
        if not find_user(token_result['sub']):
            return "Unauthorized", 401
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
