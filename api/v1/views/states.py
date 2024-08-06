#!/usr/bin/python3
""" This module represents a view for State objects that handles all default
RESTFul API actions
"""

from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
def get_states():
    """ This method returns all states objects """
    states = storage.all(State)
    states_list = [state.to_dict() for state in states.values()]
    return jsonify(states_list)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """ This method returns states objects by id """
    states = storage.all(State)
    state = [state.to_dict() for state in states if state['id'] == state_id]
    if len(state) == 0:
        abort(404)
    return jsonify(state)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ This method deletes a state with id state_id """
    states = storage.all(State)
    state = [state.to_dict() for state in states if state['id'] == state_id]
    if len(state) == 0:
        abort(404)
    states.remove(state[0])
    return {}
