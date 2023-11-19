#!/usr/bin/env python3
"""Basic Flasl app
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
# from typing import Union


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """index route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """register user routes
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": f"{user.email}",
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Implements login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    validate = AUTH.valid_login(email, password)
    if validate:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": f"{email}", "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logs user out and delete session information
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    else:
        AUTH.destroy_session(user.id)
        return redirect('/index')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
