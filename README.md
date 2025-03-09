# Trading Signal Generator MVP

A backend application that processes financial market data to generate buy, sell, or hold signals for different financial assets. The system supports both Forex and Equities markets.

## Features

- Data Ingestion: Collect market data from external sources
- Indicator Computation: Calculate SMA, RSI, MACD, and other technical indicators
- Signal Generation: Define conditions for entry and exit based on computed indicators
- Backtesting Engine: Evaluate signal performance on historical data
- Database Storage: Store market data and generated signals in PostgreSQL
- API Integration: Access signals via REST API endpoints

## Supported Markets

### Forex
Major pairs supported:
- EURUSD
- GBPUSD
- USDJPY
- AUDUSD
- USDCAD
- USDCHF
- NZDUSD

### Equities
US Equities (NYSE and NASDAQ):
- SPY
- AAPL
- GOOGL
- MSFT
- TSLA
- AMZN

## Setup Instructions

### Prerequisites

- Python 3.9+
- PostgreSQL
- Docker (optional, for containerized deployment)

### Environment Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. Create a PostgreSQL database
2. Copy `.env.example` to `.env` and update the database credentials
3. Run database migrations:
   ```bash
   python database/init_db.py
   ```

### Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Access the API documentation at `http://localhost:8000/docs`

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t trading-signal-generator .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 trading-signal-generator
   ```

## API Documentation

### Endpoints

#### GET /signals
Get the latest trading signal for a specific asset.

Request:
```
GET /signals?asset=SPY
```

Response:
```json
{
  "asset": "SPY",
  "timestamp": "2024-01-01T10:00:00Z",
  "signal": "BUY",
  "rsi": 29.5,
  "macd": 0.02
}
```

#### POST /backtest
Run a backtest for a specific asset over a date range.

Request:
```json
{
  "asset": "SPY",
  "start_date": "2023-01-01",
  "end_date": "2023-12-31"
}
```

Response:
```json
{
  "asset": "SPY",
  "backtest_period": "2023-01-01 to 2023-12-31",
  "net_profit": 1500.00,
  "profit_factor": 1.8,
  "win_rate": 0.60,
  "max_drawdown": -500.00
}
```

## Data Sources

- Equities: Yahoo Finance (via yfinance library)
- Forex: Free Forex API (via public endpoints)

## License

MIT License