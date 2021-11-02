from flask import Flask, render_template
from datetime import datetime
from random import randint

app = Flask(__name__)  # создаем экземпляр класса, передаем дерективу __name__
# в случае импорта __name__ содержит имя текужего файла
# в случае самостоятельного запуска __name__ = __main__


@app.route('/', methods=['GET'])  # создаем декоратор; указываем, по какому URL будет отрабатывать функция
def index():
    return render_template('index.html')  # рендерим отдельный HTML-файл, чтоб не грузить основной файл


@app.route('/currentTime', methods=['GET'])
def getCurrentTime():
    return str(datetime.now().time())


@app.route('/randomNumber', methods=['GET'])
def getRandomNumber():
    return str(randint(0, 10))


if __name__ == '__main__':
    app.run(debug=True)  # запуск локального веб-сервера; debug=True - видим все ошибки на самом сервере
