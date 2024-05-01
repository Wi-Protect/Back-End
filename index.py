from datetime import datetime
from flask import Flask
import requests

from livePrediction import startPredictions

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


def send_notification(message):
    data = {}
    data['body'] = message
    data['appId'] = 21063
    data['appToken'] = "Ddk9268wY7cmcRKQEcY5zI"
    data['dateSent'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data['title'] = "Intruder Detected"

    url = "https://app.nativenotify.com/api/notification"

    # Send notification to user
    try:
        requests.post(url, json=data)

    except Exception as e:
        print(e)

    return "Done"


@app.route('/start_prediction')
def predict():
    startPredictions()


@app.route('/stop_prediction')
def stop_prediction():
    return "Done"


if __name__ == '__main__':
    app.run()
