import pytest

from app.validators.exceptions import ValidationError
from app.validators.transaction_validator import (
    TransactionValidator
)


def test_invalid_asset():
    with pytest.raises(ValidationError):
        TransactionValidator.validate_asset("DOGE")


def test_negative_amount():
    with pytest.raises(ValidationError):
        TransactionValidator.validate_amount(-10)
