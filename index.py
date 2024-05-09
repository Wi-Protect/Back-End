from datetime import datetime
from flask import Flask
import requests

from livePrediction import startPredictions, stopPredictions

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/start_prediction')
def predict():
    startPredictions()
    return "Prediction started"


@app.route('/stop_prediction')
def stop_prediction():
    stopPredictions()
    return "Prediction stopped"


if __name__ == '__main__':
    app.run()
