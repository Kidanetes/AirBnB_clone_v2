#!/usr/bin/python3
"""this module contains two functions
which will return list of states in the
storage"""


from flask import Flask
from models import storage
from flask import render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_request(exception):
    """close the session after each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """list every state in the storage"""
    l1 = storage.all(State).values()
    return render_template('7-states_list.html', l1=l1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
