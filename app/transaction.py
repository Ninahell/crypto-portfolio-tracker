from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    asset: str
    amount: float
    price: float
    timestamp: datetime

    def value(self) -> float:
        return self.amount * self.price
