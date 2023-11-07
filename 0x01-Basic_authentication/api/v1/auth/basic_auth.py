#!/usr/bin/env python3
""" Basic_auth implementation
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """To be consructed

    Args:
        Auth (_type_): Authentication class to inherit.
    """
    def extract_base64_authorization_header(self, 
                                            authorization_header: str) -> str:
        """Extract utf-8 format of the authorization header

        Args:
            authorization_header (str): base64 encoded auth header string

        Returns:
            str: utf-8 format of the authorization header
        """
        ah = authorization_header
        if ah is None or isinstance(ah, str) == False:
            return None
        if not ah.startswith('Basic '):
            return None
        return ah[6:]
