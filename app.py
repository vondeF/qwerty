from flask import Flask, jsonify
import time

app = Flask(__name__)  # создаем экземпляр класса, передаем дерективу __name__
# в случае импорта __name__ содержит имя текужего файла
# в случае самостоятельного запуска __name__ = __main__

timeArray = [
    {
        'id': 1,
        'time': '12:00:00'
    }
]

@app.route('/currentTime', methods=['GET'])
def getCurrentTime():
    t1 = time.localtime()
    t2 = time.strftime("%H:%M:%S", t1)
    return str(t2)


@app.route('/timeArray', methods=['GET'])
def getTimeArray():
    return jsonify({'timeArray':timeArray})


@app.route('/timeArray', methods=['POST'])
def addTime():
    now = {
        'id': timeArray[-1]['id'] + 1,
        'time': getCurrentTime()
    }
    timeArray.append(now)
    return jsonify({'added time':now})

if __name__ == '__main__':
    app.run(debug=True)  # запуск локального веб-сервера; debug=True - видим все ошибки на самом сервере
