from binance.exceptions import BinanceAPIException, BinanceOrderException
from bot.logging_config import setup_logger

logger = setup_logger()


class OrderService:

    def __init__(self, binance_client):
        self.client = binance_client.client

    def place_market_order(self, symbol, side, quantity):
        logger.info(f"Placing MARKET order | {symbol} | {side} | qty={quantity}")
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logger.info(f"MARKET order success | orderId={order.get('orderId')}")
            return self._format_response(order)

        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f"MARKET order failed | {str(e)}")
            return self._error_response(str(e))

    def place_limit_order(self, symbol, side, quantity, price):
        logger.info(
            f"Placing LIMIT order | {symbol} | {side} | qty={quantity} | price={price}"
        )
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logger.info(f"LIMIT order success | orderId={order.get('orderId')}")
            return self._format_response(order)

        except (BinanceAPIException, BinanceOrderException) as e:
            logger.error(f"LIMIT order failed | {str(e)}")
            return self._error_response(str(e))

    def _format_response(self, order):
        return {
            "success": True,
            "orderId": order.get("orderId"),
            "status": order.get("status"),
            "executedQty": order.get("executedQty"),
            "avgPrice": order.get("avgPrice")
        }

    def _error_response(self, message):
        return {
            "success": False,
            "error": message
        }
