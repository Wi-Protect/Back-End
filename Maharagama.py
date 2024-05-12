import datetime
import time
from notificationSender import send_notification
import os

def playAlarm(): 
    # print("Playing Alarm")
    soundPath = "alarms/classic-alarm.wav"
    os.system("aplay " + soundPath + " > /dev/null 2>&1")


def intrusion():
    print("\tTime: " + str(datetime.datetime.now()), end="")

    print("\tPrediction:  ACTIVITY" + str(2))

    print("\t\tIntruder Detected.")
    send_notification("Intruder Detected", "Intruder Detected")
    playAlarm()
    # print("Intruder Detected")
    recent = [0, 0, 0, 0, 0]
    lastQueue = [0, 0, 0, 0, 0]
    time.sleep(25)

def wakeup():
    print("\tTime: " + str(datetime.datetime.now()), end="")

    print("\tPrediction:  ACTIVITY" + str(1))

    print("\t\tWakeup Detected.")
    recent = [0, 0, 0, 0, 0]
    lastQueue = [0, 0, 0, 0, 0]
    send_notification("Wakeup Detected",
                        "System will sleep for 5 minutes")
    time.sleep(60*5)