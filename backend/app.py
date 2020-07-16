import time

import views.data
import views.file
import views.index
import views.user
from database import init_db
from flask_cors import CORS
from utils import app

CORS(app)

if __name__ == '__main__':
    time.sleep(1)
    init_db()
    app.run(host='0.0.0.0', debug=True)
