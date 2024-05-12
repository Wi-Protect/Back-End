recent = [0, 0, 0, 0, 0]

NIGHT_TIME = 0
DAY_TIME = 1

mode = NIGHT_TIME








if __name__ == '__main__':
    app.run(host='192.168.104.46', port=5000)


def predictionMapping(prediction):

    global mode

    if mode == NIGHT_TIME:

        if prediction == 0 or prediction == 4:
            return 0
        elif prediction == 5:
            return 1
        else:
            return 2

    else:

        if prediction == 0 or prediction == 4:
            return 0
        else:
            return 2


def addRecent(data):
    global recent
    if len(recent) == 5:
        recent.pop(0)
    recent.append(data)


def predict(prediction):
    global recent
    prediction = predictionMapping(prediction)
    if len(recent) > 2:

        if prediction == 1:
            addRecent(prediction)
            return prediction

        else:

            if recent[len(recent)-1] == recent[len(recent)-2] == prediction:
                addRecent(prediction)
                return prediction
            elif recent[len(recent)-2] == recent[len(recent)-3] == prediction:
                addRecent(prediction)
                return prediction
            else:
                if len(recent) > 3:
                    if recent == prediction:
                        addRecent(prediction)
                        return prediction
                    else:
                        addRecent(prediction)
                        return recent[len(recent)-2]
                else:
                    addRecent(prediction)
                    return recent[len(recent)-2]
    else:
        addRecent(prediction)
        return prediction


lastQueue = [0, 0, 0, 0, 0]


def addLastQueue(data):
    global lastQueue
    if len(lastQueue) == 5:
        lastQueue.pop(0)
    lastQueue.append(data)


def lastOutput(inpt):
    global lastQueue
    addLastQueue(inpt)

    most_frequent = max(set(lastQueue), key=lastQueue.count)
    return most_frequent


def getLastOutput(inpt):
    predicted = predict(inpt)
    return lastOutput(predicted)


while True:
    a = input("Activity :")

    print(getLastOutput(int(a)))
