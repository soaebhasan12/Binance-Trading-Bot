import os
from binance.client import Client
from dotenv import load_dotenv


class BinanceFuturesClient:
    """
    Binance Futures Testnet client.
    Sirf API connection ke liye – no trading logic here.
    """

    def __init__(self):
        load_dotenv()

        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("API key or secret not found in environment variables")

        # Binance Futures client (USDT-M)
        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True
        )

        # Futures Testnet base URL (IMPORTANT)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def test_connection(self):
        """
        Simple method to verify:
        - API keys are valid
        - Futures testnet is reachable
        """
        try:
            account_info = self.client.futures_account()
            return {
                "status": "success",
                "account": account_info.get("accountAlias"),
                "canTrade": account_info.get("canTrade")
            }
        except Exception as e:
            return {
                "status": "failure",
                "error": str(e)
            }


if __name__ == "__main__":
    client = BinanceFuturesClient()
    result = client.test_connection()
    print(result)
