#!/bin/bash

source ./src/.env

export FLASK_APP=./src/app.py

flask run --host=$FLASK_HOST --port $FLASK_PORT