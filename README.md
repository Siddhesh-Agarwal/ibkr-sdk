# IBKR SDK

A Python SDK for interacting with [Interactive Brokers Web API](https://ibkrcampus.com/campus/ibkr-api-page/web-api/).

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/ibkr-sdk?period=total&units=INTERNATIONAL_SYSTEM&left_text=downloads)](https://pepy.tech/projects/ibkr-sdk)

## Installation

### From PyPI

```bash
pip install ibkr-sdk
```

## Quick Start

```python
from ibkr import IBKRClient

client = IBKRClient()
client.connect("username", "password")

# List accounts
accounts = client.portfolio.accounts()

# Get positions
positions = client.portfolio.positions("DU123456")

# Get open orders
orders = client.orders.list_orders()
```

## Features

- **Full API Coverage**: All REST endpoints from IBKR API v2.31.0
- **Pydantic Models**: Type-safe request/response parsing with validation
- **Cookie-based Auth**: Session authentication via `/iserver/auth/status`
- **snake_case Fields**: Pythonic attribute names with camelCase alias support

## Architecture

```
ibkr/
├── client.py        # IBKRClient and API classes
├── auth.py          # Session/auth handling
├── exceptions.py    # Custom exceptions
├── types.py         # Enums
└── models/          # Pydantic models
    ├── account.py
    ├── portfolio.py
    ├── orders.py
    ├── marketdata.py
    ├── contract.py
    ├── scanner.py
    ├── fa.py
    └── fyi.py
```

## API Classes

| Class               | Description                              |
| ------------------- | ---------------------------------------- |
| `client.portfolio`  | Account info, positions, ledger, summary |
| `client.orders`     | Open orders, order status                |
| `client.marketdata` | Snapshot, historical data                |
| `client.contract`   | Contract search, info                    |
| `client.scanner`    | Scanner parameters, run                  |
| `client.fa`         | Financial advisor endpoints              |
| `client.fyi`        | Notifications, settings                  |

## Authentication

```python
client = IBKRClient()
client.connect(username, password)

# Keep session alive
client.tickle()

# End session
client.disconnect()
```

## Models

All models accept camelCase JSON (from API) and expose snake_case attributes:

```python
from ibkr.models import AccountAttributes, IndividualPosition

# Works with API JSON
acct = AccountAttributes(**{"accountId": "DU123", "currency": "USD"})
print(acct.account_id)  # "DU123"
```

## Exceptions

| Exception             | Description           |
| --------------------- | --------------------- |
| `IBKRError`           | Base exception        |
| `IBKRAPIError`        | API error response    |
| `IBKRValidationError` | JSON/validation error |
| `IBKRConnectionError` | Network error         |

## Development

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest tests/

# Lint
ruff check
```
