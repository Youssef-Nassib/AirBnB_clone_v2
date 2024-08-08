#!/bin/usr/python3

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function that print hello HBNB"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """function that display HBNB"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """display C followed by the value of the text variables"""
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
