from app.portfolio import Portfolio
from app.transaction import Transaction
from datetime import datetime


def test_balance_calculation():
    portfolio = Portfolio()
    portfolio.transactions = []

    portfolio.add_transaction(Transaction("BTC", 1, 10000, datetime.now()))
    portfolio.add_transaction(Transaction("BTC", 2, 20000, datetime.now()))

    balance = portfolio.get_balance()

    assert balance["BTC"] == 3
