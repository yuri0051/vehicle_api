"""Flask App Module"""

import os
from logging.config import fileConfig
from flask import Flask

from src import settings as st
from src.database import init_db
from src.database import db_session
from src.views.cars  import cars_blueprint
from src.views.popular import popular_blueprint
from src.views.rate import rate_blueprint

def create_app():
    """Creates Flask App"""
    app_ = Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_DB_PATH
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app_.register_blueprint(cars_blueprint)
    app_.register_blueprint(popular_blueprint)
    app_.register_blueprint(rate_blueprint)
    return app_

def setup_logging():
    """Sets up Logging"""
    log_dirpath = './log'
    if not os.path.exists(log_dirpath):
        os.makedirs(log_dirpath)

    fileConfig(st.FLASK_LOGFILE_PATH)


init_db()

app = create_app()

setup_logging()

@app.teardown_appcontext
def shutdown_session(ex=None):
    """Tears down Sqlalchemy session"""
    db_session.remove()
