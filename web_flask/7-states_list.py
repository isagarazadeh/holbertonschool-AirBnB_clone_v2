#!/usr/bin/python3
"""Sript that starts a Flask web application"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """tear down app context"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """lists states from database"""
    states = storage.all('State').values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
