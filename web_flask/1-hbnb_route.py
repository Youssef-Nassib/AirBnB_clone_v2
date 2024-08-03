#!/usr/bin/python3
"""this is the same previose script but we gonna add some stuff"""

from flask import Flask

app = Flask(__name__)

"""this return hello HBNB"""


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


"""this return HBNB"""


@app.route('/hbnb', strict_slashes=False)
def ShowHBNB():
    return "HBNB"


"""our web application is listening on 0.0.0.0, port 5000"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
