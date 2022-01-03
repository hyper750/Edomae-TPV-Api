def calculate_discount(price: float, discount: float) -> float:
    if discount is None:
        discount = 0
    return price * (1 - (discount / 100))
