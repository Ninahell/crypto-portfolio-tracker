from datetime import datetime
from app.portfolio import Portfolio
from app.transaction import Transaction


def main():
    portfolio = Portfolio()

    tx1 = Transaction("BTC", 0.1, 30000, datetime.now())
    tx2 = Transaction("ETH", 1.5, 2000, datetime.now())

    portfolio.add_transaction(tx1)
    portfolio.add_transaction(tx2)

    print("Balance:", portfolio.get_balance())
    print("Total value:", portfolio.total_value())


if __name__ == "__main__":
    main()
