#!/usr/bin/python3
"""this module contains implementation
of flask framework"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """this function return hello HBNB!
    routes /"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """this function return HBNB when we
    route /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """this function returns c + <text> when we
    route /c/<text>"""
    return f"c {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
