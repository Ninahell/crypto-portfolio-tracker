from collections import defaultdict
from typing import List
from app.transaction import Transaction


class Portfolio:
    def __init__(self):
        self.transactions: List[Transaction] = []

    def add_transaction(self, tx: Transaction):
        self.transactions.append(tx)

    def get_balance(self):
        balance = defaultdict(float)
        for tx in self.transactions:
            balance[tx.asset] += tx.amount
        return dict(balance)

    def total_value(self):
        return sum(tx.value() for tx in self.transactions)
