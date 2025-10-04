# calc.py
from typing import List, Dict

def calculate_total(items: List[Dict], tax_rate: float = 0.12, discount: float = 0.0) -> float:
    """
    items: lista de dicts con {'price': float, 'qty': int}
    tax_rate: porcentaje (0.12 -> 12%)
    discount: valor absoluto a restar del subtotal (no porcentaje)
    """
    subtotal = 0.0
    for it in items:
        price = float(it.get('price', 0))
        qty = int(it.get('qty', 0))
        subtotal += price * qty
    subtotal_after_discount = max(0.0, subtotal - float(discount))
    total = subtotal_after_discount * (1 + float(tax_rate))
    return total
