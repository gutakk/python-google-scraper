from database import init_db
from flask_cors import CORS
from utils import app
import views

CORS(app)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', debug=True)
