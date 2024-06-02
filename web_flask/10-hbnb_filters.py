#!/usr/bin/python3
"""this module contains two functions
which will return list of states in the
storage"""


from flask import Flask
from models import storage
from flask import render_template
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def close_request(self):
    """close the session after each request"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def state_list():
    """list state and cities associated with them
    and amenities"""
    l1 = storage.all(State).values()
    l2 = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', l1=l1, l2=l2)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
