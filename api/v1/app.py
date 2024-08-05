#!/usr/bin/python3
""" This module represents the driver for our application
It sets up all the blueprints.
"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """ Closes the storage session after each request."""
    storage.close()


@app.errorhandler(404)
def error_404_handler(e):
    """ This method handles 404 errors"""
    return jsonify(error="Not found")


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', "0.0.0.0"),
            port=int(os.getenv('HBNB_API_PORT', 5000)),
            threaded=True, debug=True
            )
