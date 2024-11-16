# Etfs

## Holdings

Types:

```python
from tradesignals.types.etfs import OpenAPIUri
```

Methods:

- <code title="get /api/etfs/{ticker}/holdings">client.etfs.holdings.<a href="./src/tradesignals/resources/etfs/holdings.py">holdings</a>(ticker) -> <a href="./src/tradesignals/types/etfs/openapi_uri.py">OpenAPIUri</a></code>

# Darkpool

## RecentDarkpoolTrades

Types:

```python
from tradesignals.types.darkpool import RecentDarkpoolTradeRetrieveResponse
```

Methods:

- <code title="get /api/darkpool/recent">client.darkpool.recent_darkpool_trades.<a href="./src/tradesignals/resources/darkpool/recent_darkpool_trades.py">retrieve</a>(\*\*<a href="src/tradesignals/types/darkpool/recent_darkpool_trade_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/darkpool/recent_darkpool_trade_retrieve_response.py">RecentDarkpoolTradeRetrieveResponse</a></code>

## TickerDarkpoolTrades

Types:

```python
from tradesignals.types.darkpool import TickerDarkpoolTradeRetrieveResponse
```

Methods:

- <code title="get /api/darkpool/{ticker}">client.darkpool.ticker_darkpool_trades.<a href="./src/tradesignals/resources/darkpool/ticker_darkpool_trades.py">retrieve</a>(ticker, \*\*<a href="src/tradesignals/types/darkpool/ticker_darkpool_trade_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/darkpool/ticker_darkpool_trade_retrieve_response.py">TickerDarkpoolTradeRetrieveResponse</a></code>
