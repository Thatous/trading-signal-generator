from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.signal import Signal, SignalCreate
from app.services.signal_generator import SignalGenerator
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()

@router.get("/{asset}", response_model=Signal)
async def get_signal(asset: str, db: Session = Depends(get_db)):
    try:
        signal_generator = SignalGenerator(db)
        return await signal_generator.generate_signal(asset)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))