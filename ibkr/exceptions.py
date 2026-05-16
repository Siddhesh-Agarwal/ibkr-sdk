class IBKRError(Exception):
    """Base exception for IBKR SDK."""

    pass


class IBKRAPIError(IBKRError):
    """API returned an error response."""

    def __init__(self, status: int, error: str, message: str | None = None):
        self.status = status
        self.error = error
        self.message = message
        super().__init__(f"[{status}] {error}: {message}")


class IBKRValidationError(IBKRError):
    """JSON parse or Pydantic validation failed."""

    pass


class IBKRConnectionError(IBKRError):
    """Network connectivity issue."""

    pass
