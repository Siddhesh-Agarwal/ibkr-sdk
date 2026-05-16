
from pydantic import BaseModel


class FailedTickleResponse(BaseModel):
    error: str | None = None
