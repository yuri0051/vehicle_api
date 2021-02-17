from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/cars', methods=['GET'])
def fetch_all_cars():
	pass

@app.route('/cars', methods=['POST'])
def fetch_car():
	pass

@app.route('/popular', methods=['GET'])
def fetch_popular_cars():
	pass