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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the password is valid

    Args:
        hashed_password (bytes): Hashed password
        password (str): password to check

    Returns:
        bool: True or False
    """
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    return False
