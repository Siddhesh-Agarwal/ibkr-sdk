
from pydantic import BaseModel


class IndividualPosition(BaseModel):
    acctId: str | None = None
    allExchanges: str | None = None
    assetClass: str | None = None
    avgCost: float | None = None
    avgPrice: float | None = None
    baseAvgCost: float | None = None
    baseAvgPrice: float | None = None
    baseMktPrice: float | None = None
    baseMktValue: float | None = None
    baseRealizedPnl: float | None = None
    baseUnrealizedPnl: float | None = None
    chineseName: str | None = None
    conid: int | None = None
    contractDesc: str | None = None
    countryCode: str | None = None
    currency: str | None = None
    expiry: str | None = None
    fullName: str | None = None
    group: str | None = None
    hasOptions: bool | None = None
    isUS: bool | None = None
    listingExchange: str | None = None
    mktPrice: float | None = None
    mktValue: float | None = None
    model: str | None = None
    multiplier: float | None = None
    name: str | None = None
    position: float | None = None
    putOrCall: str | None = None
    realizedPnl: float | None = None
    sector: str | None = None
    strike: str | None = None
    ticker: str | None = None
    type: str | None = None
    undConid: int | None = None
    unrealizedPnl: float | None = None
