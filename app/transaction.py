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

    def __repr__(self) -> str:
        return (
            f"Transaction("
            f"asset='{self.asset}', "
            f"amount={self.amount}, "
            f"price={self.price}, "
            f"timestamp='{self.timestamp}'"
            f")"
        )
