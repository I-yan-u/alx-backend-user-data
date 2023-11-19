#!/usr/bin/env python3
"""Auth class
"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """ Hash password
    """
    return hashpw(password.encode(), gensalt())


def _generate_uuid() -> str:
    """Generates a random uuid and returns it as a string
    Returns:
        str: string representation of the generated uuid
    """
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Validates password and returns True if it matches

        Args:
            email (str): Provided email
            password (str): Provided password

        Returns:
            bool: True if password matches else False
        """
        try:
            user = self._db.find_user_by(email=email)
            hashdpw = user.hashed_password
            valid = checkpw(password.encode(), hashdpw)
            return valid
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session id for the given email

        Args:
            email (str): users email address

        Returns:
            str: session id
        """
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            return user.session_id
        except NoResultFound:
            return None
