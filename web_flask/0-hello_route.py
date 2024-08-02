#!/usr/bin/python3

"""
this how we start a Flask application
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Return a simple greeting."""
    return "Hello HBNB!"

"""
This is where our application should be listening.
"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
