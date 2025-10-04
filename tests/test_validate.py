# tests/test_validate.py
import pytest
from validate import validate_items

def test_validate_good(sample_items):
    # no lanza excepción
    validate_items(sample_items)

def test_validate_empty():
    with pytest.raises(ValueError, match="No hay items"):
        validate_items([])

def test_validate_negative_price():
    bad = [{"price": -1.0, "qty": 1}]
    with pytest.raises(ValueError, match="price negativo"):
        validate_items(bad)

def test_validate_zero_qty():
    bad = [{"price": 5.0, "qty": 0}]
    with pytest.raises(ValueError, match="qty no positiva"):
        validate_items(bad)
