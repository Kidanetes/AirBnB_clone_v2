#!/usr/bin/python3
"""
flask minmimal application
"""

from flask import Flask
from flask import render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is_cool"):
    """return python + text"""
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_number(n):
    """display n if it is integer"""
    if type(n) is int:
        return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render template"""
    if type(n) is int:
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
