#!/usr/bin/python3
"""
flask minmimal application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """returns the route /"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return the route /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """return c + text"""
    text = text.replace('_', ' ')
    return "C " + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
