from pydantic import BaseModel, Field


class FailedTickleResponse(BaseModel):
    model_config = {"populate_by_name": True}

    error: str | None = Field(default=None, alias="error")


class AccountInfoItem(BaseModel):
    model_config = {"populate_by_name": True}

    account: str | None = Field(default=None, alias="account")
    account_imbalance: str | None = Field(default=None, alias="accountImbalance")
    alias: str | None = Field(default=None, alias="alias")
    base_ccy_account: str | None = Field(default=None, alias="baseCcyAccount")
    cash_in_independent: str | None = Field(default=None, alias="cashInIndependent")
    cost_basis: str | None = Field(default=None, alias="costBasis")
    exchange_rate: float | None = Field(default=None, alias="exchangeRate")
    nlv: str | None = Field(default=None, alias="nlv")
    num_instruments_outside_range: int | None = Field(default=None, alias="numInstrumentsOutsideRange")
    unrealized_pnl: str | None = Field(default=None, alias="unrealizedPnL")


class FAModelAccountsDetails(BaseModel):
    model_config = {"populate_by_name": True}

    account_info_list: list[AccountInfoItem] = Field(default_factory=list, alias="accountInfoList")
    base_ccy_master: str | None = Field(default=None, alias="baseCcyMaster")
    model: str | None = Field(default=None, alias="model")
    req_id: int | None = Field(default=None, alias="reqID")


class CashItem(BaseModel):
    model_config = {"populate_by_name": True}

    actual: float | None = Field(default=None, alias="actual")
    ccy: str | None = Field(default=None, alias="ccy")
    exchange_rate: float | None = Field(default=None, alias="exchangeRate")
    instrument_imbalance: float | None = Field(default=None, alias="instrumentImbalance")
    mv: float | None = Field(default=None, alias="mv")
    target: float | None = Field(default=None, alias="target")


class PositionListItem(BaseModel):
    model_config = {"populate_by_name": True}

    actual: str | None = Field(default=None, alias="actual")
    actual_range_max: float | None = Field(default=None, alias="actualRangeMax")
    actual_range_min: float | None = Field(default=None, alias="actualRangeMin")
    ccy: str | None = Field(default=None, alias="ccy")
    conid: int | None = Field(default=None, alias="conid")
    dlv: float | None = Field(default=None, alias="dlv")
    exchange_rate: float | None = Field(default=None, alias="exchangeRate")
    flags: str | None = Field(default=None, alias="flags")
    instrument: str | None = Field(default=None, alias="instrument")
    instrument_imbalance: float | None = Field(default=None, alias="instrumentImbalance")
    mismatch_type: str | None = Field(default=None, alias="mismatchType")
    mv: str | None = Field(default=None, alias="mv")
    position: str | None = Field(default=None, alias="position")
    target: str | None = Field(default=None, alias="target")


class ModelPositionResponse(BaseModel):
    model_config = {"populate_by_name": True}

    cash: list[CashItem] = Field(default_factory=list, alias="cash")
    mismatched: bool | None = Field(default=None, alias="mismatched")
    model: str | None = Field(default=None, alias="model")
    nlv: float | None = Field(default=None, alias="nlv")
    position_list: list[PositionListItem] = Field(default_factory=list, alias="positionList")
    position_ts: int | None = Field(default=None, alias="positionTs")
    req_id: int | None = Field(default=None, alias="reqID")
    stk_only: bool | None = Field(default=None, alias="stkOnly")
    subscription_status: int | None = Field(default=None, alias="subscriptionStatus")
    total_dlv: float | None = Field(default=None, alias="totalDlv")
    total_mv: float | None = Field(default=None, alias="totalMv")
