#!/usr/bin/python3

"""the same previouse thing and we gonna add something"""

from flask import Flask
app = Flask(__name__)


"""this return hello HBNB"""


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


"""this return HBNB """


@app.route('/hbnb', strict_slashes=False)
def showHBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display “C ” followed by the value of the text variable
    replace underscore _ symbols with a space"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
