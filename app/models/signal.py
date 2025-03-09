from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from app.core.database import Base
import enum
from datetime import datetime

class SignalType(str, enum.Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"

class Signal(Base):
    __tablename__ = "signals"

    id = Column(Integer, primary_key=True, index=True)
    asset = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    signal = Column(Enum(SignalType))
    price = Column(Float)
    rsi = Column(Float)
    macd = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)