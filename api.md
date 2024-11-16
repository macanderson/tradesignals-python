# Etfs

## Holdings

Types:

```python
from tradesignals.types.etfs import EtfHolding, EtfHoldingsResponse, HoldingListResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/holdings">client.etfs.holdings.<a href="./src/tradesignals/resources/etfs/holdings.py">list</a>(ticker) -> <a href="./src/tradesignals/types/etfs/holding_list_response.py">Optional</a></code>

## InflowsOutflows

Types:

```python
from tradesignals.types.etfs import EtfInOutflow, EtfInOutflowResponse, InflowsOutflowListResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/in-outflow">client.etfs.inflows_outflows.<a href="./src/tradesignals/resources/etfs/inflows_outflows.py">list</a>(ticker) -> <a href="./src/tradesignals/types/etfs/inflows_outflow_list_response.py">Optional</a></code>

## Information

Types:

```python
from tradesignals.types.etfs import EtfInfo, EtfInfoResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/info">client.etfs.information.<a href="./src/tradesignals/resources/etfs/information.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/etfs/etf_info.py">EtfInfo</a></code>

## Exposure

Types:

```python
from tradesignals.types.etfs import EtfExposureData, EtfExposureResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/exposure">client.etfs.exposure.<a href="./src/tradesignals/resources/etfs/exposure.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/etfs/etf_exposure_response.py">EtfExposureResponse</a></code>

# Darkpool

Types:

```python
from tradesignals.types import TickerDarkpoolResponse, TickerDarkpoolTrade
```

## RecentDarkpoolTrades

Types:

```python
from tradesignals.types.darkpool import RecentDarkpoolTradeListResponse
```

Methods:

- <code title="get /api/darkpool/recent">client.darkpool.recent_darkpool_trades.<a href="./src/tradesignals/resources/darkpool/recent_darkpool_trades.py">list</a>(\*\*<a href="src/tradesignals/types/darkpool/recent_darkpool_trade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/darkpool/recent_darkpool_trade_list_response.py">Optional</a></code>

## TickerDarkpoolTrades

Types:

```python
from tradesignals.types.darkpool import TickerDarkpoolTradeListResponse
```

Methods:

- <code title="get /api/darkpool/{ticker}">client.darkpool.ticker_darkpool_trades.<a href="./src/tradesignals/resources/darkpool/ticker_darkpool_trades.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/darkpool/ticker_darkpool_trade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/darkpool/ticker_darkpool_trade_list_response.py">Optional</a></code>
