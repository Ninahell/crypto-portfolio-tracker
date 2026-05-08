import csv


def export_transactions_to_csv(transactions, filename="report.csv"):
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
