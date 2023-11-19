#!/usr/bin/env python3
"""Auth class
"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """ Hash password
    """
    return hashpw(password.encode(), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the given email and password

        Args:
            email (str): User's email address
            password (str): User's password

        Returns:
            User: New user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f'User {email} already exists.')
        except NoResultFound:
            hashdpw = _hash_password(password)
            user = self._db.add_user(email=email, hashed_password=hashdpw)
            return user