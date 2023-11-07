#!/usr/bin/env python3
"""Auth Class implementation
"""
from flask import request
from typing import (List, TypeVar)


class Auth:
    """Auth implementation for Flask app
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication

        Args:
            path (str): Path to models
            excluded_paths (List[str]): Path to models to exclude

        Returns:
            bool: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization content in HTTP header

        Args:
            request (_type_, optional): request header. Defaults to None.

        Returns:
            str: None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user information
        """
        return None
