# IBKR SDK Design Specification

## Overview

Python SDK for Interactive Brokers REST API using Pydantic for request/response parsing and requests for HTTP.

## Architecture

```
ibkr/
├── __init__.py          # Public API exports
├── client.py            # IBKRClient main class
├── auth.py             # Session/auth handling
├── exceptions.py       # Custom exceptions
├── models/
│   ├── __init__.py
│   ├── account.py      # Account-related schemas
│   ├── portfolio.py    # Portfolio/position schemas
│   ├── orders.py       # Order schemas
│   ├── marketdata.py   # Market data schemas
│   ├── contract.py     # Contract/search schemas
│   ├── scanner.py      # Scanner schemas
│   ├── fa.py           # Financial advisor schemas
│   └── fyi.py          # FYI notifications schemas
└── types.py            # Shared types (enums, constants)
```

## Components

### IBKRClient

Main entry point. Wraps `requests.Session` with cookie-based auth.

```python
client = IBKRClient()
client.connect(username, password)
accounts = client.portfolio.accounts
positions = client.portfolio.positions("accountId")
```

### Auth Flow

1. POST to `/iserver/auth/status` with credentials
2. Server returns session cookie
3. All subsequent requests include cookie automatically via `requests.Session`
4. `/tickle` endpoint refreshes/validates session

### Model Organization

Each swagger schema becomes a Pydantic model:
- `accountSummaryResponse` → `ibkr.models.account.AccountSummaryResponse`
- `individualPosition` → `ibkr.models.portfolio.IndividualPosition`
- `liveOrdersResponse` → `ibkr.models.orders.LiveOrdersResponse`

### Error Handling

- API errors return `IBKRAPIError` with status, error message
- JSON parse/validation errors raise `IBKRValidationError`
- Network errors raise `IBKRConnectionError`

## Implementation Priorities

1. **Core models** (account, portfolio, orders, marketdata) — ~50 key schemas
2. **Auth flow** — cookie/session handling
3. **All other endpoints** — remaining schemas
4. **Utilities** — paginated responses, streaming

## API Endpoints by Category

### Trading Orders
- `GET /iserver/account/orders` — List open orders
- `GET /iserver/account/{accountId}/order/{orderId}` — Order details
- `POST /iserver/account/{accountId}/order/{orderId}` — Place order
- `DELETE /iserver/account/{accountId}/order/{orderId}` — Cancel order

### Portfolio
- `GET /portfolio/accounts` — List all accounts
- `GET /portfolio/{accountId}/positions/{pageId}` — Positions
- `GET /portfolio/{accountId}/ledger` — Ledger entries
- `GET /portfolio/{accountId}/summary` — Portfolio summary

### Market Data
- `GET /iserver/marketdata/snapshot` — Real-time snapshot
- `GET /iserver/marketdata/history` — Historical data
- `POST /iserver/marketdata/unsubscribe` — Unsubscribe

### Account
- `GET /iserver/account/{accountId}/summary` — Account summary
- `GET /gw/api/v1/balances/query` — Balance query
- `GET /gw/api/v1/statements` — Statements

### Contract Search
- `POST /iserver/secdef/search` — Search contracts
- `GET /iserver/secdef/info` — Contract info
- `GET /iserver/contract/{conid}/info` — Contract details

### Scanner
- `GET /iserver/scanner/params` — Scanner parameters
- `POST /iserver/scanner/run` — Run scanner

### Financial Advisor
- `GET /fa/model/accounts-details` — FA account details
- `GET /fa/model/positions` — FA positions
- `POST /fa/model/invest-divest` — Invest/divest

### FYI Notifications
- `GET /fyi/notifications` — List notifications
- `GET /fyi/settings` — FYI settings
- `POST /fyi/deliveryoptions` — Delivery options

## Testing Strategy

- Unit tests for Pydantic model validation with example JSON from swagger
- Integration tests against sandbox/demo environment (if available)
- Mock responses for CI/CD

## Dependencies

- `pydantic >= 2.13.4` — Data validation
- `requests >= 2.34.2` — HTTP client