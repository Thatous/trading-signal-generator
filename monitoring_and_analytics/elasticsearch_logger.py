from elasticsearch import Elasticsearch
from datetime import datetime
from typing import Dict, Any

class ElasticsearchLogger:
    def __init__(self, es_host: str, es_port: int, index_prefix: str = 'trading_signals'):
        self.es = Elasticsearch([{'host': es_host, 'port': es_port}])
        self.index_prefix = index_prefix

    def _get_current_index(self) -> str:
        return f"{self.index_prefix}-{datetime.now().strftime('%Y.%m')}"

    def log_signal(self, signal_data: Dict[str, Any]):
        document = {
            'timestamp': datetime.utcnow(),
            'type': 'signal',
            **signal_data
        }
        self.es.index(index=self._get_current_index(), body=document)

    def log_backtest(self, backtest_data: Dict[str, Any]):
        document = {
            'timestamp': datetime.utcnow(),
            'type': 'backtest',
            **backtest_data
        }
        self.es.index(index=self._get_current_index(), body=document)

    def log_market_data(self, market_data: Dict[str, Any]):
        document = {
            'timestamp': datetime.utcnow(),
            'type': 'market_data',
            **market_data
        }
        self.es.index(index=self._get_current_index(), body=document)
