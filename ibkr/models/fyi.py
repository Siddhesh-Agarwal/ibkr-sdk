from pydantic import BaseModel, Field


class FyiSettingsItem(BaseModel):
    model_config = {"populate_by_name": True}

    a: int | None = Field(default=None, alias="a")
    fc: str | None = Field(default=None, alias="fc")
    h: int | None = Field(default=None, alias="h")
    fd: str | None = Field(default=None, alias="fd")
    fn: str | None = Field(default=None, alias="fn")


class FyiEnableDeviceOption(BaseModel):
    model_config = {"populate_by_name": True}

    device_name: str | None = Field(default=None, alias="deviceName")
    device_id: str | None = Field(default=None, alias="deviceId")
    ui_name: str | None = Field(default=None, alias="uiName")
    enabled: bool | None = Field(default=None, alias="enabled")


class FyiVT(BaseModel):
    model_config = {"populate_by_name": True}

    v: int | None = Field(default=None, alias="v")
    t: int | None = Field(default=None, alias="t")


class NotificationItem(BaseModel):
    model_config = {"populate_by_name": True}

    r: str | None = Field(default=None, alias="R")
    d: str | None = Field(default=None, alias="D")
    ms: str | None = Field(default=None, alias="MS")
    md: str | None = Field(default=None, alias="MD")
    id: str | None = Field(default=None, alias="ID")
    ht: int | None = Field(default=None, alias="HT")
    fc: str | None = Field(default=None, alias="FC")
