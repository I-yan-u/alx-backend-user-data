#!/usr/bin/env python3
""" Basic_auth implementation
"""
from api.v1.auth.auth import Auth
import base64
import binascii
from typing import TypeVar
from models.user import User


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

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Get user object from credentials

        Args:
            user_email (str): User email
            user_pwd (str): User pwrd
        """
        client = User()
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        client_s = client.search({'email': user_email})
        if client_s is not None and client_s != []:
            if client_s[0].is_valid_password(user_pwd):
                return client_s[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """populates auth with current user data
        """
        user_email, password = self.extract_user_credentials(
                self.decode_base64_authorization_header(
                    self.extract_base64_authorization_header(
                        self.authorization_header(request)
                    )
                )
            )
        return self.user_object_from_credentials(
            user_email, password
        )
