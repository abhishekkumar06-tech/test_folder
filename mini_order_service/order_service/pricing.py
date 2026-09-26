def calculate_subtotal(items):
    subtotal = 0.0
    for item in items:
        subtotal += item["price"]
    return round(subtotal, 2)


def calculate_discount(subtotal, discount_percent):
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    discount_amount = subtotal * (discount_percent / 100)
    return round(subtotal - discount_amount, 2)
