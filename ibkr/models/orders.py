from pydantic import BaseModel, Field


class Order(BaseModel):
    model_config = {"populate_by_name": True}

    account: str | None = Field(default=None, alias="account")
    acct: str | None = Field(default=None, alias="acct")
    avg_price: str | None = Field(default=None, alias="avgPrice")
    bg_color: str | None = Field(default=None, alias="bgColor")
    cash_ccy: str | None = Field(default=None, alias="cashCcy")
    company_name: str | None = Field(default=None, alias="companyName")
    conid: str | None = Field(default=None, alias="conid")
    conidex: str | None = Field(default=None, alias="conidex")
    description1: str | None = Field(default=None, alias="description1")
    description2: str | None = Field(default=None, alias="description2")
    exchange: str | None = Field(default=None, alias="exchange")
    fg_color: str | None = Field(default=None, alias="fgColor")
    filled_quantity: str | None = Field(default=None, alias="filledQuantity")
    is_event_trading: str | None = Field(default=None, alias="isEventTrading")
    last_execution_time: str | None = Field(default=None, alias="lastExecutionTime")
    last_execution_time_r: str | None = Field(default=None, alias="lastExecutionTimeR")
    listing_exchange: str | None = Field(default=None, alias="listingExchange")
    order_desc: str | None = Field(default=None, alias="orderDesc")
    order_id: int | None = Field(default=None, alias="orderId")
    order_type: str | None = Field(default=None, alias="orderType")
    order_cancellation_by_system_reason: str | None = Field(
        default=None, alias="orderCancellationBySystemReason"
    )
    order_ccp_status: str | None = Field(default=None, alias="orderCcpStatus")
    orig_order_type: str | None = Field(default=None, alias="origOrderType")
    price: str | None = Field(default=None, alias="price")
    remaining_quantity: str | None = Field(default=None, alias="remainingQuantity")
    sec_type: str | None = Field(default=None, alias="secType")
    side: str | None = Field(default=None, alias="side")
    size_and_fills: str | None = Field(default=None, alias="sizeAndFills")
    status: str | None = Field(default=None, alias="status")
    supports_tax_opt: str | None = Field(default=None, alias="supportsTaxOpt")
    tax_optimizer_id: str | None = Field(default=None, alias="taxOptimizerId")
    ticker: str | None = Field(default=None, alias="ticker")
    time_in_force: str | None = Field(default=None, alias="timeInForce")
    total_cash_size: str | None = Field(default=None, alias="totalCashSize")
    total_size: str | None = Field(default=None, alias="totalSize")


class LiveOrdersResponse(BaseModel):
    model_config = {"populate_by_name": True}

    orders: list[Order] = Field(default_factory=list, alias="orders")
    snapshot: bool = Field(default=False, alias="snapshot")
