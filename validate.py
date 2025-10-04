# validate.py
from typing import List, Dict

def validate_items(items: List[Dict]) -> None:
    """
    Valida cada item: debe tener 'price' >= 0 y 'qty' > 0.
    Lanza ValueError si algo no es válido.
    """
    if not isinstance(items, list):
        raise ValueError("items debe ser una lista")
    if len(items) == 0:
        raise ValueError("No hay items")
    for idx, it in enumerate(items):
        if not isinstance(it, dict):
            raise ValueError(f"Item {idx} no es un dict")
        if 'price' not in it or 'qty' not in it:
            raise ValueError(f"Item {idx} carece de price o qty")
        price = it['price']
        qty = it['qty']
        if price is None or qty is None:
            raise ValueError(f"Item {idx} tiene campos nulos")
        if price < 0:
            raise ValueError(f"Item {idx} tiene price negativo")
        if qty <= 0:
            raise ValueError(f"Item {idx} tiene qty no positiva")
