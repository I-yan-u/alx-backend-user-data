#!/usr/bin/env python3
"""Auth class
"""
from bcrypt import hashpw, gensalt, checkpw


def _hash_password(password: str) -> bytes:
    """ Hash password
    """
    return hashpw(password.encode(), gensalt())
