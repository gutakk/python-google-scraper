import controllers.data
import controllers.file
import controllers.index
import controllers.user
from database import engine, init_db
from flask_cors import CORS
from utils import app

CORS(app)

if __name__ == '__main__':
    init_db(engine)
    app.run(host='0.0.0.0', debug=True)
