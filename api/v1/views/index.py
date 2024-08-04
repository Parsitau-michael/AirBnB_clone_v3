#!/usr/bin/python3
""" This module creates a route /status on app_view."""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """ A method that returns a JSON: "status": "OK" """
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats')
def stats():
    """ A method that an endpoint that retrieves the number of each
    objects by type
    """
    object_counts = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'reviews': storage.count('Review'),
            'states': storage.count('State'),
            'users': storage.count('User')
            }

    return jsonify(object_counts)
