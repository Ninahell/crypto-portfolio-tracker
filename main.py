from datetime import datetime
from app.portfolio import Portfolio
from app.transaction import Transaction


def main():
    portfolio = Portfolio()

    while True:
        print("\n--- CRYPTO PORTFOLIO ---")
        print("1. Add transaction")
        print("2. Show balance")
        print("3. Show total value")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            asset = input("Asset (BTC/ETH): ")
            amount = float(input("Amount: "))
            price = float(input("Price: "))

            tx = Transaction(asset, amount, price, datetime.now())
            portfolio.add_transaction(tx)

            print("Transaction added!")

        elif choice == "2":
            print(portfolio.get_balance())

        elif choice == "3":
            print(portfolio.total_value())

        elif choice == "4":
            break


if __name__ == "__main__":
    main()
