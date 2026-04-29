import json
from app.transaction import Transaction
from datetime import datetime


class Storage:
    def __init__(self, filename="portfolio.json"):
        self.filename = filename

    def save(self, transactions):
        data = [
            {
                "asset": tx.asset,
                "amount": tx.amount,
                "price": tx.price,
                "timestamp": tx.timestamp.isoformat()
            }
            for tx in transactions
        ]

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)

            return [
                Transaction(
                    asset=item["asset"],
                    amount=item["amount"],
                    price=item["price"],
                    timestamp=datetime.fromisoformat(item["timestamp"])
                )
                for item in data
            ]
        except FileNotFoundError:
            return []
