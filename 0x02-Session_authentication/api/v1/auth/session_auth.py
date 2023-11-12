#!/usr/bin/env python3
"""Session Authentication Service # Session Auth class
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Session Authentication Service Implementation."

    Args:
        Auth (Auth): Base Authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a new session

        Args:
            user_id (str, optional): current user id. Defaults to None.

        Returns:
            str: session id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Get the user id for a session id. Returns

        Args:
            session_id (str, optional): The session id. Defaults to None.

        Returns:
            str: User id
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id, None)
        return user_id

    def current_user(self, request=None):
        """Current user

        Args:
            request (_type_, optional): Request header. Defaults to None.
        """
        session_id = self.session_cookie(request)

        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes de user session / logout"""

        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass

        return True
