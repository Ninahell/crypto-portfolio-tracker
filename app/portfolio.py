from collections import defaultdict
from typing import List

from app.logger import logger
from app.repositories.transaction_repository import TransactionRepository
from app.transaction import Transaction


class Portfolio:
    def __init__(self):
        self.repository = TransactionRepository()
        self.transactions: List[Transaction] = self.repository.get_all()

    def add_transaction(self, tx: Transaction):
        self.repository.add(tx)
        self.transactions.append(tx)

        logger.info(
            f"Transaction added: {tx.asset} | amount={tx.amount}"
        )

    def get_balance(self):
        balance = defaultdict(float)

        for tx in self.transactions:
            balance[tx.asset] += tx.amount

        return dict(balance)

    def total_value(self):
        return sum(tx.value() for tx in self.transactions)
