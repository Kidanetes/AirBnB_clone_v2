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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) 
