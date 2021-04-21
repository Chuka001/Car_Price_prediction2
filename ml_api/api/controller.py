from flask import Blueprint, request, jsonify
import pandas as pd
import json

from regression_model.make_prediction import make_prediction
from regression_model.config.config import rem_cols

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/cars', methods=['GET'])
def cars():
    if request.method == 'GET':
        return 'ok'


@prediction_app.route('/v1/predict/car_prices', methods=['POST'])
def predict():
    if request.method == 'POST':
        json_data = request.get_json()
        input_data = pd.json_normalize(json_data)
        input_data = pd.read_json(input_data)

        for i in rem_cols:
            input_data[i] = 0

        input_data = input_data.to_json()
        #Make prediction
        result = make_prediction(input_data=input_data)

        predictions = result.get('predictions').tolist()

        return jsonify({'predictions': predictions})