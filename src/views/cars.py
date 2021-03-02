from flask import Blueprint
from flask import request
import logging
import requests
import pandas as pd
import sqlalchemy

from src.settings import *
from src.database import db_session
from src.models import Car

logger = logging.getLogger('app')

cars_blueprint = Blueprint('cars', __name__, url_prefix='/cars')

@cars_blueprint.route('', methods=['GET'])
def fetch_all_cars():
	query = Car().query.order_by(Car.make.asc(), Car.model.asc())
	cars = query.all()
	results = []
	for row in cars:
		row_ = row.__dict__
		row_.pop('_sa_instance_state')
		row_.pop('id')
		results.append(row_)

	return {'data': results}

@cars_blueprint.route('', methods=['POST'])
def fetch_car():
	json_data = request.json

	make = json_data.get('make')
	model = json_data.get('model')
	if not make:
		return {'error': 'Make is required'}, 400
	elif not model:
		return {'error': 'Model is required'}, 400

	make, model = make.lower(), model.lower()

	url = GET_MODELS_FOR_MAKE_URL.format(make=make)
	with requests.get(url) as resp:
		status_code = resp.status_code
		if status_code != 200:
			return {'error': f'API error, response status code {status_code}'}, 400

		json_resp = resp.json()
		data = json_resp['Results']

		df = pd.DataFrame(data)
		result_df = df.loc[df['Model_Name'].str.lower() == model]
		if len(result_df) == 0:
			error_message = "Model doesn't exist"
			return {'error': error_message}, 400

		result_data = result_df.iloc[0]
		make = result_data.Make_Name
		model = result_data.Model_Name

		try:
			car = Car(make=make, model=model)
			db_session.add(car)
			db_session.commit()
			logger.info(f'Inserted {make} {model}')
			return {'status': 'OK'}

		except sqlalchemy.exc.IntegrityError:
			error_message = 'Make and Model already exist in the Database'
			logger.error(error_message)
			return {'error': error_message}, 400

		except Exception as e:
			logger.error(e, exc_info=True)
			return {'error': str(e)}, 500
	