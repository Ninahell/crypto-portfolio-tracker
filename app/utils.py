import csv


from typing import List

from app.transaction import Transaction


def export_transactions_to_csv(
    transactions: List[Transaction],
    filename: str = "report.csv"
):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Asset",
            "Amount",
            "Price",
            "Timestamp"
        ])

        for tx in transactions:
            writer.writerow([
                tx.asset,
                tx.amount,
                tx.price,
                tx.timestamp
            ])
