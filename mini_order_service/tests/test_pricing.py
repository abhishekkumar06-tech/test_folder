import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from order_service.pricing import calculate_discount, calculate_subtotal


def test_subtotal_multiple_items():
    items = [
        {"name": "Notebook", "price": 10.0, "quantity": 1},
        {"name": "Pen", "price": 2.5, "quantity": 1},
    ]
    assert calculate_subtotal(items) == 12.5


def test_subtotal_with_quantity():
    items = [
        {"name": "Notebook", "price": 10.0, "quantity": 3},
    ]
    assert calculate_subtotal(items) == 30.0


def test_no_discount():
    assert calculate_discount(100.0, 0) == 100.0


def test_ten_percent_discount():
    assert calculate_discount(100.0, 10) == 90.0
