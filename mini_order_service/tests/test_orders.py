import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from order_service.orders import calculate_order_total, create_order


def test_create_order():
    items = [
        {"name": "Book", "price": 40.0, "quantity": 1},
        {"name": "Marker", "price": 60.0, "quantity": 1},
    ]
    order = create_order(items, discount_percent=10)
    assert order["items"] == items
    assert order["subtotal"] == 100.0
    assert order["discount_percent"] == 10
    assert order["total"] == 90.0


def test_calculate_order_total():
    order = {
        "items": [{"name": "Book", "price": 50.0, "quantity": 1}],
        "subtotal": 50.0,
        "discount_percent": 0,
        "total": 50.0,
    }
    assert calculate_order_total(order) == 50.0
