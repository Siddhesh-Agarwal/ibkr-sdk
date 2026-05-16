from pydantic import BaseModel, Field


class FailedTickleResponse(BaseModel):
    model_config = {"populate_by_name": True}

    error: str | None = Field(default=None, alias="error")
