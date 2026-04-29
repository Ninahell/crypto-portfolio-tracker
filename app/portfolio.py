from collections import defaultdict
from typing import List
from app.transaction import Transaction
from app.storage import Storage


class Portfolio:
    def __init__(self):
        self.storage = Storage()
        self.transactions: List[Transaction] = self.storage.load()

    def add_transaction(self, tx: Transaction):
        self.transactions.append(tx)
        self.storage.save(self.transactions)

    def get_balance(self):
        balance = defaultdict(float)
        for tx in self.transactions:
            balance[tx.asset] += tx.amount
        return dict(balance)

    def total_value(self):
        return sum(tx.value() for tx in self.transactions)
