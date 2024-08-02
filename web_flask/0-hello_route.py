#!/usr/bin/python3

""" this how we start aflask application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)




def index():
    return "Hello HBNB!"


""" this where our application should be listenning"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
