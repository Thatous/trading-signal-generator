from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.backtest import BacktestService
from datetime import date
from typing import Optional

router = APIRouter()

@router.post("/")
async def run_backtest(
    asset: str,
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db)
):
    try:
        backtest_service = BacktestService(db)
        results = await backtest_service.run_backtest(asset, start_date, end_date)
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))