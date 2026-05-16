from typing import Any

from pydantic import BaseModel, Field


class ContractInfo(BaseModel):
    model_config = {"populate_by_name": True}

    cfi_code: str | None = Field(default=None, alias="cfiCode")
    symbol: str | None = Field(default=None, alias="symbol")
    cusip: str | None = Field(default=None, alias="cusip")
    expiry_full: str | None = Field(default=None, alias="expiryFull")
    con_id: int | None = Field(default=None, alias="conId")
    maturity_date: str | None = Field(default=None, alias="maturityDate")
    industry: str | None = Field(default=None, alias="industry")
    instrument_type: str | None = Field(default=None, alias="instrumentType")
    trading_class: str | None = Field(default=None, alias="tradingClass")
    valid_exchanges: str | None = Field(default=None, alias="validExchanges")
    allow_sell_long: bool | None = Field(default=None, alias="allowSellLong")
    is_zero_commission_security: bool | None = Field(
        default=None, alias="isZeroCommissionSecurity"
    )
    local_symbol: str | None = Field(default=None, alias="localSymbol")
    contract_clarification_type: str | None = Field(
        default=None, alias="contractClarificationType"
    )
    classifier: str | None = Field(default=None, alias="classifier")
    currency: str | None = Field(default=None, alias="currency")
    text: str | None = Field(default=None, alias="text")
    underlying_con_id: int | None = Field(default=None, alias="underlyingConId")
    r_t_h: bool | None = Field(default=None, alias="rT_H")
    multiplier: str | None = Field(default=None, alias="multiplier")
    underlying_issuer: str | None = Field(default=None, alias="underlyingIssuer")
    contract_month: str | None = Field(default=None, alias="contractMonth")
    company_name: str | None = Field(default=None, alias="companyName")
    smart_available: bool | None = Field(default=None, alias="smartAvailable")
    exchange: str | None = Field(default=None, alias="exchange")
    category: str | None = Field(default=None, alias="category")


class IncrementRule(BaseModel):
    model_config = {"populate_by_name": True}

    lower_edge: int | None = Field(default=None, alias="lowerEdge")
    increment: int | None = Field(default=None, alias="increment")


class TifDefaults(BaseModel):
    model_config = {"populate_by_name": True}

    tif: str | None = Field(default=None, alias="tif")
    size: str | None = Field(default=None, alias="size")
    default_acct: str | None = Field(default=None, alias="defaultAcct")
    pmalgo: bool | None = Field(default=None, alias="pmalgo")


class OrderDefaults(BaseModel):
    model_config = {"populate_by_name": True}

    lmt: dict[str, Any] | None = Field(default=None, alias="lmt")


class ContractRules(BaseModel):
    model_config = {"populate_by_name": True}

    algo_eligible: bool | None = Field(default=None, alias="algoEligible")
    all_or_none_eligible: bool | None = Field(default=None, alias="allOrNoneEligible")
    cost_report: bool | None = Field(default=None, alias="costReport")
    can_trade_acct_ids: list[str] = Field(default_factory=list, alias="canTradeAcctIds")
    error: str | None = Field(default=None, alias="error")
    order_types: list[str] = Field(default_factory=list, alias="orderTypes")
    ib_algo_types: list[str] = Field(default_factory=list, alias="ibAlgoTypes")
    fraq_types: list[str] = Field(default_factory=list, alias="fraqTypes")
    force_order_preview: bool | None = Field(default=None, alias="forceOrderPreview")
    cqt_types: list[str] = Field(default_factory=list, alias="cqtTypes")
    order_defaults: OrderDefaults | None = Field(default=None, alias="orderDefaults")
    order_types_outside: list[str] = Field(
        default_factory=list, alias="orderTypesOutside"
    )
    default_size: int | None = Field(default=None, alias="defaultSize")
    cash_size: int | None = Field(default=None, alias="cashSize")
    size_increment: int | None = Field(default=None, alias="sizeIncrement")
    tif_types: list[str] = Field(default_factory=list, alias="tifTypes")
    tif_defaults: TifDefaults | None = Field(default=None, alias="tifDefaults")
    limit_price: float | None = Field(default=None, alias="limitPrice")
    stop_price: float | None = Field(default=None, alias="stopPrice")
    order_origination: str | None = Field(default=None, alias="orderOrigination")
    preview: bool | None = Field(default=None, alias="preview")
    display_size: int | None = Field(default=None, alias="displaySize")
    fraq_int: int | None = Field(default=None, alias="fraqInt")
    cash_ccy: str | None = Field(default=None, alias="cashCcy")
    cash_qty_incr: int | None = Field(default=None, alias="cashQtyIncr")
    price_magnifier: int | None = Field(default=None, alias="priceMagnifier")
    negative_capable: bool | None = Field(default=None, alias="negativeCapable")
    increment_type: int | None = Field(default=None, alias="incrementType")
    increment_rules: list[IncrementRule] = Field(
        default_factory=list, alias="incrementRules"
    )
    has_secondary: bool | None = Field(default=None, alias="hasSecondary")
    mod_types: list[str] = Field(default_factory=list, alias="modTypes")
    increment: float | None = Field(default=None, alias="increment")
    increment_digits: int | None = Field(default=None, alias="incrementDigits")


class SecType(BaseModel):
    model_config = {"populate_by_name": True}

    sec_type: str | None = Field(default=None, alias="secType")
    months: str | None = Field(default=None, alias="months")
    exchange: str | None = Field(default=None, alias="exchange")


class Issuer(BaseModel):
    model_config = {"populate_by_name": True}

    id: str | None = Field(default=None, alias="id")
    name: str | None = Field(default=None, alias="name")


class SecdefSearchResponse(BaseModel):
    model_config = {"populate_by_name": True}

    bondid: int | None = Field(default=None, alias="bondid")
    conid: str | None = Field(default=None, alias="conid")
    company_header: str | None = Field(default=None, alias="companyHeader")
    company_name: str | None = Field(default=None, alias="companyName")
    symbol: str | None = Field(default=None, alias="symbol")
    description: str | None = Field(default=None, alias="description")
    restricted: bool | None = Field(default=None, alias="restricted")
    fop: str | None = Field(default=None, alias="fop")
    opt: str | None = Field(default=None, alias="opt")
    war: str | None = Field(default=None, alias="war")
    sections: list[SecType] = Field(default_factory=list, alias="sections")
    issuers: list[Issuer] = Field(default_factory=list, alias="issuers")


class IncrementRulesItem(BaseModel):
    model_config = {"populate_by_name": True}

    lower_edge: float | None = Field(default=None, alias="lowerEdge")
    increment: float | None = Field(default=None, alias="increment")


class DisplayRuleStepItem(BaseModel):
    model_config = {"populate_by_name": True}

    decimal_digits: int | None = Field(default=None, alias="decimalDigits")
    lower_edge: float | None = Field(default=None, alias="lowerEdge")
    whole_digits: int | None = Field(default=None, alias="wholeDigits")


class DisplayRuleItem(BaseModel):
    model_config = {"populate_by_name": True}

    magnification: int | None = Field(default=None, alias="magnification")
    display_rule_step: list[DisplayRuleStepItem] = Field(
        default_factory=list, alias="displayRuleStep"
    )


class Secdef(BaseModel):
    model_config = {"populate_by_name": True}

    conid: int | None = Field(default=None, alias="conid")
    currency: str | None = Field(default=None, alias="currency")
    time: int | None = Field(default=None, alias="time")
    chinese_name: str | None = Field(default=None, alias="chineseName")
    all_exchanges: str | None = Field(default=None, alias="allExchanges")
    listing_exchange: str | None = Field(default=None, alias="listingExchange")
    country_code: str | None = Field(default=None, alias="countryCode")
    name: str | None = Field(default=None, alias="name")
    asset_class: str | None = Field(default=None, alias="assetClass")
    expiry: str | None = Field(default=None, alias="expiry")
    last_trading_day: str | None = Field(default=None, alias="lastTradingDay")
    group: str | None = Field(default=None, alias="group")
    put_or_call: str | None = Field(default=None, alias="putOrCall")
    sector: str | None = Field(default=None, alias="sector")
    sector_group: str | None = Field(default=None, alias="sectorGroup")
    strike: str | None = Field(default=None, alias="strike")
    ticker: str | None = Field(default=None, alias="ticker")
    und_conid: int | None = Field(default=None, alias="undConid")
    multiplier: int | None = Field(default=None, alias="multiplier")
    type: str | None = Field(default=None, alias="type")
    has_options: bool | None = Field(default=None, alias="hasOptions")
    full_name: str | None = Field(default=None, alias="fullName")
    is_us: bool | None = Field(default=None, alias="isUS")
    increment_rules: list[IncrementRulesItem] = Field(
        default_factory=list, alias="incrementRules"
    )
    display_rule: list[DisplayRuleItem] = Field(
        default_factory=list, alias="displayRule"
    )
    is_event_contract: bool | None = Field(default=None, alias="isEventContract")
    page_size: int | None = Field(default=None, alias="pageSize")


class TrsrvSecDefResponse(BaseModel):
    model_config = {"populate_by_name": True}

    secdef: list[Secdef] = Field(default_factory=list, alias="secdef")


class EligibleContractParticipantDetails(BaseModel):
    model_config = {"populate_by_name": True}

    code: str | None = Field(default=None, alias="code")
    status: bool | None = Field(default=None, alias="status")


class EligibleContractParticipant(BaseModel):
    model_config = {"populate_by_name": True}

    eligible_contract_participant_details: list[EligibleContractParticipantDetails] = (
        Field(default_factory=list, alias="eligibleContractParticipantDetails")
    )
    status: bool | None = Field(default=None, alias="status")
