#!/usr/bin/python3
"""doc"""


from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def remove(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list():
    sort = storage.all("State").values()
    states = sorted(sort, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
