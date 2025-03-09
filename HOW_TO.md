# How To Use the Trading Signal Generator

This document provides a detailed explanation of how the Trading Signal Generator works, its components, and how to use it effectively.

## Table of Contents
1. [System Overview](#system-overview)
2. [Architecture](#architecture)
3. [Setting Up the Project](#setting-up-the-project)
4. [Using the API](#using-the-api)
5. [Understanding Signal Generation](#understanding-signal-generation)
6. [Backtesting](#backtesting)
7. [Customization Guide](#customization-guide)
8. [Troubleshooting](#troubleshooting)

## System Overview

The Trading Signal Generator is a backend application that:
1. Fetches real-time market data for Forex and Equities
2. Calculates technical indicators
3. Generates trading signals (BUY, SELL, HOLD)
4. Provides backtesting capabilities
5. Stores historical signals and performance metrics

### Key Features
- Real-time signal generation
- Multiple market support (Forex & Equities)
- Technical indicator calculations
- Historical backtesting
- REST API access
- Database storage

## Architecture

The system is built with a modular architecture:

```
app/
├── api/           # API endpoints
├── core/          # Core configuration and database
├── models/        # Database models
├── schemas/       # Pydantic schemas
└── services/      # Business logic
```

### Key Components

1. **Market Data Service** (`app/services/market_data.py`)
   - Fetches real-time data from:
     - Yahoo Finance for equities
     - Forex API for currency pairs
   - Handles data normalization

2. **Technical Indicators** (`app/services/technical_indicators.py`)
   - Calculates:
     - RSI (Relative Strength Index)
     - MACD (Moving Average Convergence Divergence)
     - SMA (Simple Moving Average)

3. **Signal Generator** (`app/services/signal_generator.py`)
   - Processes market data and indicators
   - Applies trading logic
   - Generates trading signals

4. **Backtest Service** (`app/services/backtest.py`)
   - Tests strategies on historical data
   - Calculates performance metrics

## Setting Up the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Thatous/trading-signal-generator.git
   cd trading-signal-generator
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your:
   - Database credentials
   - API keys
   - Other configuration parameters

4. **Initialize Database**
   ```bash
   python database/init_db.py
   ```

5. **Start the Application**
   ```bash
   uvicorn main:app --reload
   ```

### Docker Setup (Alternative)
```bash
docker build -t trading-signal-generator .
docker run -p 8000:8000 trading-signal-generator
```

## Using the API

### 1. Get Trading Signals

**Endpoint:** `GET /signals/{asset}`

```bash
curl http://localhost:8000/signals/AAPL
```

Response:
```json
{
  "asset": "AAPL",
  "timestamp": "2024-03-09T10:00:00Z",
  "signal": "BUY",
  "price": 150.25,
  "rsi": 29.5,
  "macd": 0.02
}
```

### 2. Run Backtest

**Endpoint:** `POST /backtest`

```bash
curl -X POST http://localhost:8000/backtest \
  -H "Content-Type: application/json" \
  -d '{
    "asset": "AAPL",
    "start_date": "2024-01-01",
    "end_date": "2024-03-01"
  }'
```

Response:
```json
{
  "asset": "AAPL",
  "backtest_period": "2024-01-01 to 2024-03-01",
  "net_profit": 1500.00,
  "profit_factor": 1.8,
  "win_rate": 0.60,
  "max_drawdown": -500.00
}
```

## Understanding Signal Generation

The signal generation process follows these steps:

1. **Data Collection**
   - Fetches latest market data
   - Normalizes data format

2. **Indicator Calculation**
   - RSI calculation (14-period default)
   - MACD calculation (12,26,9 default periods)
   - Additional technical indicators

3. **Signal Logic**
   - BUY Signal Conditions:
     - RSI < 30 (oversold)
     - MACD > 0 (positive momentum)
   
   - SELL Signal Conditions:
     - RSI > 70 (overbought)
     - MACD < 0 (negative momentum)
   
   - HOLD Signal:
     - When neither BUY nor SELL conditions are met

## Backtesting

The backtesting engine allows you to:
1. Test trading strategies on historical data
2. Calculate performance metrics
3. Optimize strategy parameters

### Key Metrics
- Net Profit/Loss
- Win Rate
- Profit Factor
- Maximum Drawdown
- Risk-Adjusted Return

## Customization Guide

### 1. Adding New Technical Indicators

Add new indicators in `app/services/technical_indicators.py`:
```python
def calculate_new_indicator(self, data: Dict[str, Any]) -> float:
    # Implementation
    pass
```

### 2. Modifying Signal Logic

Update signal conditions in `app/services/signal_generator.py`:
```python
def _determine_signal(self, rsi: float, macd: float) -> SignalType:
    # Modify conditions here
    pass
```

### 3. Adding New Data Sources

Extend `MarketDataService` in `app/services/market_data.py`:
```python
async def _get_new_source_data(self, symbol: str) -> Dict[str, Any]:
    # Implementation
    pass
```

## Troubleshooting

### Common Issues

1. **Database Connection Errors**
   - Check database credentials in `.env`
   - Ensure PostgreSQL is running
   - Verify database exists

2. **API Key Issues**
   - Verify API keys in `.env`
   - Check API rate limits
   - Ensure proper API permissions

3. **Performance Issues**
   - Monitor database query performance
   - Check network latency for data sources
   - Consider caching frequently used data

### Logging

The application logs are available at:
- Application logs: `logs/app.log`
- Error logs: `logs/error.log`

### Support

For additional support:
1. Check the GitHub issues
2. Review the test cases
3. Consult the API documentation at `/docs`

## Best Practices

1. **Production Deployment**
   - Use proper SSL/TLS
   - Implement rate limiting
   - Set up monitoring
   - Configure proper logging

2. **Data Management**
   - Regular database backups
   - Data cleanup policies
   - Cache management

3. **Strategy Development**
   - Test strategies thoroughly
   - Start with small positions
   - Monitor performance metrics
   - Implement risk management