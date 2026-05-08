from datetime import datetime

from app.cli import create_parser
from app.database.schema import initialize_database
from app.services.portfolio_service import PortfolioService
from app.transaction import Transaction
from app.utils import export_transactions_to_csv
from app.validators.exceptions import ValidationError

def main():
    parser = create_parser()
    args = parser.parse_args()

    initialize_database()

    service = PortfolioService()

   if args.command == "add":
    try:
        transaction = Transaction(
            asset=args.asset,
            amount=args.amount,
            price=args.price,
            timestamp=datetime.now()
        )

        service.add_transaction(transaction)

        print("Transaction added")

    except ValidationError as error:
        print(f"Validation error: {error}")

        service.add_transaction(transaction)

        print("Transaction added")

    elif args.command == "balance":
        print(service.calculate_balance())

    elif args.command == "value":
        print(service.calculate_total_value())
elif args.command == "export":
    transactions = service.get_transactions()

    export_transactions_to_csv(transactions)

    print("CSV report exported")

elif args.command == "filter":
    transactions = service.get_transactions()

    if args.asset:
        transactions = (
            service.filter_transactions_by_asset(
                args.asset.upper()
            )
        )

    elif args.min_price:
        transactions = (
            service.filter_transactions_by_min_price(
                args.min_price
            )
        )

    elif args.min_amount:
        transactions = (
            service.filter_transactions_by_min_amount(
                args.min_amount
            )
        )

    for transaction in transactions:
        print(transaction)

else:
        parser.print_help()


if __name__ == "__main__":
    main()
