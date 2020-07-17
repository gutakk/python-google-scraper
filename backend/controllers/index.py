from flask import jsonify
from utils import app


@app.route('/')
def index():
    routes = {}
    for r in app.url_map._rules:
        routes[r.endpoint] = r.rule

    return jsonify(routes)
