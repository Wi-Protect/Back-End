from flask import Flask

from livePrediction import caliberate, changeModeToNight, startPredictions, stopPredictions

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/start_prediction', methods=['POST'])
def predict():

    startPredictions()
    return "Prediction started"


@app.route('/stop_prediction', methods=['POST'])
def stop_prediction():
    stopPredictions()
    return "Prediction stopped"


@app.route('/night-mode', methods=['POST'])
def night_mode():
    changeModeToNight()
    return "Night mode activated"


@app.route('/day-mode', methods=['POST'])
def day_mode():
    changeModeToNight()
    return "Day mode activated"


@app.route('/caliberate', methods=['POST'])
def caliberate_model():
    caliberate()
    return "Caliberation done"


if __name__ == '__main__':
    app.run(host='192.168.96.46', port=5000)
