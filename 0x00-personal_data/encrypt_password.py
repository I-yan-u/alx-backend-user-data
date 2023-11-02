#!/usr/bin/env python3
"""
Password Encryption and Validation Module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash password

    Args:
        password (str): The password in string form

    Returns:
        bytes: The hashed password
    """
    password = password.encode()
    hash = bcrypt.hashpw(password, bcrypt.gensalt())
    return hash
