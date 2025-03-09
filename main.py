from fastapi import FastAPI, Depends, HTTPException
from app.api import signals, backtest
from app.core.config import settings

app = FastAPI(
    title="Trading Signal Generator",
    description="API for generating trading signals for Forex and Equities markets",
    version="1.0.0"
)

# Include routers
app.include_router(signals.router, prefix="/signals", tags=["signals"])
app.include_router(backtest.router, prefix="/backtest", tags=["backtest"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Trading Signal Generator API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=settings.API_HOST, port=settings.API_PORT, reload=True)