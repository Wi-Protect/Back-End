from flask import Flask

from livePrediction import changeModeToNight, startPredictions, stopPredictions

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


@app.route('/night-mode', ['POST'])
def night_mode():
    changeModeToNight()
    return "Night mode activated"


@app.route('/day-mode', ['POST'])
def day_mode():
    changeModeToNight()
    return "Day mode activated"


if __name__ == '__main__':
    app.run(host='192.168.1.14', port=5000)
