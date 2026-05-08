from collections import defaultdict

from app.logger import logger
from app.repositories.transaction_repository import TransactionRepository
from app.transaction import Transaction
from app.validators.transaction_validator import TransactionValidator
from app.validators.helpers import normalize_asset_name

class PortfolioService:
    def __init__(self):
        self.repository = TransactionRepository()

    def add_transaction(self, transaction: Transaction):
transaction.asset = normalize_asset_name(
    transaction.asset
)

TransactionValidator.validate_amount(
    transaction.amount
)

TransactionValidator.validate_price(
    transaction.price
)
        self.repository.add(transaction)

        logger.info(
            f"Added transaction: {transaction.asset}"
        )

    def get_transactions(self):
        return self.repository.get_all()

    def calculate_balance(self):
        balance = defaultdict(float)

        for tx in self.get_transactions():
            balance[tx.asset] += tx.amount

        return dict(balance)

    def calculate_total_value(self):
        return sum(
            tx.value()
            for tx in self.get_transactions()
        )
