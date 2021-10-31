from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    print('URL для главной страницы = ' + str(url_for('index')))
    return render_template('index.html')

@app.route("/profile/<username>")
def profile(username):
    return f'Пользователь: {username}'

if __name__ == '__main__':
    app.run(debug=True)
