from datetime import datetime

from app.cli import create_parser
from app.portfolio import Portfolio
from app.transaction import Transaction


def main():
    parser = create_parser()
    args = parser.parse_args()

    portfolio = Portfolio()

    if args.command == "add":
        tx = Transaction(
            asset=args.asset,
            amount=args.amount,
            price=args.price,
            timestamp=datetime.now()
        )

        portfolio.add_transaction(tx)
        print("Transaction added")

    elif args.command == "balance":
        print(portfolio.get_balance())

    elif args.command == "value":
        print(portfolio.total_value())

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
