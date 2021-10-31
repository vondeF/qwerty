from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def getCurrentTime():
    return str(datetime.now().time())

if __name__ == '__main__':
    app.run(debug=True)
