# action.py
from typing import List, Dict, Any
import itertools
from validate import validate_items
from calc import calculate_total

_order_id_counter = itertools.count(1)

def place_order(items: List[Dict], tax_rate: float = 0.12, discount: float = 0.0, storage: List[Dict] = None) -> Dict[str, Any]:
    validate_items(items)
    total = calculate_total(items, tax_rate=tax_rate, discount=discount)
    order = {
        "id": next(_order_id_counter),
        "items": items,
        "tax_rate": tax_rate,
        "discount": discount,
        "total": total,
        "status": "placed"
    }
    if storage is not None:
        storage.append(order)
    return order
