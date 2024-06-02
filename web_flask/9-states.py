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
def close_request(self):
    """close the session after each request"""
    storage.close()


@app.route("/states", strict_slashes=False)
def state_list():
    """list every state in the storage"""
    l1 = storage.all(State).values()
    return render_template('9-states.html', l1=l1, n=1)

@app.route('/states/<id>', strict_slashes=False)
def city_by_id(id):
    """list all cities associated with a state"""
    l1 = storage.all(State).values()
    for i in l1:
        if i.id == id:
            return render_template('9-states.html', state=i, n=2)
    return render_template('9-states.html', n=3)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
