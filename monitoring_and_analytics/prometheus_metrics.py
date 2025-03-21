from prometheus_client import Counter, Histogram, Info

# Signal Generation Metrics
signal_generation_total = Counter(
    'trading_signal_generation_total',
    'Total number of trading signals generated',
    ['asset', 'signal_type']
)

signal_generation_duration = Histogram(
    'trading_signal_generation_duration_seconds',
    'Time spent generating trading signals',
    ['asset']
)

# Market Data Metrics
market_data_fetch_total = Counter(
    'market_data_fetch_total',
    'Total number of market data fetch operations',
    ['asset', 'source']
)

market_data_fetch_errors = Counter(
    'market_data_fetch_errors_total',
    'Total number of market data fetch errors',
    ['asset', 'source', 'error_type']
)

# Backtest Metrics
backtest_execution_total = Counter(
    'backtest_execution_total',
    'Total number of backtest executions',
    ['asset']
)

backtest_duration = Histogram(
    'backtest_duration_seconds',
    'Time spent running backtests',
    ['asset']
)

# System Info
system_info = Info('trading_signal_generator_info', 'Information about the trading signal generator')
