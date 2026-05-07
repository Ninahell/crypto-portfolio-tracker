from datetime import datetime

from app.database.db import Database
from app.transaction import Transaction


class TransactionRepository:
    def __init__(self):
        self.db = Database()

    def add(self, transaction: Transaction):
        self.db.execute("""
            INSERT INTO transactions (
                asset,
                amount,
                price,
                timestamp
            )
            VALUES (?, ?, ?, ?)
        """, (
            transaction.asset,
            transaction.amount,
            transaction.price,
            transaction.timestamp.isoformat()
        ))

    def get_all(self):
        rows = self.db.fetchall("""
            SELECT asset, amount, price, timestamp
            FROM transactions
        """)

        return [
            Transaction(
                asset=row[0],
                amount=row[1],
                price=row[2],
                timestamp=datetime.fromisoformat(row[3])
            )
            for row in rows
        ]
