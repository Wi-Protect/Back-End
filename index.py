from datetime import datetime
from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    data['appId'] = 21063
    data['appToken'] = "Ddk9268wY7cmcRKQEcY5zI"
    data['dateSent'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data['title'] = "Intruder Detected"

    url = "https://app.nativenotify.com/api/notification"

    requests.post(url, json=data)

    # Send notification to user

    return "Done"


if __name__ == '__main__':
    app.run()
