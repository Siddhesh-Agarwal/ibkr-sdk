
from pydantic import BaseModel, Field


class Order(BaseModel):
    account: str | None = None
    acct: str | None = None
    avgPrice: str | None = None
    bgColor: str | None = None
    cashCcy: str | None = None
    companyName: str | None = None
    conid: str | None = None
    conidex: str | None = None
    description1: str | None = None
    description2: str | None = None
    exchange: str | None = None
    fgColor: str | None = None
    filledQuantity: str | None = None
    isEventTrading: str | None = None
    lastExecutionTime: str | None = None
    lastExecutionTime_r: str | None = None
    listingExchange: str | None = None
    orderDesc: str | None = None
    orderId: int | None = None
    orderType: str | None = None
    order_cancellation_by_system_reason: str | None = None
    order_ccp_status: str | None = None
    origOrderType: str | None = None
    price: str | None = None
    remainingQuantity: str | None = None
    secType: str | None = None
    side: str | None = None
    sizeAndFills: str | None = None
    status: str | None = None
    supportsTaxOpt: str | None = None
    taxOptimizerId: str | None = None
    ticker: str | None = None
    timeInForce: str | None = None
    totalCashSize: str | None = None
    totalSize: str | None = None


class LiveOrdersResponse(BaseModel):
    orders: list[Order] = Field(default_factory=list)
    snapshot: bool = False
