from sqlalchemy.orm import Session
from app.models.signal import Signal, SignalType
from app.services.market_data import MarketDataService
from app.services.technical_indicators import TechnicalIndicators

class SignalGenerator:
    def __init__(self, db: Session):
        self.db = db
        self.market_data = MarketDataService()
        self.indicators = TechnicalIndicators()

    async def generate_signal(self, asset: str) -> Signal:
        # Get latest market data
        price_data = await self.market_data.get_latest_data(asset)
        
        # Calculate indicators
        rsi = self.indicators.calculate_rsi(price_data)
        macd = self.indicators.calculate_macd(price_data)
        
        # Generate signal based on indicators
        signal = self._determine_signal(rsi, macd)
        
        # Create and save signal
        new_signal = Signal(
            asset=asset,
            signal=signal,
            price=price_data["close"],
            rsi=rsi,
            macd=macd
        )
        
        self.db.add(new_signal)
        self.db.commit()
        self.db.refresh(new_signal)
        
        return new_signal

    def _determine_signal(self, rsi: float, macd: float) -> SignalType:
        if rsi < 30 and macd > 0:
            return SignalType.BUY
        elif rsi > 70 and macd < 0:
            return SignalType.SELL
        return SignalType.HOLD