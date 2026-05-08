from dataclasses import dataclass
from typing import List

from app.transaction import Transaction


@dataclass
class Portfolio:
    transactions: List[Transaction]
