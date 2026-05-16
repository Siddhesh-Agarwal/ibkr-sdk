import requests

from ibkr.exceptions import IBKRAPIError


class AuthHandler:
    def __init__(self, base_url: str = "https://api.ibkr.com"):
        self.base_url = base_url
        self.session = requests.Session()
        self._authenticated = False

    def login(self, username: str, password: str) -> dict:
        """Authenticate and establish session."""
        response = self.session.post(
            f"{self.base_url}/v1/api/iserver/auth/status",
            json={"username": username, "password": password},
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "connected":
                self._authenticated = True
                return data
            elif data.get("status") == "need_password_change":
                raise IBKRAPIError(401, "Password change required", data.get("message"))
        raise IBKRAPIError(response.status_code, "Authentication failed")

    def tickle(self) -> dict:
        """Ping server to refresh/validate session."""
        response = self.session.get(f"{self.base_url}/v1/api/tickle")
        if response.status_code == 200:
            return response.json()
        raise IBKRAPIError(response.status_code, "Tickle failed")

    def logout(self) -> dict:
        """End session."""
        response = self.session.post(f"{self.base_url}/v1/api/logout")
        if response.status_code == 200:
            self._authenticated = False
            return response.json()
        raise IBKRAPIError(response.status_code, "Logout failed")

    @property
    def authenticated(self) -> bool:
        return self._authenticated
