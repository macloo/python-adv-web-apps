"""a demo Flask app with two decorators"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/foobar')
def foobar():
    return '<h1>Hi there, foobar!</h1>'
