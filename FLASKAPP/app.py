from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "To jest pierwsza strona www -> <b>framework FLASK</b>"

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1')
