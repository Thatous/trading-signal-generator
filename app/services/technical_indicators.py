import pandas as pd
import numpy as np
from typing import Dict, Any

class TechnicalIndicators:
    def calculate_rsi(self, data: Dict[str, Any], period: int = 14) -> float:
        # Simplified RSI calculation for demo
        # In production, you would use a proper RSI calculation
        price = data["close"]
        return 50.0 + np.random.normal(0, 10)  # Simulated RSI

    def calculate_macd(self, data: Dict[str, Any]) -> float:
        # Simplified MACD calculation for demo
        # In production, you would use proper MACD calculation
        price = data["close"]
        return np.random.normal(0, 0.5)  # Simulated MACD

    def calculate_sma(self, data: Dict[str, Any], period: int = 20) -> float:
        # Simplified SMA calculation
        price = data["close"]
        return price  # For demo, just return current price