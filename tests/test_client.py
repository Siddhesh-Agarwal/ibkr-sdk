from http import HTTPStatus

import pytest
import responses

from ibkr.client import IBKRClient
from ibkr.exceptions import IBKRAPIError


class TestIBKRClient:
    def test_initialization(self):
        client = IBKRClient()
        assert client.base_url == "https://api.ibkr.com"

    def test_initialization_custom_base_url(self):
        client = IBKRClient(base_url="https://qa.interactivebrokers.com")
        assert client.base_url == "https://qa.interactivebrokers.com"

    @responses.activate
    def test_connect_success(self):
        responses.add(
            responses.POST,
            "https://api.ibkr.com/v1/api/iserver/auth/status",
            json={"status": "connected", "user": {"username": "testuser"}},
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        result = client.connect("testuser", "testpass")
        assert result["status"] == "connected"

    @responses.activate
    def test_connect_password_change_required(self):
        responses.add(
            responses.POST,
            "https://api.ibkr.com/v1/api/iserver/auth/status",
            json={"status": "need_password_change", "message": "Password expired"},
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        with pytest.raises(IBKRAPIError) as exc_info:
            client.connect("testuser", "testpass")
        assert "Password change required" in str(exc_info.value)

    @responses.activate
    def test_disconnect(self):
        responses.add(
            responses.POST,
            "https://api.ibkr.com/v1/api/logout",
            json={"status": "logout"},
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        result = client.disconnect()
        assert result["status"] == "logout"


class TestPortfolioAPI:
    @responses.activate
    def test_accounts(self):
        responses.add(
            responses.GET,
            "https://api.ibkr.com/v1/api/portfolio/accounts",
            json=[
                {
                    "accountId": "DU123456",
                    "accountTitle": "Test Account",
                    "currency": "USD",
                    "type": "CASH",
                },
                {
                    "accountId": "DU789012",
                    "accountTitle": "Second Account",
                    "currency": "EUR",
                    "type": "MARGIN",
                },
            ],
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        accounts = client.portfolio.accounts()
        assert len(accounts) == 2
        assert accounts[0].account_id == "DU123456"
        assert accounts[1].currency == "EUR"

    @responses.activate
    def test_positions(self):
        responses.add(
            responses.GET,
            "https://api.ibkr.com/v1/api/portfolio/DU123456/positions/0",
            json=[
                {"conid": 123456, "ticker": "AAPL", "position": 100.0},
                {"conid": 654321, "ticker": "GOOGL", "position": 50.0},
            ],
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        positions = client.portfolio.positions("DU123456")
        assert len(positions) == 2
        assert positions[0].ticker == "AAPL"

    @responses.activate
    def test_ledger(self):
        responses.add(
            responses.GET,
            "https://api.ibkr.com/v1/api/portfolio/DU123456/ledger",
            json={"cash": {"USD": 10000}, "netLiquidationValue": 50000},
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        ledger = client.portfolio.ledger("DU123456")
        assert ledger["netLiquidationValue"] == 50000

    @responses.activate
    def test_summary(self):
        responses.add(
            responses.GET,
            "https://api.ibkr.com/v1/api/portfolio/DU123456/summary",
            json={"accountType": "CASH", "balance": 100000, "cashBalances": []},
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        summary = client.portfolio.summary("DU123456")
        assert summary.account_type == "CASH"


class TestOrdersAPI:
    @responses.activate
    def test_list_orders(self):
        responses.add(
            responses.GET,
            "https://api.ibkr.com/v1/api/iserver/account/orders",
            json={
                "orders": [
                    {
                        "conid": "123456",
                        "orderId": 12345,
                        "side": "BUY",
                        "status": "Filled",
                        "ticker": "AAPL",
                    }
                ],
                "snapshot": True,
            },
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        orders = client.orders.list_orders()
        assert len(orders.orders) == 1
        assert orders.orders[0].ticker == "AAPL"
        assert orders.snapshot is True

    @responses.activate
    def test_list_orders_with_filters(self):
        responses.add(
            responses.GET,
            "https://api.ibkr.com/v1/api/iserver/account/orders",
            json={"orders": [], "snapshot": False},
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        orders = client.orders.list_orders(filters="STK")
        assert len(orders.orders) == 0

    @responses.activate
    def test_list_orders_force(self):
        responses.add(
            responses.GET,
            "https://api.ibkr.com/v1/api/iserver/account/orders",
            json={"orders": [], "snapshot": True},
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        orders = client.orders.list_orders(force=True)
        assert orders.snapshot is True

    @responses.activate
    def test_get_order(self):
        responses.add(
            responses.GET,
            "https://api.ibkr.com/v1/api/iserver/account/DU123456/order/12345",
            json={"orderId": 12345, "status": "Filled"},
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        order = client.orders.get_order("DU123456", "12345")
        assert order["orderId"] == 12345


class TestMarketDataAPI:
    @responses.activate
    def test_snapshot(self):
        responses.add(
            responses.POST,
            "https://api.ibkr.com/v1/api/iserver/marketdata/snapshot",
            json=[
                {"conid": 123456, "conidEx": "123456--NASDAQ", "server_id": "s1"},
                {"conid": 654321, "conidEx": "654321--NYSE", "server_id": "s2"},
            ],
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        snapshots = client.marketdata.snapshot([123456, 654321])
        assert len(snapshots) == 2
        assert snapshots[0].conid == 123456

    @responses.activate
    def test_snapshot_with_fields(self):
        responses.add(
            responses.POST,
            "https://api.ibkr.com/v1/api/iserver/marketdata/snapshot",
            json=[{"conid": 123456, "field_6509": "155.50"}],
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        snapshots = client.marketdata.snapshot([123456], fields=["31", "32"])
        assert len(snapshots) == 1

    @responses.activate
    def test_history(self):
        responses.add(
            responses.GET,
            "https://api.ibkr.com/v1/api/iserver/marketdata/history",
            json={
                "symbol": "AAPL",
                "data": [
                    {
                        "o": 150.0,
                        "c": 155.0,
                        "h": 156.0,
                        "l": 149.0,
                        "v": 1000000,
                        "t": 1234567890,
                    }
                ],
            },
            status=HTTPStatus.OK,
        )
        client = IBKRClient()
        history = client.marketdata.history(123456, "1 D")
        assert history["symbol"] == "AAPL"
        assert len(history["data"]) == 1


class TestClientErrorHandling:
    @responses.activate
    def test_get_error(self):
        responses.add(
            responses.GET,
            "https://api.ibkr.com/v1/api/portfolio/accounts",
            json={"error": "Not found"},
            status=404,
        )
        client = IBKRClient()
        with pytest.raises(IBKRAPIError) as exc_info:
            client.portfolio.accounts()
        assert exc_info.value.status == HTTPStatus.NOT_FOUND

    @responses.activate
    def test_post_error(self):
        responses.add(
            responses.POST,
            "https://api.ibkr.com/v1/api/iserver/marketdata/snapshot",
            json={"error": "Invalid request"},
            status=400,
        )
        client = IBKRClient()
        with pytest.raises(IBKRAPIError) as exc_info:
            client.marketdata.snapshot([999999])
        assert exc_info.value.status == HTTPStatus.BAD_REQUEST
