from typing import List

from app.transaction import Transaction


class TransactionFilters:
    @staticmethod
    def filter_by_asset(
        transactions: List[Transaction],
        asset: str
    ):
        return [
            tx for tx in transactions
            if tx.asset == asset
        ]

    @staticmethod
    def filter_by_min_price(
        transactions: List[Transaction],
        min_price: float
    ):
        return [
            tx for tx in transactions
            if tx.price >= min_price
        ]

    @staticmethod
    def filter_by_min_amount(
        transactions: List[Transaction],
        min_amount: float
    ):
        return [
            tx for tx in transactions
            if tx.amount >= min_amount
        ]
