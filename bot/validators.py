def validate_order_input(symbol, side, order_type, quantity, price=None):
    """
    Validates user input before placing an order.
    Returns (True, None) if valid
    Returns (False, error_message) if invalid
    """

    # Symbol validation
    if not symbol or not isinstance(symbol, str):
        return False, "Symbol must be a non-empty string"

    # Side validation
    side = side.upper()
    if side not in ("BUY", "SELL"):
        return False, "Side must be BUY or SELL"

    # Order type validation
    order_type = order_type.upper()
    if order_type not in ("MARKET", "LIMIT"):
        return False, "Order type must be MARKET or LIMIT"

    # Quantity validation
    try:
        quantity = float(quantity)
        if quantity <= 0:
            return False, "Quantity must be greater than 0"
    except ValueError:
        return False, "Quantity must be a number"

    # Price validation (only for LIMIT orders)
    if order_type == "LIMIT":
        if price is None:
            return False, "Price is required for LIMIT orders"
        try:
            price = float(price)
            if price <= 0:
                return False, "Price must be greater than 0"
        except ValueError:
            return False, "Price must be a number"

    return True, None
