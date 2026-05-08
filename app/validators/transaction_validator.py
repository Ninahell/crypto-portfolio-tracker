from app.config import SUPPORTED_ASSETS
from app.validators.exceptions import ValidationError


class TransactionValidator:
    @staticmethod
    def validate_asset(asset: str):
        if asset not in SUPPORTED_ASSETS:
            raise ValidationError(
                f"Unsupported asset: {asset}"
            )

    @staticmethod
    def validate_amount(amount: float):
        if amount <= 0:
            raise ValidationError(
                "Amount must be greater than zero"
            )

    @staticmethod
    def validate_price(price: float):
        if price <= 0:
            raise ValidationError(
                "Price must be greater than zero"
            )
