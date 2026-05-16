from ibkr.models.account import AccountAttributes, AccountSummaryResponse
from ibkr.models.marketdata import IserverSnapshot
from ibkr.models.orders import LiveOrdersResponse, Order
from ibkr.models.portfolio import IndividualPosition


class TestAccountAttributes:
    def test_from_example(self):
        account_example = {
            "PrepaidCrypto-Z": False,
            "PrepaidCrypto-P": False,
            "accountAlias": None,
            "accountId": "DU123456",
            "accountTitle": "John Smith, LLC",
            "accountVan": "DU123456",
            "acctCustType": "LLC",
            "brokerageAccess": True,
            "businessType": "IB_SALES",
            "displayName": "John Smith, LLC",
            "currency": "USD",
            "id": "DU123456",
            "type": "DEMO",
        }
        acct = AccountAttributes(**account_example)
        assert acct.account_id == "DU123456"
        assert acct.currency == "USD"
        assert acct.account_title == "John Smith, LLC"
        assert acct.business_type == "IB_SALES"

    def test_minimal_account(self):
        acct = AccountAttributes(accountId="DU999999")
        assert acct.account_id == "DU999999"
        assert acct.currency is None


class TestIndividualPosition:
    def test_from_example(self):
        position_example = {
            "acctId": "DU123456",
            "assetClass": "STK",
            "avgCost": 150.25,
            "avgPrice": 150.25,
            "conid": 123456,
            "contractDesc": "AAPL US REAL",
            "countryCode": "US",
            "currency": "USD",
            "expiry": None,
            "fullName": "APPLE INC",
            "group": "STOCK",
            "hasOptions": False,
            "isUS": True,
            "listingExchange": "NASDAQ",
            "mktPrice": 155.00,
            "mktValue": 15500.0,
            "model": None,
            "multiplier": None,
            "name": "AAPL",
            "position": 100.0,
            "putOrCall": None,
            "realizedPnl": 0.0,
            "sector": "Technology",
            "strike": None,
            "ticker": "AAPL",
            "type": "AAPL",
            "undConid": None,
            "unrealizedPnl": 475.0,
        }
        pos = IndividualPosition(**position_example)
        assert pos.conid == 123456
        assert pos.ticker == "AAPL"
        assert pos.position == 100.0
        assert pos.unrealized_pnl == 475.0

    def test_minimal_position(self):
        pos = IndividualPosition(conid=999)
        assert pos.conid == 999


class TestLiveOrdersResponse:
    def test_from_example(self):
        orders_example = {
            "orders": [
                {
                    "account": "DU123456",
                    "acct": "DU123456",
                    "avgPrice": "0.0",
                    "bgColor": "-3816855",
                    "cashCcy": "USD",
                    "companyName": "APPLE INC",
                    "conid": "123456",
                    "conidex": "123456--NASDAQ",
                    "description1": "AAPL",
                    "description2": "NASDAQ",
                    "exchange": "NASDAQ",
                    "fgColor": "-1",
                    "filledQuantity": "0",
                    "isEventTrading": "N",
                    "lastExecutionTime": "",
                    "lastExecutionTime_r": "",
                    "listingExchange": "NASDAQ",
                    "orderDesc": "Buy 100 @ MKT",
                    "orderId": 12345,
                    "orderType": "MKT",
                    "origOrderType": "MKT",
                    "price": "0.0",
                    "remainingQuantity": "100",
                    "secType": "STK",
                    "side": "BUY",
                    "sizeAndFills": "0",
                    "status": "PendingSubmit",
                    "supportsTaxOpt": "N",
                    "taxOptimizerId": None,
                    "ticker": "AAPL",
                    "timeInForce": "DAY",
                    "totalCashSize": "",
                    "totalSize": "100",
                }
            ],
            "snapshot": True,
        }
        response = LiveOrdersResponse(**orders_example)
        assert len(response.orders) == 1
        assert response.orders[0].ticker == "AAPL"
        assert response.orders[0].order_id == 12345
        assert response.snapshot is True

    def test_empty_orders(self):
        response = LiveOrdersResponse()
        assert response.orders == []
        assert response.snapshot is False


class TestOrder:
    def test_order_parsing(self):
        order_data = {
            "account": "DU123456",
            "conid": "123456",
            "orderId": 99999,
            "orderType": "LMT",
            "price": "150.00",
            "side": "BUY",
            "status": "Filled",
            "ticker": "AAPL",
        }
        order = Order(**order_data)
        assert order.conid == "123456"
        assert order.order_type == "LMT"
        assert order.price == "150.00"

    def test_order_with_optional_fields(self):
        order_data = {
            "account": "DU123456",
            "avgPrice": "149.50",
            "filledQuantity": "50",
            "remainingQuantity": "50",
            "secType": "STK",
            "timeInForce": "GTC",
            "totalSize": "100",
        }
        order = Order(**order_data)
        assert order.filled_quantity == "50"
        assert order.time_in_force == "GTC"


class TestIserverSnapshot:
    def test_snapshot_parsing(self):
        snapshot_data = {
            "conidEx": "123456--NASDAQ",
            "conid": 123456,
            "field_6509": "155.50",
            "_updated": 1234567890,
            "field_6119": "155.50",
            "server_id": "12345",
            "MD_Field": {
                "31": "155.50",
                "32": "155.50",
                "33": "155.50",
                "34": "155.50",
            },
        }
        snapshot = IserverSnapshot(**snapshot_data)
        assert snapshot.conid == 123456
        assert snapshot.server_id == "12345"

    def test_empty_snapshot(self):
        snapshot = IserverSnapshot()
        assert snapshot.conid is None


class TestAccountSummaryResponse:
    def test_account_summary_with_cash_balances(self):
        summary_data = {
            "accountType": "CASH",
            "status": "ACTIVE",
            "balance": 100000,
            "SMA": 50000,
            "buyingPower": 200000,
            "availableFunds": 75000,
            "excessLiquidity": 80000,
            "netLiquidationValue": 100000,
            "equityWithLoanValue": 100000,
            "regTLoan": 0,
            "securitiesGVP": 95000,
            "totalCashValue": 100000,
            "accruedInterest": 100,
            "regTMargin": 0,
            "initialMargin": 25000,
            "maintenanceMargin": 20000,
            "cashBalances": [
                {"currency": "USD", "balance": 80000, "settledCash": 80000},
                {"currency": "EUR", "balance": 20000, "settledCash": 20000},
            ],
        }
        summary = AccountSummaryResponse(**summary_data)
        assert summary.account_type == "CASH"
        assert len(summary.cash_balances) == 2
        assert summary.cash_balances[0].currency == "USD"

    def test_account_summary_minimal(self):
        summary = AccountSummaryResponse()
        assert summary.cash_balances == []
