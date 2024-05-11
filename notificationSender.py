from datetime import datetime
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


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
