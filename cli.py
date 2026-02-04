import argparse
from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.validators import validate_order_input
from bot.logging_config import setup_logger

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(
        description="Simple Binance Futures Trading Bot (Testnet)"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, help="Order side: BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    # Step 1: Validate input
    is_valid, error = validate_order_input(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    if not is_valid:
        # print(f"❌ Validation Error: {error}")
        logger.error(f"Validation failed: {error}")
        return

    # Step 2: Initialize client and services
    try:
        client = BinanceFuturesClient()
        order_service = OrderService(client)
    except Exception as e:
        print(f"❌ Failed to initialize Binance client: {e}")
        return

    # Step 3: Place order
    order_type = args.type.upper()
    side = args.side.upper()

    if order_type == "MARKET":
        result = order_service.place_market_order(
            symbol=args.symbol,
            side=side,
            quantity=float(args.quantity)
        )
    else:
        result = order_service.place_limit_order(
            symbol=args.symbol,
            side=side,
            quantity=float(args.quantity),
            price=float(args.price)
        )

    # Step 4: Print result
    if result.get("success"):
        logger.info("Order placed successfully via CLI")
        print("✅ Order placed successfully")
        print(f"Order ID     : {result.get('orderId')}")
        print(f"Status       : {result.get('status')}")
        print(f"Executed Qty : {result.get('executedQty')}")
        print(f"Avg Price    : {result.get('avgPrice')}")
    else:
        print("❌ Order failed")
        print(f"Reason: {result.get('error')}")


if __name__ == "__main__":
    main()
