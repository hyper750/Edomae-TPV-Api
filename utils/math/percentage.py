def calculate_discount(price: float, discount: float) -> float:
    if discount is None:
        discount = 0
    return price * (1 - (discount / 100))


def calculate_percentage(price: float, percentage: float) -> float:
    if percentage is None:
        percentage = 0
    return price * percentage / 100


def calculate_amount(price: float, percentage: float) -> float:
    if percentage is None:
        percentage = 0
    return price * (1 + (percentage / 100))
