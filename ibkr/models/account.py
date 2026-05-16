from pydantic import BaseModel, Field


class CashBalance(BaseModel):
    model_config = {"populate_by_name": True}

    currency: str = Field(alias="currency")
    balance: int = Field(alias="balance")
    settled_cash: int = Field(alias="settledCash")


class AccountSummaryResponse(BaseModel):
    model_config = {"populate_by_name": True}

    account_type: str | None = Field(default=None, alias="accountType")
    status: str | None = Field(default=None, alias="status")
    balance: int | None = Field(default=None, alias="balance")
    sma: int | None = Field(default=None, alias="sma")
    buying_power: int | None = Field(default=None, alias="buyingPower")
    available_funds: int | None = Field(default=None, alias="availableFunds")
    excess_liquidity: int | None = Field(default=None, alias="excessLiquidity")
    net_liquidation_value: int | None = Field(default=None, alias="netLiquidationValue")
    equity_with_loan_value: int | None = Field(default=None, alias="equityWithLoanValue")
    reg_t_loan: int | None = Field(default=None, alias="regTLoan")
    securities_gvp: int | None = Field(default=None, alias="securitiesGVP")
    total_cash_value: int | None = Field(default=None, alias="totalCashValue")
    accrued_interest: int | None = Field(default=None, alias="accruedInterest")
    reg_t_margin: int | None = Field(default=None, alias="regTMargin")
    initial_margin: int | None = Field(default=None, alias="initialMargin")
    maintenance_margin: int | None = Field(default=None, alias="maintenanceMargin")
    cash_balances: list[CashBalance] = Field(default_factory=list, alias="cashBalances")


class AccountAttributes(BaseModel):
    model_config = {"populate_by_name": True}

    account_id: str = Field(alias="accountId")
    account_title: str | None = Field(default=None, alias="accountTitle")
    account_van: str | None = Field(default=None, alias="accountVan")
    acct_cust_type: str | None = Field(default=None, alias="acctCustType")
    brokerage_access: bool | None = Field(default=None, alias="brokerageAccess")
    business_type: str | None = Field(default=None, alias="businessType")
    currency: str | None = Field(default=None, alias="currency")
    display_name: str | None = Field(default=None, alias="displayName")
    id: str | None = Field(default=None, alias="id")
    type: str | None = Field(default=None, alias="type")
