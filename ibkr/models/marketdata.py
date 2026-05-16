from typing import Any

from pydantic import BaseModel, Field


class SingleHistoricalBarBidAsk(BaseModel):
    o: float
    c: float
    h: float
    l: float
    v: float
    t: int


class SingleHistoricalBarLast(BaseModel):
    o: float
    c: float
    h: float
    l: float
    v: float
    t: int


class SingleHistoricalBarMidpoint(BaseModel):
    o: float
    c: float
    h: float
    l: float
    v: float
    t: int


class IserverSnapshot(BaseModel):
    conidEx: str | None = None
    conid: int | None = None
    field_6509: str | None = None
    _updated: int | None = None
    field_6119: str | None = None
    server_id: str | None = None
    MD_Field: dict[str, Any] | None = None


class IserverHistoryBidAskResponse(BaseModel):
    serverId: str | None = None
    symbol: str | None = None
    text: str | None = None
    priceFactor: int | None = None
    startTime: str | None = None
    high: str | None = None
    low: str | None = None
    timePeriod: str | None = None
    barLength: int | None = None
    mdAvailability: str | None = None
    outsideRth: bool | None = None
    tradingDayDuration: int | None = None
    volumeFactor: int | None = None
    priceDisplayRule: int | None = None
    priceDisplayValue: str | None = None
    chartPanStartTime: str | None = None
    direction: int | None = None
    negativeCapable: bool | None = None
    messageVersion: int | None = None
    travelTime: int | None = None
    data: list[SingleHistoricalBarBidAsk] = Field(default_factory=list)
    points: int | None = None
    mktDataDelay: int | None = None


class IserverHistoryLastResponse(BaseModel):
    serverId: str | None = None
    symbol: str | None = None
    text: str | None = None
    priceFactor: int | None = None
    startTime: str | None = None
    high: str | None = None
    low: str | None = None
    timePeriod: str | None = None
    barLength: int | None = None
    mdAvailability: str | None = None
    outsideRth: bool | None = None
    tradingDayDuration: int | None = None
    volumeFactor: int | None = None
    priceDisplayRule: int | None = None
    priceDisplayValue: str | None = None
    chartPanStartTime: str | None = None
    direction: int | None = None
    negativeCapable: bool | None = None
    messageVersion: int | None = None
    travelTime: int | None = None
    data: list[SingleHistoricalBarLast] = Field(default_factory=list)
    points: int | None = None
    mktDataDelay: int | None = None


class IserverHistoryMidpointResponse(BaseModel):
    serverId: str | None = None
    symbol: str | None = None
    text: str | None = None
    priceFactor: int | None = None
    startTime: str | None = None
    high: str | None = None
    low: str | None = None
    timePeriod: str | None = None
    barLength: int | None = None
    mdAvailability: str | None = None
    outsideRth: bool | None = None
    tradingDayDuration: int | None = None
    volumeFactor: int | None = None
    priceDisplayRule: int | None = None
    priceDisplayValue: str | None = None
    chartPanStartTime: str | None = None
    direction: int | None = None
    negativeCapable: bool | None = None
    messageVersion: int | None = None
    travelTime: int | None = None
    data: list[SingleHistoricalBarMidpoint] = Field(default_factory=list)
    points: int | None = None
    mktDataDelay: int | None = None


class Service(BaseModel):
    value: int | None = None
    action: str | None = None


class ManageMarketDataSubscriptions(BaseModel):
    service: list[Service] = []
    referenceUserName: str | None = None
