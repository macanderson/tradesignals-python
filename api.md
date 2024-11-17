# Congress

## RecentTrades

Types:

```python
from tradesignals.types.congress import CongressionalTrade, RecentTradeListResponse
```

Methods:

- <code title="get /api/congress/recent-trades">client.congress.recent_trades.<a href="./src/tradesignals/resources/congress/recent_trades.py">list</a>(\*\*<a href="src/tradesignals/types/congress/recent_trade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/recent_trade_list_response.py">Optional</a></code>

## LateTradeReports

Types:

```python
from tradesignals.types.congress import LateCongressionalReport, LateTradeReportListResponse
```

Methods:

- <code title="get /api/congress/late-reports">client.congress.late_trade_reports.<a href="./src/tradesignals/resources/congress/late_trade_reports.py">list</a>(\*\*<a href="src/tradesignals/types/congress/late_trade_report_list_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/late_trade_report_list_response.py">Optional</a></code>

## Trader

Types:

```python
from tradesignals.types.congress import CongressionalTraderReport
```

Methods:

- <code title="get /api/congress/congress-trader">client.congress.trader.<a href="./src/tradesignals/resources/congress/trader.py">retrieve</a>(\*\*<a href="src/tradesignals/types/congress/trader_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/congressional_trader_report.py">CongressionalTraderReport</a></code>

## RecentTradeReports

Types:

```python
from tradesignals.types.congress import RecentCongressionalReport, RecentTradeReportListResponse
```

Methods:

- <code title="get /api/congress/recent-reports">client.congress.recent_trade_reports.<a href="./src/tradesignals/resources/congress/recent_trade_reports.py">list</a>(\*\*<a href="src/tradesignals/types/congress/recent_trade_report_list_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/recent_trade_report_list_response.py">Optional</a></code>

# IndustryGroups

## GreekFlows

Types:

```python
from tradesignals.types.industry_groups import GroupGreekFlow, GreekFlowListResponse
```

Methods:

- <code title="get /api/group-flow/{flow_group}/greek-flow">client.industry_groups.greek_flows.<a href="./src/tradesignals/resources/industry_groups/greek_flows.py">list</a>(flow_group, \*\*<a href="src/tradesignals/types/industry_groups/greek_flow_list_params.py">params</a>) -> <a href="./src/tradesignals/types/industry_groups/greek_flow_list_response.py">Optional</a></code>

## GreekFlowsByExpiry

Types:

```python
from tradesignals.types.industry_groups import GroupFlowsResponse, GreekFlowsByExpiryListResponse
```

Methods:

- <code title="get /api/group-flow/{flow_group}/greek-flow/{expiry}">client.industry_groups.greek_flows_by_expiry.<a href="./src/tradesignals/resources/industry_groups/greek_flows_by_expiry.py">list</a>(expiry, \*, flow_group, \*\*<a href="src/tradesignals/types/industry_groups/greek_flows_by_expiry_list_params.py">params</a>) -> <a href="./src/tradesignals/types/industry_groups/greek_flows_by_expiry_list_response.py">Optional</a></code>

# Etf

## Holdings

Types:

```python
from tradesignals.types.etf import Holdings, HoldingListResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/holdings">client.etf.holdings.<a href="./src/tradesignals/resources/etf/holdings.py">list</a>(ticker) -> <a href="./src/tradesignals/types/etf/holding_list_response.py">Optional</a></code>

## InflowsOutflows

Types:

```python
from tradesignals.types.etf import Outflows, InflowsOutflowListResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/in-outflow">client.etf.inflows_outflows.<a href="./src/tradesignals/resources/etf/inflows_outflows.py">list</a>(ticker) -> <a href="./src/tradesignals/types/etf/inflows_outflow_list_response.py">Optional</a></code>

## Information

Types:

```python
from tradesignals.types.etf import Info, InformationRetrieveResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/info">client.etf.information.<a href="./src/tradesignals/resources/etf/information.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/etf/information_retrieve_response.py">Optional</a></code>

## Exposure

Types:

```python
from tradesignals.types.etf import Exposure, ExposureRetrieveResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/exposure">client.etf.exposure.<a href="./src/tradesignals/resources/etf/exposure.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/etf/exposure_retrieve_response.py">Optional</a></code>

## Weights

Types:

```python
from tradesignals.types.etf import Weights
```

Methods:

- <code title="get /api/etfs/{ticker}/weights">client.etf.weights.<a href="./src/tradesignals/resources/etf/weights.py">list</a>(ticker) -> <a href="./src/tradesignals/types/etf/weights.py">Weights</a></code>

# Darkpool

Types:

```python
from tradesignals.types import Trade
```

## RecentTrades

Types:

```python
from tradesignals.types.darkpool import RecentTradeListResponse
```

Methods:

- <code title="get /api/darkpool/recent">client.darkpool.recent_trades.<a href="./src/tradesignals/resources/darkpool/recent_trades.py">list</a>(\*\*<a href="src/tradesignals/types/darkpool/recent_trade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/darkpool/recent_trade_list_response.py">Optional</a></code>

## TradesByTicker

Types:

```python
from tradesignals.types.darkpool import TradesByTickerListResponse
```

Methods:

- <code title="get /api/darkpool/{ticker}">client.darkpool.trades_by_ticker.<a href="./src/tradesignals/resources/darkpool/trades_by_ticker.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/darkpool/trades_by_ticker_list_params.py">params</a>) -> <a href="./src/tradesignals/types/darkpool/trades_by_ticker_list_response.py">Optional</a></code>
