# AGENTS.md

## Commands

```bash
# Install dependencies
uv sync

# Run all tests
uv run pytest tests/

# Run a single test file / test
uv run pytest tests/test_client.py
uv run pytest tests/test_client.py::TestIBKRClient::test_connect_success

# Lint
uv run ruff check

# Format
uv run ruff format

# Type check
uv run ty check
```

Pre-commit hooks (`.pre-commit-config.yaml`) run `uv sync`, `ty check`, and `ruff check` on every commit — run these manually before committing to catch failures early.

## Architecture

This is a thin Python SDK wrapping the Interactive Brokers Web API (`https://api.ibkr.com`). It has no server/app component — just a client library.

**Layered structure:**
- `ibkr/auth.py` — `AuthHandler` owns the `requests.Session` and handles login/tickle/logout against `/v1/api/iserver/auth/status`, `/v1/api/tickle`, `/v1/api/logout`. Session cookies persist auth state; there is no token to manage manually.
- `ibkr/client.py` — `IBKRClient` is the single entry point. It holds an `AuthHandler` and exposes domain-specific API classes (`PortfolioAPI`, `OrdersAPI`, `MarketDataAPI`, `ContractAPI`, `ScannerAPI`, `FAAPI`, `FYIAPI`) as **lazily-instantiated properties** (e.g. `client.portfolio`), each holding a back-reference to the client. All HTTP calls funnel through `IBKRClient._get` / `_post`, which raise `IBKRAPIError` on any non-200 response — API classes never touch `requests` directly.
- `ibkr/models/` — one file per API domain (`account.py`, `portfolio.py`, `orders.py`, `marketdata.py`, `contract.py`, `scanner.py`, `fa.py`, `fyi.py`, `ledger.py`). Every model is a Pydantic `BaseModel` with `model_config = {"populate_by_name": True}` and fields declared as `snake_case_name: type = Field(alias="camelCaseName")` — this is the core convention for the whole SDK: raw IBKR JSON is camelCase, the Python-facing API is snake_case via aliasing.
- `ibkr/exceptions.py` — a flat exception hierarchy rooted at `IBKRError`: `IBKRAPIError` (non-2xx response, carries `status`/`error`/`message`), `IBKRValidationError` (JSON/pydantic parse failure), `IBKRConnectionError` (network failure).
- `ibkr/types.py` — shared enums used across models.

**Adding a new endpoint:** add/extend a Pydantic model in `ibkr/models/<domain>.py` following the alias convention above, then add a method to the corresponding `*API` class in `client.py` that calls `self.client._get(...)` or `self.client._post(...)` and parses the response with `Model.model_validate_json(data)` (single object) or `TypeAdapter(list[Model]).validate_json(data)` (list responses).

**Testing:** tests use the `responses` library to mock HTTP calls against `https://api.ibkr.com` (see `tests/test_client.py`) rather than hitting the real IBKR API.

`swagger.json` at the repo root is the upstream IBKR Web API spec (v2.31.0) — consult it when implementing new endpoints to confirm exact paths/payloads.
