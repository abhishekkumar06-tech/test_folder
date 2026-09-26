from order_service.pricing import calculate_discount, calculate_subtotal


def create_order(items, discount_percent=0):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal, discount_percent)
    total = subtotal - discount
    return {
        "items": items,
        "subtotal": subtotal,
        "discount_percent": discount_percent,
        "total": total,
    }


def calculate_order_total(order):
    return order["total"]
