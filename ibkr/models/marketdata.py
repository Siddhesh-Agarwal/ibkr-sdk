from typing import Any

from pydantic import BaseModel, Field


class SingleHistoricalBarBidAsk(BaseModel):
    model_config = {"populate_by_name": True}

    open: float = Field(alias="open")
    close: float = Field(alias="close")
    high: float = Field(alias="high")
    low: float = Field(alias="low")
    volume: float = Field(alias="volume")
    timestamp: int = Field(alias="timestamp")


class SingleHistoricalBarLast(BaseModel):
    model_config = {"populate_by_name": True}

    open: float = Field(alias="open")
    close: float = Field(alias="close")
    high: float = Field(alias="high")
    low: float = Field(alias="low")
    volume: float = Field(alias="volume")
    timestamp: int = Field(alias="timestamp")


class SingleHistoricalBarMidpoint(BaseModel):
    model_config = {"populate_by_name": True}

    open: float = Field(alias="open")
    close: float = Field(alias="close")
    high: float = Field(alias="high")
    low: float = Field(alias="low")
    volume: float = Field(alias="volume")
    timestamp: int = Field(alias="timestamp")


class IserverSnapshot(BaseModel):
    model_config = {"populate_by_name": True}

    conid_ex: str | None = Field(default=None, alias="conidEx")
    conid: int | None = Field(default=None, alias="conid")
    field_6509: str | None = Field(default=None, alias="field_6509")
    updated: int | None = Field(default=None, alias="updated")
    field_6119: str | None = Field(default=None, alias="field_6119")
    server_id: str | None = Field(default=None, alias="serverId")
    md_field: dict[str, Any] | None = Field(default=None, alias="md_field")


class IserverHistoryBidAskResponse(BaseModel):
    model_config = {"populate_by_name": True}

    server_id: str | None = Field(default=None, alias="serverId")
    symbol: str | None = Field(default=None, alias="symbol")
    text: str | None = Field(default=None, alias="text")
    price_factor: int | None = Field(default=None, alias="priceFactor")
    start_time: str | None = Field(default=None, alias="startTime")
    high: str | None = Field(default=None, alias="high")
    low: str | None = Field(default=None, alias="low")
    time_period: str | None = Field(default=None, alias="timePeriod")
    bar_length: int | None = Field(default=None, alias="barLength")
    md_availability: str | None = Field(default=None, alias="mdAvailability")
    outside_rth: bool | None = Field(default=None, alias="outsideRth")
    trading_day_duration: int | None = Field(default=None, alias="tradingDayDuration")
    volume_factor: int | None = Field(default=None, alias="volumeFactor")
    price_display_rule: int | None = Field(default=None, alias="priceDisplayRule")
    price_display_value: str | None = Field(default=None, alias="priceDisplayValue")
    chart_pan_start_time: str | None = Field(default=None, alias="chartPanStartTime")
    direction: int | None = Field(default=None, alias="direction")
    negative_capable: bool | None = Field(default=None, alias="negativeCapable")
    message_version: int | None = Field(default=None, alias="messageVersion")
    travel_time: int | None = Field(default=None, alias="travelTime")
    data: list[SingleHistoricalBarBidAsk] = Field(default_factory=list, alias="data")
    points: int | None = Field(default=None, alias="points")
    mkt_data_delay: int | None = Field(default=None, alias="mktDataDelay")


class IserverHistoryLastResponse(BaseModel):
    model_config = {"populate_by_name": True}

    server_id: str | None = Field(default=None, alias="serverId")
    symbol: str | None = Field(default=None, alias="symbol")
    text: str | None = Field(default=None, alias="text")
    price_factor: int | None = Field(default=None, alias="priceFactor")
    start_time: str | None = Field(default=None, alias="startTime")
    high: str | None = Field(default=None, alias="high")
    low: str | None = Field(default=None, alias="low")
    time_period: str | None = Field(default=None, alias="timePeriod")
    bar_length: int | None = Field(default=None, alias="barLength")
    md_availability: str | None = Field(default=None, alias="mdAvailability")
    outside_rth: bool | None = Field(default=None, alias="outsideRth")
    trading_day_duration: int | None = Field(default=None, alias="tradingDayDuration")
    volume_factor: int | None = Field(default=None, alias="volumeFactor")
    price_display_rule: int | None = Field(default=None, alias="priceDisplayRule")
    price_display_value: str | None = Field(default=None, alias="priceDisplayValue")
    chart_pan_start_time: str | None = Field(default=None, alias="chartPanStartTime")
    direction: int | None = Field(default=None, alias="direction")
    negative_capable: bool | None = Field(default=None, alias="negativeCapable")
    message_version: int | None = Field(default=None, alias="messageVersion")
    travel_time: int | None = Field(default=None, alias="travelTime")
    data: list[SingleHistoricalBarLast] = Field(default_factory=list, alias="data")
    points: int | None = Field(default=None, alias="points")
    mkt_data_delay: int | None = Field(default=None, alias="mktDataDelay")


class IserverHistoryMidpointResponse(BaseModel):
    model_config = {"populate_by_name": True}

    server_id: str | None = Field(default=None, alias="serverId")
    symbol: str | None = Field(default=None, alias="symbol")
    text: str | None = Field(default=None, alias="text")
    price_factor: int | None = Field(default=None, alias="priceFactor")
    start_time: str | None = Field(default=None, alias="startTime")
    high: str | None = Field(default=None, alias="high")
    low: str | None = Field(default=None, alias="low")
    time_period: str | None = Field(default=None, alias="timePeriod")
    bar_length: int | None = Field(default=None, alias="barLength")
    md_availability: str | None = Field(default=None, alias="mdAvailability")
    outside_rth: bool | None = Field(default=None, alias="outsideRth")
    trading_day_duration: int | None = Field(default=None, alias="tradingDayDuration")
    volume_factor: int | None = Field(default=None, alias="volumeFactor")
    price_display_rule: int | None = Field(default=None, alias="priceDisplayRule")
    price_display_value: str | None = Field(default=None, alias="priceDisplayValue")
    chart_pan_start_time: str | None = Field(default=None, alias="chartPanStartTime")
    direction: int | None = Field(default=None, alias="direction")
    negative_capable: bool | None = Field(default=None, alias="negativeCapable")
    message_version: int | None = Field(default=None, alias="messageVersion")
    travel_time: int | None = Field(default=None, alias="travelTime")
    data: list[SingleHistoricalBarMidpoint] = Field(default_factory=list, alias="data")
    points: int | None = Field(default=None, alias="points")
    mkt_data_delay: int | None = Field(default=None, alias="mktDataDelay")


class Service(BaseModel):
    model_config = {"populate_by_name": True}

    value: int | None = Field(default=None, alias="value")
    action: str | None = Field(default=None, alias="action")


class ManageMarketDataSubscriptions(BaseModel):
    model_config = {"populate_by_name": True}

    service: list[Service] = Field(default_factory=list, alias="service")
    reference_user_name: str | None = Field(default=None, alias="referenceUserName")
