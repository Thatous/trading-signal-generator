from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.signal import SignalType

class SignalBase(BaseModel):
    asset: str
    signal: SignalType
    price: float
    rsi: float
    macd: float

class SignalCreate(SignalBase):
    pass

class Signal(SignalBase):
    id: int
    timestamp: datetime
    created_at: datetime

    class Config:
        from_attributes = True