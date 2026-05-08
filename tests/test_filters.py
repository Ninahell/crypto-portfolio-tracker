from datetime import datetime

from app.filters.transaction_filters import (
    TransactionFilters
)
from app.transaction import Transaction


def test_filter_by_asset():
    transactions = [
        Transaction(
            "BTC",
            1,
            50000,
            datetime.now()
        ),
        Transaction(
            "ETH",
            2,
            2000,
            datetime.now()
        )
    ]

    filtered = (
        TransactionFilters.filter_by_asset(
            transactions,
            "BTC"
        )
    )

    assert len(filtered) == 1


def test_filter_by_min_price():
    transactions = [
        Transaction(
            "BTC",
            1,
            50000,
            datetime.now()
        ),
        Transaction(
            "ETH",
            2,
            2000,
            datetime.now()
        )
    ]

    filtered = (
        TransactionFilters.filter_by_min_price(
            transactions,
            10000
        )
    )

    assert len(filtered) == 1
