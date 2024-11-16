# Shared Types

```python
from tradesignals.types import (
    DarkpoolTrade,
    DarkpoolTradesResponse,
    EtfHolding,
    EtfHoldingsResponse,
    EtfInOutflow,
    EtfInOutflowResponse,
)
```

# Etf

## Holdings

Types:

```python
from tradesignals.types.etf import HoldingRetrieveResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/holdings">client.etf.holdings.<a href="./src/tradesignals/resources/etf/holdings.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/etf/holding_retrieve_response.py">Optional</a></code>

## InflowOutflow

Types:

```python
from tradesignals.types.etf import InflowOutflowRetrieveResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/in-outflow">client.etf.inflow_outflow.<a href="./src/tradesignals/resources/etf/inflow_outflow.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/etf/inflow_outflow_retrieve_response.py">Optional</a></code>

## Info

Types:

```python
from tradesignals.types.etf import InfoRetrieveResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/info">client.etf.info.<a href="./src/tradesignals/resources/etf/info.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/etf/info_retrieve_response.py">InfoRetrieveResponse</a></code>

## Exposure

Types:

```python
from tradesignals.types.etf import ExposureRetrieveResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/exposure">client.etf.exposure.<a href="./src/tradesignals/resources/etf/exposure.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/etf/exposure_retrieve_response.py">ExposureRetrieveResponse</a></code>

# Darkpool

## RecentDarkpoolTrades

Types:

```python
from tradesignals.types.darkpool import RecentDarkpoolTradeRetrieveResponse
```

Methods:

- <code title="get /api/darkpool/recent">client.darkpool.recent_darkpool_trades.<a href="./src/tradesignals/resources/darkpool/recent_darkpool_trades.py">retrieve</a>(\*\*<a href="src/tradesignals/types/darkpool/recent_darkpool_trade_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/darkpool/recent_darkpool_trade_retrieve_response.py">Optional</a></code>

## TickerDarkpoolTrades

Types:

```python
from tradesignals.types.darkpool import TickerDarkpoolTradeRetrieveResponse
```

Methods:

- <code title="get /api/darkpool/{ticker}">client.darkpool.ticker_darkpool_trades.<a href="./src/tradesignals/resources/darkpool/ticker_darkpool_trades.py">retrieve</a>(ticker, \*\*<a href="src/tradesignals/types/darkpool/ticker_darkpool_trade_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/darkpool/ticker_darkpool_trade_retrieve_response.py">Optional</a></code>
