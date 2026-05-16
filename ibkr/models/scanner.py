from typing import Any

from pydantic import BaseModel, Field


class ComboValuesItem(BaseModel):
    model_config = {"populate_by_name": True}

    default: bool | None = Field(default=None, alias="default")
    vendor: dict[str, Any] | None = Field(default=None, alias="vendor")


class FilterListItem(BaseModel):
    model_config = {"populate_by_name": True}

    group: str | None = Field(default=None, alias="group")
    display_name: str | None = Field(default=None, alias="displayName")
    code: str | None = Field(default=None, alias="code")
    type: str | None = Field(default=None, alias="type")
    combo_values: list[ComboValuesItem] = Field(
        default_factory=list, alias="comboValues"
    )


class LocationsItem(BaseModel):
    model_config = {"populate_by_name": True}

    display_name: str | None = Field(default=None, alias="displayName")
    type: str | None = Field(default=None, alias="type")
    locations: list[dict[str, Any]] = Field(default_factory=list, alias="locations")


class LocationsItem2(BaseModel):
    model_config = {"populate_by_name": True}

    display_name: str | None = Field(default=None, alias="displayName")
    type: str | None = Field(default=None, alias="type")
    locations: list[dict[str, Any]] = Field(default_factory=list, alias="locations")


class LocationItem(BaseModel):
    model_config = {"populate_by_name": True}

    display_name: str | None = Field(default=None, alias="displayName")
    type: str | None = Field(default=None, alias="type")
    locations: list[LocationsItem] = Field(default_factory=list, alias="locations")


class InstrumentsItem(BaseModel):
    model_config = {"populate_by_name": True}

    display_name: str | None = Field(default=None, alias="displayName")
    type: str | None = Field(default=None, alias="type")
    filters: list[str] = Field(default_factory=list, alias="filters")


class ScanTypeListItem(BaseModel):
    model_config = {"populate_by_name": True}

    display_name: str | None = Field(default=None, alias="displayName")
    code: str | None = Field(default=None, alias="code")
    instruments: list[str] = Field(default_factory=list, alias="instruments")


class IserverScannerParams(BaseModel):
    model_config = {"populate_by_name": True}

    scan_type_list: list[ScanTypeListItem] = Field(
        default_factory=list, alias="scanTypeList"
    )
    instrument_list: list[InstrumentsItem] = Field(
        default_factory=list, alias="instrumentList"
    )
    filter_list: list[FilterListItem] = Field(default_factory=list, alias="filterList")
    location_tree: list[LocationItem] = Field(
        default_factory=list, alias="locationTree"
    )


class FilterItem(BaseModel):
    model_config = {"populate_by_name": True}

    code: str | None = Field(default=None, alias="code")
    value: Any | None = Field(default=None, alias="value")


class IserverScannerRunRequest(BaseModel):
    model_config = {"populate_by_name": True}

    instrument: str | None = Field(default=None, alias="instrument")
    type: str | None = Field(default=None, alias="type")
    location: str | None = Field(default=None, alias="location")
    filter: list[FilterItem] = Field(default_factory=list, alias="filter")


class ContractItem(BaseModel):
    model_config = {"populate_by_name": True}

    server_id: str | None = Field(default=None, alias="serverId")
    column_name: str | None = Field(default=None, alias="columnName")
    symbol: str | None = Field(default=None, alias="symbol")
    conidex: str | None = Field(default=None, alias="conidex")
    con_id: int | None = Field(default=None, alias="conId")
    available_chart_periods: str | None = Field(
        default=None, alias="availableChartPeriods"
    )
    company_name: str | None = Field(default=None, alias="companyName")
    contract_description_1: str | None = Field(
        default=None, alias="contractDescription1"
    )
    listing_exchange: str | None = Field(default=None, alias="listingExchange")
    sec_type: str | None = Field(default=None, alias="secType")


class IserverScannerRunResponse(BaseModel):
    model_config = {"populate_by_name": True}

    contracts: list[ContractItem] = Field(default_factory=list, alias="contracts")
    scan_data_column_name: str | None = Field(default=None, alias="scanDataColumnName")
