from app.portfolio import Portfolio
from app.transaction import Transaction
from datetime import datetime


def test_add_transaction():
    portfolio = Portfolio()
    tx = Transaction("BTC", 1, 10000, datetime.now())

    portfolio.add_transaction(tx)

    assert len(portfolio.transactions) == 1
