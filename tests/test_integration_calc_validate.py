# tests/test_integration_calc_validate.py
import pytest
from validate import validate_items
from calc import calculate_total

def test_integration_validate_then_calc(sample_items):
    # primer paso: validar
    validate_items(sample_items)
    # segundo paso: calcular
    total = calculate_total(sample_items, tax_rate=0.15, discount=0)
    # comprobamos valor esperado
    assert total == pytest.approx((10*2 + 5.5)*1.15)

def test_integration_invalid_raises_before_calc():
    bad = [{"price": -10, "qty": 1}]
    with pytest.raises(ValueError):
        validate_items(bad)
    # no intentamos calcular si valida falla (este test refleja el flujo correcto)
