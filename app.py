from flask import Flask
from datetime import datetime
from random import randint

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Тут нет ничего интересного. Отправляйся по другим URL'

@app.route('/test/api/time', methods=['GET'])
def getCurrentTime():
    return str(datetime.now().time())

@app.route('/test/api/randomNumber', methods=['GET'])
def getRandomNumber():
    return str(randint(0, 10))

@app.route('/test/api/certainNumber/<a>', methods=['GET'])
def getCertainNumber(a):
    return str(a)

if __name__ == '__main__':
    app.run(debug=True)
