from flask import Flask
import requests

app = Flask(__name__)

@app.route('/currentTime', methods=['GET'])
def getCurrentTime():
    response = requests.get('http://127.0.0.1:5000/currentTime')  # get-запрос по соответсвующему адресу

    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        return "Fail"


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # запуск локального веб-сервера; debug=True - видим все ошибки на самом сервере
