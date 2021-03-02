"""Vehicle API Settings Module"""

import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

FLASK_HOST = os.getenv('FLASK_HOST')
FLASK_PORT = os.getenv('FLASK_PORT')
FLASK_DEBUG = os.getenv('FLASK_DEBUG')
FLASK_LOGFILE_PATH = os.getenv('FLASK_LOGFILE_PATH')

GET_MODELS_FOR_MAKE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json"

SQLITE_DB_PATH = 'sqlite:///' + os.path.join(basedir, 'test.db')
