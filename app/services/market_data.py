import yfinance as yf
from typing import Dict, Any
import aiohttp
from app.core.config import settings

class MarketDataService:
    def __init__(self):
        self.forex_api_key = settings.FOREX_API_KEY

    async def get_latest_data(self, asset: str) -> Dict[str, Any]:
        if self._is_forex(asset):
            return await self._get_forex_data(asset)
        return await self._get_equity_data(asset)

    async def _get_forex_data(self, pair: str) -> Dict[str, Any]:
        async with aiohttp.ClientSession() as session:
            url = f"https://api.forexapi.com/v1/latest?symbol={pair}&apikey={self.forex_api_key}"
            async with session.get(url) as response:
                data = await response.json()
                return {
                    "close": data["rates"][pair],
                    "timestamp": data["timestamp"]
                }

    async def _get_equity_data(self, symbol: str) -> Dict[str, Any]:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1d")
        return {
            "close": hist["Close"].iloc[-1],
            "timestamp": hist.index[-1].to_pydatetime()
        }

    def _is_forex(self, asset: str) -> bool:
        return len(asset) == 6 and asset.isupper()