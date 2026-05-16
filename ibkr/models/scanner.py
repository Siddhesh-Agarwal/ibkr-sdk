from typing import Any

from pydantic import BaseModel, Field


class ComboValuesItem(BaseModel):
    default: bool | None = None
    vendor: dict[str, Any] | None = None


class FilterListItem(BaseModel):
    group: str | None = None
    display_name: str | None = None
    code: str | None = None
    type: str | None = None
    combo_values: list[ComboValuesItem] = Field(default_factory=list)


class LocationsItem(BaseModel):
    display_name: str | None = None
    type: str | None = None
    locations: list[dict[str, Any]] = Field(default_factory=list)


class LocationsItem2(BaseModel):
    display_name: str | None = None
    type: str | None = None
    locations: list[dict[str, Any]] = Field(default_factory=list)


class LocationItem(BaseModel):
    display_name: str | None = None
    type: str | None = None
    locations: list[LocationsItem] = Field(default_factory=list)


class InstrumentsItem(BaseModel):
    display_name: str | None = None
    type: str | None = None
    filters: list[str] = Field(default_factory=list)


class ScanTypeListItem(BaseModel):
    display_name: str | None = None
    code: str | None = None
    instruments: list[str] = Field(default_factory=list)


class IserverScannerParams(BaseModel):
    scan_type_list: list[ScanTypeListItem] = Field(default_factory=list)
    instrument_list: list[InstrumentsItem] = Field(default_factory=list)
    filter_list: list[FilterListItem] = Field(default_factory=list)
    location_tree: list[LocationItem] = Field(default_factory=list)


class FilterItem(BaseModel):
    code: str | None = None
    value: Any | None = None


class IserverScannerRunRequest(BaseModel):
    instrument: str | None = None
    type: str | None = None
    location: str | None = None
    filter: list[FilterItem] = Field(default_factory=list)


class ContractItem(BaseModel):
    server_id: str | None = None
    column_name: str | None = None
    symbol: str | None = None
    conidex: str | None = None
    con_id: int | None = None
    available_chart_periods: str | None = None
    company_name: str | None = None
    contract_description_1: str | None = None
    listing_exchange: str | None = None
    sec_type: str | None = None


class IserverScannerRunResponse(BaseModel):
    contracts: list[ContractItem] = Field(default_factory=list)
    scan_data_column_name: str | None = None
