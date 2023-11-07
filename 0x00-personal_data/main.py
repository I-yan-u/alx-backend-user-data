#!/usr/bin/env python3
"""
Main file
"""

hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid

password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(encrypted_password)
encrypted_password2 = hash_password(password)
print(encrypted_password2)
print(is_valid(encrypted_password, password))
