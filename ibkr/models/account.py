
from pydantic import BaseModel, Field


class CashBalance(BaseModel):
    currency: str
    balance: int
    settledCash: int


class AccountSummaryResponse(BaseModel):
    accountType: str | None = None
    status: str | None = None
    balance: int | None = None
    SMA: int | None = None
    buyingPower: int | None = None
    availableFunds: int | None = None
    excessLiquidity: int | None = None
    netLiquidationValue: int | None = None
    equityWithLoanValue: int | None = None
    regTLoan: int | None = None
    securitiesGVP: int | None = None
    totalCashValue: int | None = None
    accruedInterest: int | None = None
    regTMargin: int | None = None
    initialMargin: int | None = None
    maintenanceMargin: int | None = None
    cashBalances: list[CashBalance] = Field(default_factory=list)


class AccountAttributes(BaseModel):
    accountId: str
    accountTitle: str | None = None
    accountVan: str | None = None
    acctCustType: str | None = None
    brokerageAccess: bool | None = None
    businessType: str | None = None
    currency: str | None = None
    displayName: str | None = None
    id: str | None = None
    type: str | None = None
