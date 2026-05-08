from datetime import datetime

from app.cli import create_parser
from app.database.schema import initialize_database
from app.services.portfolio_service import PortfolioService
from app.transaction import Transaction


def main():
    parser = create_parser()
    args = parser.parse_args()

    initialize_database()

    service = PortfolioService()

    if args.command == "add":
        transaction = Transaction(
            asset=args.asset,
            amount=args.amount,
            price=args.price,
            timestamp=datetime.now()
        )

        service.add_transaction(transaction)

        print("Transaction added")

    elif args.command == "balance":
        print(service.calculate_balance())

    elif args.command == "value":
        print(service.calculate_total_value())

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
