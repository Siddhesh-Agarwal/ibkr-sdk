# IBKR SDK: Pydantic Model Coverage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update 8 endpoints to return Pydantic models instead of dict, using model_validate_json and TypeAdapter

**Architecture:** Add missing Pydantic models for dict-returning endpoints. Extend existing model files per domain. Update client methods to use JSON validation methods.

**Tech Stack:** Python, Pydantic, pytest, ruff

---

## File Map

```
ibkr/models/
  ledger.py        # NEW - LedgerEntry, LedgerResponse
  orders.py        # MODIFY - add OrderDetail
  fa.py           # MODIFY - add FAModelAccountsDetails, ModelPositionResponse, etc.
  fyi.py          # MODIFY - add NotificationItem (FyiSettingsItem exists)
  marketdata.py   # MODIFY - history() already has union types

ibkr/client.py    # MODIFY - update 8 endpoint methods
ibkr/models/__init__.py  # MODIFY - export new models
```

---

## Task 1: Create ledger.py with LedgerEntry and LedgerResponse models

**Files:**
- Create: `ibkr/models/ledger.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_models.py
from ibkr.models.ledger import LedgerEntry, LedgerResponse

def test_ledger_entry_model_validate():
    data = {
        "acctcode": "DU123456",
        "cashbalance": 1000.0,
        "commoditymarketvalue": 500.0,
        "currency": "USD",
        "key": "LedgerList",
        "netliquidationvalue": 50000.0,
        "realizedpnl": 100.0,
        "stockmarketvalue": 10000.0,
        "unrealizedpnl": 500.0
    }
    entry = LedgerEntry.model_validate(data)
    assert entry.acctcode == "DU123456"
    assert entry.currency == "USD"

def test_ledger_response_dict_parsing():
    data = {
        "USD": {
            "acctcode": "DU123456",
            "cashbalance": 1000.0,
            "currency": "USD",
            "key": "LedgerList",
            "netliquidationvalue": 50000.0
        }
    }
    resp = LedgerResponse.model_validate(data)
    assert "USD" in resp.entries
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_models.py::test_ledger_entry_model_validate -v`
Expected: FAIL - ModuleNotFoundError

- [ ] **Step 3: Write minimal implementation**

```python
# ibkr/models/ledger.py
from pydantic import BaseModel, Field


class LedgerEntry(BaseModel):
    model_config = {"populate_by_name": True}

    acctcode: str | None = Field(default=None, alias="acctcode")
    cashbalance: float | None = Field(default=None, alias="cashbalance")
    cashbalancefxsegment: float | None = Field(default=None, alias="cashbalancefxsegment")
    commoditymarketvalue: float | None = Field(default=None, alias="commoditymarketvalue")
    corporatebondsmarketvalue: float | None = Field(default=None, alias="corporatebondsmarketvalue")
    currency: str | None = Field(default=None, alias="currency")
    dividends: float | None = Field(default=None, alias="dividends")
    exchangerate: int | None = Field(default=None, alias="exchangerate")
    funds: float | None = Field(default=None, alias="funds")
    futuremarketvalue: float | None = Field(default=None, alias="futuremarketvalue")
    futureoptionmarketvalue: float | None = Field(default=None, alias="futureoptionmarketvalue")
    futuresonlypnl: float | None = Field(default=None, alias="futuresonlypnl")
    interest: float | None = Field(default=None, alias="interest")
    issueroptionsmarketvalue: float | None = Field(default=None, alias="issueroptionsmarketvalue")
    key: str | None = Field(default=None, alias="key")
    moneyfunds: float | None = Field(default=None, alias="moneyfunds")
    netliquidationvalue: float | None = Field(default=None, alias="netliquidationvalue")
    realizedpnl: float | None = Field(default=None, alias="realizedpnl")
    secondkey: str | None = Field(default=None, alias="secondkey")
    sessionid: int | None = Field(default=None, alias="sessionid")
    settledcash: float | None = Field(default=None, alias="settledcash")
    severity: int | None = Field(default=None, alias="severity")
    stockmarketvalue: float | None = Field(default=None, alias="stockmarketvalue")
    stockoptionmarketvalue: float | None = Field(default=None, alias="stockoptionmarketvalue")
    tbillsmarketvalue: float | None = Field(default=None, alias="tbillsmarketvalue")
    tbondsmarketvalue: float | None = Field(default=None, alias="tbondsmarketvalue")
    timestamp: int | None = Field(default=None, alias="timestamp")
    unrealizedpnl: float | None = Field(default=None, alias="unrealizedpnl")
    warrantsmarketvalue: float | None = Field(default=None, alias="warrantsmarketvalue")


class LedgerResponse(BaseModel):
    model_config = {"populate_by_name": True}

    entries: dict[str, LedgerEntry] = Field(default_factory=dict)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_models.py::test_ledger_entry_model_validate tests/test_models.py::test_ledger_response_dict_parsing -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add ibkr/models/ledger.py tests/test_models.py
git commit -m "feat: add LedgerEntry and LedgerResponse models"
```

---

## Task 2: Extend orders.py with OrderDetail model

**Files:**
- Modify: `ibkr/models/orders.py`
- Test: `tests/test_models.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_models.py
from ibkr.models.orders import OrderDetail

def test_order_detail_model_validate():
    data = {
        "acct": "U1234567",
        "exchange": "IDEALPRO",
        "conidex": "15016138@IDEALPRO",
        "conid": 15016138,
        "account": "DU4355398",
        "orderId": 1370093238,
        "status": "Filled"
    }
    order = OrderDetail.model_validate(data)
    assert order.acct == "U1234567"
    assert order.conid == 15016138
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_models.py::test_order_detail_model_validate -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

Append to `ibkr/models/orders.py`:

```python
class OrderDetail(BaseModel):
    model_config = {"populate_by_name": True}

    acct: str | None = Field(default=None, alias="acct")
    account: str | None = Field(default=None, alias="account")
    account_title: str | None = Field(default=None, alias="accountTitle")
    account_van: str | None = Field(default=None, alias="accountVan")
    active: str | None = Field(default=None, alias="active")
    algo_base_liq: str | None = Field(default=None, alias="algoBaseLiq")
    algo_params: list[dict] | None = Field(default=None, alias="algoParams")
    algo_strategy: str | None = Field(default=None, alias="algoStrategy")
    algo_try_to_end: str | None = Field(default=None, alias="algoTryToEnd")
    allow_end: str | None = Field(default=None, alias="allowEnd")
    attached_allow: str | None = Field(default=None, alias="attachedAllow")
    attached_parent: int | None = Field(default=None, alias="attachedParent")
    auth_time: int | None = Field(default=None, alias="authTime")
    avg_fill_size: float | None = Field(default=None, alias="avgFillSize")
    balance: str | None = Field(default=None, alias="balance")
    basis: str | None = Field(default=None, alias="basis")
    basis_type: str | None = Field(default=None, alias="basisType")
    bg_color: str | None = Field(default=None, alias="bgColor")
    book_basket: str | None = Field(default=None, alias="bookBasket")
    buyer: str | None = Field(default=None, alias="buyer")
    cancel_color: str | None = Field(default=None, alias="cancelColor")
    cancel_time: str | None = Field(default=None, alias="cancelTime")
    cash_ccy: str | None = Field(default=None, alias="cashCcy")
    clearing_firm: str | None = Field(default=None, alias="clearingFirm")
    clearing_id: str | None = Field(default=None, alias="clearingId")
    clearing_name: str | None = Field(default=None, alias="clearingName")
    close: str | None = Field(default=None, alias="close")
    code: str | None = Field(default=None, alias="code")
    collection: str | None = Field(default=None, alias="collection")
    combo_leg_description: str | None = Field(default=None, alias="comboLegDescription")
    combo_routes: str | None = Field(default=None, alias="comboRoutes")
    conidex: str | None = Field(default=None, alias="conidex")
    conid: int | None = Field(default=None, alias="conid")
    contract_desc: str | None = Field(default=None, alias="contractDesc")
    contract_month: str | None = Field(default=None, alias="contractMonth")
    country_code: str | None = Field(default=None, alias="countryCode")
    depth_mkt_priority: str | None = Field(default=None, alias="depthMktPriority")
    description1: str | None = Field(default=None, alias="description1")
    description2: str | None = Field(default=None, alias="description2")
    discrete: str | None = Field(default=None, alias="discrete")
    display_size: str | None = Field(default=None, alias="displaySize")
    dont_init_seq: str | None = Field(default=None, alias="dontInitSeq")
    exchange: str | None = Field(default=None, alias="exchange")
    expiry: str | None = Field(default=None, alias="expiry")
    external: str | None = Field(default=None, alias="external")
    f_g_color: str | None = Field(default=None, alias="fGColor")
    fa_group: str | None = Field(default=None, alias="faGroup")
    fa_method: str | None = Field(default=None, alias="faMethod")
    fa_percentages: str | None = Field(default=None, alias="faPercentages")
    filled_amount: str | None = Field(default=None, alias="filledAmount")
    filled_qty: str | None = Field(default=None, alias="filledQty")
    firm: str | None = Field(default=None, alias="firm")
    flag: str | None = Field(default=None, alias="flag")
    front_device_name: str | None = Field(default=None, alias="frontDeviceName")
    fu_indicator: str | None = Field(default=None, alias="fuIndicator")
    fxid: str | None = Field(default=None, alias="fxid")
    g_Color: str | None = Field(default=None, alias="gColor")
    gamma: str | None = Field(default=None, alias="gamma")
    hedge: str | None = Field(default=None, alias="hedge")
    hedge_param: str | None = Field(default=None, alias="hedgeParam")
    hist: str | None = Field(default=None, alias="hist")
    host: str | None = Field(default=None, alias="host")
    is_cash: str | None = Field(default=None, alias="isCash")
    is_connected: str | None = Field(default=None, alias="isConnected")
    is_event_trading: str | None = Field(default=None, alias="isEventTrading")
    is_flex: str | None = Field(default=None, alias="isFlex")
    is_hot: str | None = Field(default=None, alias="isHot")
    is_marketable: str | None = Field(default=None, alias="isMarketable")
    is_mm_flex_combo: str | None = Field(default=None, alias="isMmFlexCombo")
    is_opt_flex: str | None = Field(default=None, alias="isOptFlex")
    is_pricing: str | None = Field(default=None, alias="isPricing")
    is_quote: str | None = Field(default=None, alias="isQuote")
    is_single: str | None = Field(default=None, alias="isSingle")
    is_size: str | None = Field(default=None, alias="isSize")
    is_spread: str | None = Field(default=None, alias="isSpread")
    is_total: str | None = Field(default=None, alias="isTotal")
    issuer: str | None = Field(default=None, alias="issuer")
    last_execution_time: str | None = Field(default=None, alias="lastExecutionTime")
    last_execution_time_r: int | None = Field(default=None, alias="lastExecutionTime_r")
    last_fill_price: str | None = Field(default=None, alias="lastFillPrice")
    last_fill_size: str | None = Field(default=None, alias="lastFillSize")
    last_price: str | None = Field(default=None, alias="lastPrice")
    last_qty: str | None = Field(default=None, alias="lastQty")
    last_side: str | None = Field(default=None, alias="lastSide")
    layer: str | None = Field(default=None, alias="layer")
    leg_total_qty: str | None = Field(default=None, alias="legTotalQty")
    level_of_no_open_orders: str | None = Field(default=None, alias="levelOfNoOpenOrders")
    listing_exchange: str | None = Field(default=None, alias="listingExchange")
    loc_amt: str | None = Field(default=None, alias="locAmt")
    loc_borrow: str | None = Field(default=None, alias="locBorrow")
    loc_borrow_far: str | None = Field(default=None, alias="locBorrowFar")
    loc_borrow_near: str | None = Field(default=None, alias="locBorrowNear")
    loc_borrow_status: str | None = Field(default=None, alias="locBorrowStatus")
    loc_limit_connection: str | None = Field(default=None, alias="locLimitConnection")
    loc_warning: str | None = Field(default=None, alias="locWarning")
    market_rule: str | None = Field(default=None, alias="marketRule")
    marketing_permission: str | None = Field(default=None, alias="marketingPermission")
    max_show: str | None = Field(default=None, alias="maxShow")
    mkt_rule: str | None = Field(default=None, alias="mktRule")
    mktdata_con_id: str | None = Field(default=None, alias="mktdataConId")
    multiplier: str | None = Field(default=None, alias="multiplier")
    net_money: str | None = Field(default=None, alias="netMoney")
    non_mkt_margin: str | None = Field(default=None, alias="nonMktMargin")
    num_batch: str | None = Field(default=None, alias="numBatch")
    oca_group_id: str | None = Field(default=None, alias="ocaGroupId")
    oca_name: str | None = Field(default=None, alias="ocaName")
    oca_type: str | None = Field(default=None, alias="ocaType")
    only_ahm: str | None = Field(default=None, alias="onlyAhM")
    open_close: str | None = Field(default=None, alias="openClose")
    open_time: str | None = Field(default=None, alias="openTime")
    open_time_r: int | None = Field(default=None, alias="openTime_r")
    opt_id: str | None = Field(default=None, alias="optId")
    order_id: int | None = Field(default=None, alias="orderId")
    order_ref: str | None = Field(default=None, alias="orderRef")
    order_side: str | None = Field(default=None, alias="orderSide")
    order_source: str | None = Field(default=None, alias="orderSource")
    order_status: str | None = Field(default=None, alias="orderStatus")
    order_sub_type: str | None = Field(default=None, alias="orderSubType")
    order_type: str | None = Field(default=None, alias="orderType")
    order_desc: str | None = Field(default=None, alias="orderDesc")
    organic_flag: int | None = Field(default=None, alias="organicFlag")
    orig_order_type: str | None = Field(default=None, alias="origOrderType")
    origin: str | None = Field(default=None, alias="origin")
    other: str | None = Field(default=None, alias="other")
    parent_id: int | None = Field(default=None, alias="parentId")
    peg_current_reference: str | None = Field(default=None, alias="pegCurrentReference")
    peg_pep_name: str | None = Field(default=None, alias="pegPepName")
    peg_security_type: str | None = Field(default=None, alias="pegSecurityType")
    peg_strike_type: str | None = Field(default=None, alias="pegStrikeType")
    perm_id: int | None = Field(default=None, alias="permId")
    position: str | None = Field(default=None, alias="position")
    price: str | None = Field(default=None, alias="price")
    price_change: str | None = Field(default=None, alias="priceChange")
    price_cond: str | None = Field(default=None, alias="priceCond")
    price_linked: str | None = Field(default=None, alias="priceLinked")
    priority: str | None = Field(default=None, alias="priority")
    protected_cash: str | None = Field(default=None, alias="protectedCash")
    provider: str | None = Field(default=None, alias="provider")
    quantum: str | None = Field(default=None, alias="quantum")
    random_dollar_id: str | None = Field(default=None, alias="randomDollarId")
    re_alloc_broker: str | None = Field(default=None, alias="reAllocBroker")
    re_alloc_firm: str | None = Field(default=None, alias="reAllocFirm")
    readable_desc: str | None = Field(default=None, alias="readableDesc")
    remaining_qty: str | None = Field(default=None, alias="remainingQty")
    replaceable: str | None = Field(default=None, alias="replaceable")
    report_options: str | None = Field(default=None, alias="reportOptions")
    reset_time: str | None = Field(default=None, alias="resetTime")
    resting: str | None = Field(default=None, alias="resting")
    revision: int | None = Field(default=None, alias="revision")
    route: str | None = Field(default=None, alias="route")
    routes: str | None = Field(default=None, alias="routes")
    scale: str | None = Field(default=None, alias="scale")
    scale_ord_type: str | None = Field(default=None, alias="scaleOrdType")
    scale_auto_inc: str | None = Field(default=None, alias="scaleAutoInc")
    scale_init_level: str | None = Field(default=None, alias="scaleInitLevel")
    scale_init_pos: str | None = Field(default=None, alias="scaleInitPos")
    scale_init_set: str | None = Field(default=None, alias="scaleInitSet")
    scale_rlh: str | None = Field(default=None, alias="scaleRlH")
    sec_type: str | None = Field(default=None, alias="secType")
    serial: str | None = Field(default=None, alias="serial")
    ser_num: int | None = Field(default=None, alias="serNum")
    settlement: str | None = Field(default=None, alias="settlement")
    shared: str | None = Field(default=None, alias="shared")
    size_and_fills: str | None = Field(default=None, alias="sizeAndFills")
    size_linked: str | None = Field(default=None, alias="sizeLinked")
    small_trade: str | None = Field(default=None, alias="smallTrade")
    smart: str | None = Field(default=None, alias="smart")
    spread: str | None = Field(default=None, alias="spread")
    state: str | None = Field(default=None, alias="state")
    status: str | None = Field(default=None, alias="status")
    stipulations: str | None = Field(default=None, alias="stipulations")
    stop_price: str | None = Field(default=None, alias="stopPrice")
    stop_trigger_method: str | None = Field(default=None, alias="stopTriggerMethod")
    submission_time: str | None = Field(default=None, alias="submissionTime")
    submitting_user: str | None = Field(default=None, alias="submittingUser")
    subscribed: str | None = Field(default=None, alias="subscribed")
    supports_tax_opt: str | None = Field(default=None, alias="supportsTaxOpt")
    symbol: str | None = Field(default=None, alias="symbol")
    t: str | None = Field(default=None, alias="t")
    tax_opt: str | None = Field(default=None, alias="taxOpt")
    text: str | None = Field(default=None, alias="text")
    tick_link: str | None = Field(default=None, alias="tickLink")
    tier: str | None = Field(default=None, alias="tier")
    time_cond: str | None = Field(default=None, alias="timeCond")
    time_in_force: str | None = Field(default=None, alias="timeInForce")
    timeout: str | None = Field(default=None, alias="timeout")
    ticker: str | None = Field(default=None, alias="ticker")
    trail_limit_price: str | None = Field(default=None, alias="trailLimitPrice")
    trailing_percent: str | None = Field(default=None, alias="trailingPercent")
    trans_id: int | None = Field(default=None, alias="transId")
    trigger_action: str | None = Field(default=None, alias="triggerAction")
    trigger_contract: str | None = Field(default=None, alias="triggerContract")
    trigger_exchange: str | None = Field(default=None, alias="triggerExchange")
    trigger_price: str | None = Field(default=None, alias="triggerPrice")
    trigger_section: str | None = Field(default=None, alias="triggerSection")
    trigger_time: str | None = Field(default=None, alias="triggerTime")
    trigger_time_r: int | None = Field(default=None, alias="triggerTime_r")
    type: str | None = Field(default=None, alias="type")
    underlying_con_id: int | None = Field(default=None, alias="underlyingConId")
    user: str | None = Field(default=None, alias="user")
    user_account: str | None = Field(default=None, alias="userAccount")
    user_initials: str | None = Field(default=None, alias="userInitials")
    user_long: str | None = Field(default=None, alias="userLong")
    user_partial_fill: str | None = Field(default=None, alias="userPartialFill")
    vol_count: str | None = Field(default=None, alias="volCount")
    volatility: str | None = Field(default=None, alias="volatility")
    volatility_type: str | None = Field(default=None, alias="volatilityType")
    what_if: str | None = Field(default=None, alias="whatIf")
    withholding: str | None = Field(default=None, alias="withholding")
    x_Color: str | None = Field(default=None, alias="xColor")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_models.py::test_order_detail_model_validate -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add ibkr/models/orders.py tests/test_models.py
git commit -m "feat: add OrderDetail model"
```

---

## Task 3: Extend fa.py with FAModelAccountsDetails, ModelPositionResponse, and related models

**Files:**
- Modify: `ibkr/models/fa.py`
- Test: `tests/test_models.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_models.py
from ibkr.models.fa import FAModelAccountsDetails, ModelPositionResponse, PositionListItem, CashItem

def test_fa_model_accounts_details():
    data = {
        "accountInfoList": [
            {
                "account": "DUN884097",
                "accountImbalance": "0.904036",
                "alias": "",
                "baseCcyAccount": "USD",
                "costBasis": "0",
                "exchangeRate": 1.0,
                "nlv": "0",
                "numInstrumentsOutsideRange": 2,
                "unrealizedPnL": "0"
            }
        ],
        "baseCcyMaster": "USD",
        "model": "MCPAPI01",
        "reqID": 131
    }
    result = FAModelAccountsDetails.model_validate(data)
    assert result.model == "MCPAPI01"
    assert len(result.account_info_list) == 1

def test_model_position_response():
    data = {
        "cash": [{"actual": 0, "ccy": "USD", "exchangeRate": 1, "mv": 0, "target": 0.096}],
        "mismatched": False,
        "model": "MCPAPI01",
        "nlv": 0.0,
        "positionList": [
            {"actual": "0", "ccy": "USD", "conid": 268084, "instrument": "CSCO", "mv": "0", "position": "0", "target": "0.432"}
        ],
        "positionTs": 1769614805464,
        "reqID": 540607,
        "stkOnly": True,
        "subscriptionStatus": 1,
        "totalDlv": 0.0,
        "totalMv": 0.0
    }
    result = ModelPositionResponse.model_validate(data)
    assert result.model == "MCPAPI01"
    assert len(result.position_list) == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_models.py::test_fa_model_accounts_details tests/test_models.py::test_model_position_response -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

Append to `ibkr/models/fa.py`:

```python
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
    actual_range_max: str | None = Field(default=None, alias="actualRangeMax")
    actual_range_min: str | None = Field(default=None, alias="actualRangeMin")
    ccy: str | None = Field(default=None, alias="ccy")
    conid: int | None = Field(default=None, alias="conid")
    dlv: str | None = Field(default=None, alias="dlv")
    exchange_rate: int | None = Field(default=None, alias="exchangeRate")
    flags: int | None = Field(default=None, alias="flags")
    instrument: str | None = Field(default=None, alias="instrument")
    instrument_imbalance: float | None = Field(default=None, alias="instrumentImbalance")
    mismatch_type: float | None = Field(default=None, alias="mismatchType")
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_models.py::test_fa_model_accounts_details tests/test_models.py::test_model_position_response -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add ibkr/models/fa.py tests/test_models.py
git commit -m "feat: add FAModelAccountsDetails and ModelPositionResponse models"
```

---

## Task 4: Add NotificationItem model to fyi.py

**Files:**
- Modify: `ibkr/models/fyi.py`
- Test: `tests/test_models.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_models.py
from ibkr.models.fyi import NotificationItem

def test_notification_item():
    data = {
        "R": "0",
        "D": "1710847062.0",
        "MS": "FYI: Changes in Analyst Ratings",
        "MD": "<html>Notification content</html>",
        "ID": "2024031947509444",
        "HT": 0,
        "FC": "PF"
    }
    item = NotificationItem.model_validate(data)
    assert item.ms == "FYI: Changes in Analyst Ratings"
    assert item.id == "2024031947509444"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_models.py::test_notification_item -v`
Expected: FAIL

- [ ] **Step 3: Write minimal implementation**

Append to `ibkr/models/fyi.py`:

```python
class NotificationItem(BaseModel):
    model_config = {"populate_by_name": True}

    r: str | None = Field(default=None, alias="R")
    d: str | None = Field(default=None, alias="D")
    ms: str | None = Field(default=None, alias="MS")
    md: str | None = Field(default=None, alias="MD")
    id: str | None = Field(default=None, alias="ID")
    ht: int | None = Field(default=None, alias="HT")
    fc: str | None = Field(default=None, alias="FC")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_models.py::test_notification_item -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add ibkr/models/fyi.py tests/test_models.py
git commit -m "feat: add NotificationItem model to fyi"
```

---

## Task 5: Update models/__init__.py exports

**Files:**
- Modify: `ibkr/models/__init__.py`

- [ ] **Step 1: Update exports**

Add to imports:
```python
from ibkr.models.ledger import (
    LedgerEntry,
    LedgerResponse,
)
from ibkr.models.fyi import (
    NotificationItem,
)
from ibkr.models.fa import (
    AccountInfoItem,
    CashItem,
    FAModelAccountsDetails,
    ModelPositionResponse,
    PositionListItem,
)
from ibkr.models.orders import (
    OrderDetail,
)
```

Add to `__all__`:
```python
"AccountInfoItem",
"CashItem",
"FAModelAccountsDetails",
"LedgerEntry",
"LedgerResponse",
"ModelPositionResponse",
"NotificationItem",
"OrderDetail",
"PositionListItem",
```

- [ ] **Step 2: Verify imports work**

Run: `uv run python -c "from ibkr.models import *; print('OK')"`
Expected: OK

- [ ] **Step 3: Commit**

```bash
git add ibkr/models/__init__.py
git commit -m "feat: export new models"
```

---

## Task 6: Update client.py endpoint methods

**Files:**
- Modify: `ibkr/client.py`

- [ ] **Step 1: Update PortfolioAPI.ledger()**

```python
from ibkr.models.ledger import LedgerResponse

def ledger(self, account_id: str) -> LedgerResponse:
    data = self.client._get(f"/v1/api/portfolio/{account_id}/ledger")
    return LedgerResponse.model_validate(data)
```

- [ ] **Step 2: Update OrdersAPI.get_order()**

```python
from ibkr.models.orders import OrderDetail

def get_order(self, account_id: str, order_id: str) -> OrderDetail:
    data = self.client._get(
        f"/v1/api/iserver/account/{account_id}/order/{order_id}"
    )
    return OrderDetail.model_validate(data)
```

- [ ] **Step 3: Update ContractAPI.info()**

```python
def info(self, conid: int) -> ContractInfo:
    data = self.client._get(f"/v1/api/iserver/contract/{conid}/info")
    return ContractInfo.model_validate(data)
```

- [ ] **Step 4: Update FAAPI.account_details()**

```python
from ibkr.models.fa import FAModelAccountsDetails

def account_details(self) -> FAModelAccountsDetails:
    data = self.client._get("/v1/api/fa/model/accounts-details")
    return FAModelAccountsDetails.model_validate(data)
```

- [ ] **Step 5: Update FAAPI.positions()**

```python
from ibkr.models.fa import ModelPositionResponse

def positions(self, model: str) -> ModelPositionResponse:
    data = self.client._get("/v1/api/fa/model/positions", params={"model": model})
    return ModelPositionResponse.model_validate(data)
```

- [ ] **Step 6: Update FYIAPI.notifications()**

```python
from pydantic import TypeAdapter
from ibkr.models.fyi import NotificationItem

def notifications(self) -> list[NotificationItem]:
    data = self.client._get("/v1/api/fyi/notifications")
    return TypeAdapter(list[NotificationItem]).validate_json(
        json.dumps(data)
    )
```

- [ ] **Step 7: Update FYIAPI.settings()**

```python
from pydantic import TypeAdapter
from ibkr.models.fyi import FyiSettingsItem

def settings(self) -> list[FyiSettingsItem]:
    data = self.client._get("/v1/api/fyi/settings")
    return TypeAdapter(list[FyiSettingsItem]).validate_json(
        json.dumps(data)
    )
```

- [ ] **Step 8: Run tests**

Run: `uv run pytest tests/ -v`

- [ ] **Step 9: Run lint**

Run: `ruff check .`

- [ ] **Step 10: Commit**

```bash
git add ibkr/client.py
git commit -m "feat: update endpoint methods to return Pydantic models"
```

---

## Task 7: Final verification

- [ ] **Step 1: Run full test suite**

Run: `uv run pytest tests/ -v`

- [ ] **Step 2: Run full lint check**

Run: `ruff check .`

---

## Spec Coverage Check

| Spec Requirement | Task |
|------------------|------|
| PortfolioAPI.ledger() returns LedgerResponse | Task 1, 6 |
| OrdersAPI.get_order() returns OrderDetail | Task 2, 6 |
| MarketDataAPI.history() uses existing union models | Already done |
| ContractAPI.info() returns ContractInfo | Task 6 |
| FAAPI.account_details() returns FAModelAccountsDetails | Task 3, 6 |
| FAAPI.positions() returns ModelPositionResponse | Task 3, 6 |
| FYIAPI.notifications() returns list[NotificationItem] | Task 4, 6 |
| FYIAPI.settings() returns list[FyiSettingsItem] | Task 6 |
| All new models exported | Task 5 |