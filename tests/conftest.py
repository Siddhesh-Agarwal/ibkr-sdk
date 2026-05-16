import pytest

from ibkr.client import IBKRClient


@pytest.fixture
def client():
    return IBKRClient()
