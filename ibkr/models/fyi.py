
from pydantic import BaseModel


class FyiSettingsItem(BaseModel):
    A: int | None = None
    FC: str | None = None
    H: int | None = None
    FD: str | None = None
    FN: str | None = None


class FyiEnableDeviceOption(BaseModel):
    deviceName: str | None = None
    deviceId: str | None = None
    uiName: str | None = None
    enabled: bool | None = None


class FyiVT(BaseModel):
    V: int | None = None
    T: int | None = None
