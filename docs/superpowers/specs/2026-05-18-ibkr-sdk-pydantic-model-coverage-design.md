# IBKR SDK: Pydantic Model Coverage for Dict-Returning Endpoints

## Status
Approved

## Overview

Refactor all SDK endpoints currently returning raw `dict` to return properly-typed Pydantic models. Add any missing models for the 8 affected endpoints, and update client methods to use `model_validate_json` for single objects and `TypeAdapter(list[Model]).validate_json` for lists.

## Background

The SDK currently has 8 API endpoints that return `dict` instead of Pydantic models. These should return typed models for better developer experience, IDE autocomplete, and type safety.

## Changes by API

| API Class | Method | Current Return | New Return | Model Needed |
|-----------|--------|----------------|------------|--------------|
| PortfolioAPI | ledger() | dict | LedgerResponse | Yes (new) |
| OrdersAPI | get_order() | dict | OrderDetail | Yes (new) |
| MarketDataAPI | history() | dict | Union[IserverHistoryBidAskResponse, IserverHistoryLastResponse, IserverHistoryMidpointResponse] | Exists |
| ContractAPI | info() | dict | ContractInfo | Exists |
| FAAPI | account_details() | dict | FAModelAccountsDetails | Yes (new) |
| FAAPI | positions() | dict | ModelPositionResponse | Yes (new) |
| FYIAPI | notifications() | dict | NotificationItem | Yes (new) |
| FYIAPI | settings() | dict | FyiSettingsResponse | Yes (new) |

## New Model Files

### ibkr/models/ledger.py (new)
Create `LedgerResponse` model to wrap the ledger dictionary response. The ledger endpoint returns a `dict` keyed by currency code, each value containing account balance information.

```python
class LedgerEntry(BaseModel):
    model_config = {"populate_by_name": True}
    acctcode: str = Field(alias="acctcode")
    cashbalance: float | None = Field(default=None, alias="cashbalance")
    # ... other fields

class LedgerResponse(BaseModel):
    model_config = {"populate_by_name": True}
    # Response wraps multiple currency entries
```

### ibkr/models/order.py (extend existing)
Add `OrderDetail` model for the `get_order()` endpoint.

### ibkr/models/fa.py (extend existing)
Add `FAModelAccountsDetails` and `ModelPositionResponse` models.

### ibkr/models/fyi.py (extend existing)
Add `NotificationItem` and `FyiSettingsResponse` models.

## Validation Pattern

Update client methods to use:

```python
# Single object response
from pydantic import BaseModel
return SomeModel.model_validate_json(response.text)

# List response  
from pydantic import TypeAdapter
return TypeAdapter(list[SomeModel]).validate_json(response.text)
```

## Implementation Notes

1. Use `model_validate_json` on the response text for single objects
2. Use `TypeAdapter(list[Model]).validate_json(response.text)` for lists
3. All models use `Field(alias="camelCaseName")` with `model_config = {"populate_by_name": True}`
4. Keep snake_case for Python attributes per convention

## Tasks

1. Create `ibkr/models/ledger.py` with `LedgerResponse` and `LedgerEntry` models
2. Extend `ibkr/models/orders.py` with `OrderDetail` model
3. Extend `ibkr/models/fa.py` with `FAModelAccountsDetails` and `ModelPositionResponse` models
4. Extend `ibkr/models/fyi.py` with `NotificationItem` and `FyiSettingsResponse` models
5. Update `PortfolioAPI.ledger()` to return `LedgerResponse`
6. Update `OrdersAPI.get_order()` to return `OrderDetail`
7. Update `MarketDataAPI.history()` to use union type with existing models
8. Update `ContractAPI.info()` to return `ContractInfo`
9. Update `FAAPI.account_details()` to return `FAModelAccountsDetails`
10. Update `FAAPI.positions()` to return `ModelPositionResponse`
11. Update `FYIAPI.notifications()` to return list of `NotificationItem`
12. Update `FYIAPI.settings()` to return `FyiSettingsResponse`
13. Update `ibkr/models/__init__.py` exports
14. Run tests with `uv run pytest tests/`
15. Run lint with `ruff check .`