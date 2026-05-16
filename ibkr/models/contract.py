from typing import Any

from pydantic import BaseModel, Field


class ContractInfo(BaseModel):
    cfi_code: str | None = None
    symbol: str | None = None
    cusip: str | None = None
    expiry_full: str | None = None
    con_id: int | None = None
    maturity_date: str | None = None
    industry: str | None = None
    instrument_type: str | None = None
    trading_class: str | None = None
    valid_exchanges: str | None = None
    allow_sell_long: bool | None = None
    is_zero_commission_security: bool | None = None
    local_symbol: str | None = None
    contract_clarification_type: str | None = None
    classifier: str | None = None
    currency: str | None = None
    text: str | None = None
    underlying_con_id: int | None = None
    r_t_h: bool | None = None
    multiplier: str | None = None
    underlying_issuer: str | None = None
    contract_month: str | None = None
    company_name: str | None = None
    smart_available: bool | None = None
    exchange: str | None = None
    category: str | None = None


class IncrementRule(BaseModel):
    lowerEdge: int | None = None
    increment: int | None = None


class TifDefaults(BaseModel):
    TIF: str | None = None
    SIZE: str | None = None
    DEFAULT_ACCT: str | None = None
    PMALGO: bool | None = None


class OrderDefaults(BaseModel):
    LMT: dict[str, Any] | None = None


class ContractRules(BaseModel):
    algoEligible: bool | None = None
    allOrNoneEligible: bool | None = None
    costReport: bool | None = None
    canTradeAcctIds: list[str] = Field(default_factory=list)
    error: str | None = None
    orderTypes: list[str] = Field(default_factory=list)
    ibAlgoTypes: list[str] = Field(default_factory=list)
    fraqTypes: list[str] = Field(default_factory=list)
    forceOrderPreview: bool | None = None
    cqtTypes: list[str] = Field(default_factory=list)
    orderDefaults: OrderDefaults | None = None
    orderTypesOutside: list[str] = Field(default_factory=list)
    defaultSize: int | None = None
    cashSize: int | None = None
    sizeIncrement: int | None = None
    tifTypes: list[str] = Field(default_factory=list)
    tifDefaults: TifDefaults | None = None
    limitPrice: float | None = None
    stopPrice: float | None = None
    orderOrigination: str | None = None
    preview: bool | None = None
    displaySize: int | None = None
    fraqInt: int | None = None
    cashCcy: str | None = None
    cashQtyIncr: int | None = None
    priceMagnifier: int | None = None
    negativeCapable: bool | None = None
    incrementType: int | None = None
    incrementRules: list[IncrementRule] = Field(default_factory=list)
    hasSecondary: bool | None = None
    modTypes: list[str] = Field(default_factory=list)
    increment: float | None = None
    incrementDigits: int | None = None


class SecType(BaseModel):
    secType: str | None = None
    months: str | None = None
    exchange: str | None = None


class Issuer(BaseModel):
    id: str | None = None
    name: str | None = None


class SecdefSearchResponse(BaseModel):
    bondid: int | None = None
    conid: str | None = None
    companyHeader: str | None = None
    companyName: str | None = None
    symbol: str | None = None
    description: str | None = None
    restricted: bool | None = None
    fop: str | None = None
    opt: str | None = None
    war: str | None = None
    sections: list[SecType] = Field(default_factory=list)
    issuers: list[Issuer] = Field(default_factory=list)


class IncrementRulesItem(BaseModel):
    lowerEdge: float | None = None
    increment: float | None = None


class DisplayRuleStepItem(BaseModel):
    decimalDigits: int | None = None
    lowerEdge: float | None = None
    wholeDigits: int | None = None


class DisplayRuleItem(BaseModel):
    magnification: int | None = None
    displayRuleStep: list[DisplayRuleStepItem] = Field(default_factory=list)


class Secdef(BaseModel):
    conid: int | None = None
    currency: str | None = None
    time: int | None = None
    chineseName: str | None = None
    allExchanges: str | None = None
    listingExchange: str | None = None
    countryCode: str | None = None
    name: str | None = None
    assetClass: str | None = None
    expiry: str | None = None
    lastTradingDay: str | None = None
    group: str | None = None
    putOrCall: str | None = None
    sector: str | None = None
    sectorGroup: str | None = None
    strike: str | None = None
    ticker: str | None = None
    undConid: int | None = None
    multiplier: int | None = None
    type: str | None = None
    hasOptions: bool | None = None
    fullName: str | None = None
    isUS: bool | None = None
    incrementRules: list[IncrementRulesItem] = Field(default_factory=list)
    displayRule: list[DisplayRuleItem] = Field(default_factory=list)
    isEventContract: bool | None = None
    pageSize: int | None = None


class TrsrvSecDefResponse(BaseModel):
    secdef: list[Secdef] = Field(default_factory=list)


class EligibleContractParticipantDetails(BaseModel):
    code: str | None = None
    status: bool | None = None


class EligibleContractParticipant(BaseModel):
    eligibleContractParticipantDetails: list[EligibleContractParticipantDetails] = (
        Field(default_factory=list)
    )
    status: bool | None = None
