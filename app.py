from flask import Flask

app = Flask(__name__)


@app.route('/api/simpleNumber/', methods=['GET'])
def getSimpleNumber():
    return '15'

if __name__ == '__main__':
    app.run(debug=True)
