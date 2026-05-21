import json
from http import HTTPStatus

from pydantic import TypeAdapter

from ibkr.auth import AuthHandler
from ibkr.exceptions import IBKRAPIError
from ibkr.models.account import AccountAttributes, AccountSummaryResponse
from ibkr.models.contract import ContractInfo
from ibkr.models.fa import FAModelAccountsDetails, ModelPositionResponse
from ibkr.models.fyi import FyiSettingsItem, NotificationItem
from ibkr.models.ledger import LedgerResponse
from ibkr.models.marketdata import IserverSnapshot
from ibkr.models.orders import LiveOrdersResponse, OrderDetail
from ibkr.models.portfolio import IndividualPosition
from ibkr.models.scanner import IserverScannerParams, IserverScannerRunResponse


class PortfolioAPI:
    def __init__(self, client: "IBKRClient"):
        self.client = client

    def accounts(self) -> list[AccountAttributes]:
        data = self.client._get("/v1/api/portfolio/accounts")
        # return [AccountAttributes(**a) for a in data]
        return TypeAdapter(list[AccountAttributes]).validate_json(data)

    def positions(self, account_id: str, page_id: int = 0) -> list[IndividualPosition]:
        data = self.client._get(f"/v1/api/portfolio/{account_id}/positions/{page_id}")
        return TypeAdapter(list[IndividualPosition]).validate_json(data)

    def ledger(self, account_id: str) -> LedgerResponse:
        data = self.client._get(f"/v1/api/portfolio/{account_id}/ledger")
        return LedgerResponse.model_validate_json(data)

    def summary(self, account_id: str) -> AccountSummaryResponse:
        data = self.client._get(f"/v1/api/portfolio/{account_id}/summary")
        return AccountSummaryResponse.model_validate_json(data)


class OrdersAPI:
    def __init__(self, client: "IBKRClient"):
        self.client = client

    def list_orders(
        self, filters: str | None = None, force: bool = False
    ) -> LiveOrdersResponse:
        params = {}
        if filters:
            params["filters"] = filters
        if force:
            params["force"] = "true"
        data = self.client._get("/v1/api/iserver/account/orders", params=params)
        return LiveOrdersResponse.model_validate_json(data)

    def get_order(self, account_id: str, order_id: str) -> OrderDetail:
        data = self.client._get(
            f"/v1/api/iserver/account/{account_id}/order/{order_id}"
        )
        return OrderDetail.model_validate_json(data)


class MarketDataAPI:
    def __init__(self, client: "IBKRClient"):
        self.client = client

    def snapshot(
        self, conids: list[int], fields: list[str] | None = None
    ) -> list[IserverSnapshot]:
        payload: dict[str, list[int] | list[str]] = {"conids": conids}
        if fields:
            payload["fields"] = fields
        data = self.client._post("/v1/api/iserver/marketdata/snapshot", json=payload)
        return TypeAdapter(list[IserverSnapshot]).validate_json(data)

    def history(
        self, conid: int, period: str, bar: str = "1 min", outside_rth: bool = False
    ) -> dict:
        params = {
            "conid": conid,
            "period": period,
            "bar": bar,
            "outsideRegularTradingHours": outside_rth,
        }
        return json.loads(
            self.client._get("/v1/api/iserver/marketdata/history", params=params)
        )


class ContractAPI:
    def __init__(self, client: "IBKRClient"):
        self.client = client

    def search(self, symbol: str, sec_type: str = "STK") -> list[ContractInfo]:
        payload = {"symbol": symbol, "secType": sec_type}
        data = self.client._post("/v1/api/iserver/secdef/search", json=payload)
        json_data = json.loads(data)
        return TypeAdapter(list[ContractInfo]).validate_json(
            json_data.get("contracts", [])
        )

    def info(self, conid: int) -> ContractInfo:
        data = self.client._get(f"/v1/api/iserver/contract/{conid}/info")
        return ContractInfo.model_validate_json(data)


class ScannerAPI:
    def __init__(self, client: "IBKRClient"):
        self.client = client

    def params(self) -> IserverScannerParams:
        data = self.client._get("/v1/api/iserver/scanner/params")
        return IserverScannerParams.model_validate_json(data)

    def run(self, scanner_request: dict) -> list[IserverScannerRunResponse]:
        data = self.client._post("/v1/api/iserver/scanner/run", json=scanner_request)
        return TypeAdapter(list[IserverScannerRunResponse]).validate_json(data)


class FAAPI:
    def __init__(self, client: "IBKRClient"):
        self.client = client

    def account_details(self) -> FAModelAccountsDetails:
        data = self.client._get("/v1/api/fa/model/accounts-details")
        return FAModelAccountsDetails.model_validate_json(data)

    def positions(self, model: str) -> ModelPositionResponse:
        data = self.client._get("/v1/api/fa/model/positions", params={"model": model})
        return ModelPositionResponse.model_validate_json(data)


class FYIAPI:
    def __init__(self, client: "IBKRClient"):
        self.client = client

    def notifications(self) -> list[NotificationItem]:
        data = self.client._get("/v1/api/fyi/notifications")
        return TypeAdapter(list[NotificationItem]).validate_json(data)

    def settings(self) -> list[FyiSettingsItem]:
        data = self.client._get("/v1/api/fyi/settings")
        return TypeAdapter(list[FyiSettingsItem]).validate_json(data)


class IBKRClient:
    def __init__(self, base_url: str = "https://api.ibkr.com"):
        self.base_url = base_url
        self.auth = AuthHandler(base_url)
        self._portfolio: PortfolioAPI | None = None
        self._orders: OrdersAPI | None = None
        self._marketdata: MarketDataAPI | None = None
        self._contract: ContractAPI | None = None
        self._scanner: ScannerAPI | None = None
        self._fa: FAAPI | None = None
        self._fyi: FYIAPI | None = None

    def connect(self, username: str, password: str) -> dict:
        return self.auth.login(username, password)

    def tickle(self) -> dict:
        return self.auth.tickle()

    def disconnect(self) -> dict:
        return self.auth.logout()

    @property
    def portfolio(self) -> PortfolioAPI:
        if self._portfolio is None:
            self._portfolio = PortfolioAPI(self)
        return self._portfolio

    @property
    def orders(self) -> OrdersAPI:
        if self._orders is None:
            self._orders = OrdersAPI(self)
        return self._orders

    @property
    def marketdata(self) -> MarketDataAPI:
        if self._marketdata is None:
            self._marketdata = MarketDataAPI(self)
        return self._marketdata

    @property
    def contract(self) -> ContractAPI:
        if self._contract is None:
            self._contract = ContractAPI(self)
        return self._contract

    @property
    def scanner(self) -> ScannerAPI:
        if self._scanner is None:
            self._scanner = ScannerAPI(self)
        return self._scanner

    @property
    def fa(self) -> FAAPI:
        if self._fa is None:
            self._fa = FAAPI(self)
        return self._fa

    @property
    def fyi(self) -> FYIAPI:
        if self._fyi is None:
            self._fyi = FYIAPI(self)
        return self._fyi

    def _get(self, path: str, params: dict | None = None) -> str:
        response = self.auth.session.get(f"{self.base_url}{path}", params=params)
        if response.status_code == HTTPStatus.OK:
            return response.text
        raise IBKRAPIError(response.status_code, "GET failed", response.text)

    def _post(self, path: str, json: dict | None = None) -> str:
        response = self.auth.session.post(f"{self.base_url}{path}", json=json)
        if response.status_code == HTTPStatus.OK:
            return response.text
        raise IBKRAPIError(response.status_code, "POST failed", response.text)
