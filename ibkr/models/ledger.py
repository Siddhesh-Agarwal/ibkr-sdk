from typing import Any

from pydantic import BaseModel, Field, model_validator


class LedgerEntry(BaseModel):
    model_config = {"populate_by_name": True}

    acctcode: str | None = Field(default=None, alias="acctcode")
    cashbalance: float | None = Field(default=None, alias="cashbalance")
    cashbalancefxsegment: float | None = Field(
        default=None, alias="cashbalancefxsegment"
    )
    commoditymarketvalue: float | None = Field(
        default=None, alias="commoditymarketvalue"
    )
    corporatebondsmarketvalue: float | None = Field(
        default=None, alias="corporatebondsmarketvalue"
    )
    currency: str | None = Field(default=None, alias="currency")
    dividends: float | None = Field(default=None, alias="dividends")
    exchangerate: int | None = Field(default=None, alias="exchangerate")
    funds: float | None = Field(default=None, alias="funds")
    futuremarketvalue: float | None = Field(default=None, alias="futuremarketvalue")
    futureoptionmarketvalue: float | None = Field(
        default=None, alias="futureoptionmarketvalue"
    )
    futuresonlypnl: float | None = Field(default=None, alias="futuresonlypnl")
    interest: float | None = Field(default=None, alias="interest")
    issueroptionsmarketvalue: float | None = Field(
        default=None, alias="issueroptionsmarketvalue"
    )
    key: str | None = Field(default=None, alias="key")
    moneyfunds: float | None = Field(default=None, alias="moneyfunds")
    netliquidationvalue: float | None = Field(default=None, alias="netliquidationvalue")
    realizedpnl: float | None = Field(default=None, alias="realizedpnl")
    secondkey: str | None = Field(default=None, alias="secondkey")
    sessionid: int | None = Field(default=None, alias="sessionid")
    settledcash: float | None = Field(default=None, alias="settledcash")
    severity: int | None = Field(default=None, alias="severity")
    stockmarketvalue: float | None = Field(default=None, alias="stockmarketvalue")
    stockoptionmarketvalue: float | None = Field(
        default=None, alias="stockoptionmarketvalue"
    )
    tbillsmarketvalue: float | None = Field(default=None, alias="tbillsmarketvalue")
    tbondsmarketvalue: float | None = Field(default=None, alias="tbondsmarketvalue")
    timestamp: int | None = Field(default=None, alias="timestamp")
    unrealizedpnl: float | None = Field(default=None, alias="unrealizedpnl")
    warrantsmarketvalue: float | None = Field(default=None, alias="warrantsmarketvalue")


class LedgerResponse(BaseModel):
    model_config = {"populate_by_name": True}

    entries: dict[str, LedgerEntry] = Field(default_factory=dict)

    @model_validator(mode="before")
    @classmethod
    def parse_ledger_entries(cls, data: Any) -> Any:
        if isinstance(data, dict):
            entries: dict[str, LedgerEntry] = {}
            for key, value in data.items():
                if isinstance(value, dict):
                    entries[key] = LedgerEntry.model_validate(value)
                else:
                    entries[key] = value
            return {"entries": entries}
        return data
