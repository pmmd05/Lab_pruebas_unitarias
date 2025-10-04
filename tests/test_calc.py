# Pruebas unitarias:
# pytest tests/test_calc.py -s
import pytest
from calc import calculate_total

def test_calculate_total_basic(sample_items):
    total = calculate_total(sample_items, tax_rate=0.10, discount=0.0)
    # subtotal = 10*2 + 5.5*1 = 25.5 ; total = 25.5 * 1.10 = 28.05
    assert total == pytest.approx(28.05, rel=1e-9)
    print(f"\nTotal calculado: {total}")

def test_calculate_with_discount(sample_items):
    total = calculate_total(sample_items, tax_rate=0.12, discount=5.5)
    # subtotal 25.5 - 5.5 = 20.0 -> total = 20 * 1.12 = 22.4
    assert total == pytest.approx(22.4)
    print(f"Total con descuento: {total}")

def test_calculate_zero_items():
    total = calculate_total([], tax_rate=0.12)
    assert total == pytest.approx(0.0)
    print(f"Total con lista vacía: {total}")
