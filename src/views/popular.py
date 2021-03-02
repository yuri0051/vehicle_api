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

popular_blueprint = Blueprint('popular', __name__, url_prefix='/popular')

@popular_blueprint.route('', methods=['GET'])
def fetch_popular_cars():
	query = Car().query.order_by(Car.rate.desc(), Car.make.asc(), Car.model.asc())
	cars = query.all()[:10]
	results = []
	for row in cars:
		row_ = row.__dict__
		row_.pop('_sa_instance_state')
		row_.pop('id')
		results.append(row_)	

	return {'data': results}
	