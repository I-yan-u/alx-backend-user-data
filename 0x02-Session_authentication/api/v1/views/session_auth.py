#!/usr/bin/env python3
"""Session auth flask view
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def login():
    """Login view
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == '':
        return make_response(jsonify({ "error": "email missing" }), 400)
    if not password or password == '':
        return make_response(jsonify({ "error": "password missing"}), 400)
    client = User()
    client_s = client.search({'email': email})
    if client_s is None or client_s == []:
        return make_response(jsonify({"error": "no user found for this email"}
                                     ), 404)
    verified = client_s[0].is_valid_password(password)
    if not verified:
        return make_response(jsonify({"error": "wrong password"}), 401)
    else:
        from api.v1.app import auth
        user = client_s[0]
        user_id = user.get('id')
        session_id = auth.create_session(user_id)
        SESSION_NAME = getenv("SESSION_NAME")
        response = user.to_json()
        response.set_cookie('SESSION_NAME', session_id)
        return response
