#!/usr/bin/env python3
""" Basic_auth implementation
"""
from api.v1.auth.auth import Auth
import base64
import binascii


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
        if ah is None or isinstance(ah, str) is False:
            return None
        if not ah.startswith('Basic '):
            return None
        return ah[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Decode base64 authorization header

        Args:
            base64_authorization_header (str): base64 authorization header

        Returns:
            str: utf-8 encoded base64 authorization header
        """
        bah = base64_authorization_header
        if bah is None or not isinstance(bah, str):
            return None
        try:
            res = base64.b64decode(bah, validate=True)
            return res.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """EXtract user credentials from authentication header

        Args:
            str (str): decoded_base64_authorization_header
        """
        bbah = decoded_base64_authorization_header
        if not bbah or not isinstance(bbah, str):
            return None, None
        if ':' in bbah:
            email, password = bbah.split(':')
            return email, password
        else:
            return None, None
