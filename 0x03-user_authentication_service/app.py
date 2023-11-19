#!/usr/bin/env python3
"""Basic Flasl app
"""
from flask import Flask, jsonify, request
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


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
