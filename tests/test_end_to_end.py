# Prueba de flujo completo:
# pytests tests/test_end_to_end.py -s
from action import place_order
import pytest

def test_place_order_appends_to_storage(sample_items, storage):
    order = place_order(sample_items, tax_rate=0.10, discount=0.0, storage=storage)
    assert order["status"] == "placed"
    assert "total" in order
    assert len(storage) == 1
    assert storage[0]["id"] == order["id"]
    print(f"\nOrden almacenada: {storage[0]}")

def test_place_order_invalid_items_raises(sample_items):
    bad = [{"price": -2, "qty": 1}]
    with pytest.raises(ValueError):
        place_order(bad)
        print("Error capturado como se esperaba al intentar colocar orden con items inválidos")
    
