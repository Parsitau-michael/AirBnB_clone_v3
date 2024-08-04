#!/usr/bin/python3
""" This module creates a route /status on app_view."""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """ A method that returns a JSON: "status": "OK" """
    return jsonify({"status": "OK"})
