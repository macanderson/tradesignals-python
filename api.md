# Congress

## RecentTrades

Types:

```python
from tradesignals.types.congress import CongressionalTrade, RecentTradeListResponse
```

Methods:

- <code title="get /api/congress/recent-trades">client.congress.recent_trades.<a href="./src/tradesignals/resources/congress/recent_trades.py">list</a>(\*\*<a href="src/tradesignals/types/congress/recent_trade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/recent_trade_list_response.py">Optional</a></code>

## LateReports

Types:

```python
from tradesignals.types.congress import LateCongressionalReport, LateReportListResponse
```

Methods:

- <code title="get /api/congress/late-reports">client.congress.late_reports.<a href="./src/tradesignals/resources/congress/late_reports.py">list</a>(\*\*<a href="src/tradesignals/types/congress/late_report_list_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/late_report_list_response.py">Optional</a></code>

## CongressTrader

Types:

```python
from tradesignals.types.congress import CongressionalTraderReport
```

Methods:

- <code title="get /api/congress/congress-trader">client.congress.congress_trader.<a href="./src/tradesignals/resources/congress/congress_trader.py">retrieve</a>(\*\*<a href="src/tradesignals/types/congress/congress_trader_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/late_congressional_report.py">LateCongressionalReport</a></code>

## RecentReports

Types:

```python
from tradesignals.types.congress import RecentCongressionalReport, RecentReportListResponse
```

Methods:

- <code title="get /api/congress/recent-reports">client.congress.recent_reports.<a href="./src/tradesignals/resources/congress/recent_reports.py">list</a>(\*\*<a href="src/tradesignals/types/congress/recent_report_list_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/recent_report_list_response.py">Optional</a></code>

# IndustryGroups

Types:

```python
from tradesignals.types import GroupGreekFlow
```

## GreekFlows

Types:

```python
from tradesignals.types.industry_groups import GreekFlowListResponse
```

Methods:

- <code title="get /api/group-flow/{flow_group}/greek-flow">client.industry_groups.greek_flows.<a href="./src/tradesignals/resources/industry_groups/greek_flows.py">list</a>(flow_group, \*\*<a href="src/tradesignals/types/industry_groups/greek_flow_list_params.py">params</a>) -> <a href="./src/tradesignals/types/industry_groups/greek_flow_list_response.py">Optional</a></code>

## GreekFlowsByExpiry

Types:

```python
from tradesignals.types.industry_groups import GreekFlowsByExpiryListResponse
```

Methods:

- <code title="get /api/group-flow/{flow_group}/greek-flow/{expiry}">client.industry_groups.greek_flows_by_expiry.<a href="./src/tradesignals/resources/industry_groups/greek_flows_by_expiry.py">list</a>(expiry, \*, flow_group, \*\*<a href="src/tradesignals/types/industry_groups/greek_flows_by_expiry_list_params.py">params</a>) -> <a href="./src/tradesignals/types/industry_groups/greek_flows_by_expiry_list_response.py">Optional</a></code>

# Etfs

## Holdings

Types:

```python
from tradesignals.types.etfs import Holdings, HoldingListResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/holdings">client.etfs.holdings.<a href="./src/tradesignals/resources/etfs/holdings.py">list</a>(ticker) -> <a href="./src/tradesignals/types/etfs/holding_list_response.py">Optional</a></code>

## InflowsOutflows

Types:

```python
from tradesignals.types.etfs import Outflows, InflowsOutflowListResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/in-outflow">client.etfs.inflows_outflows.<a href="./src/tradesignals/resources/etfs/inflows_outflows.py">list</a>(ticker) -> <a href="./src/tradesignals/types/etfs/inflows_outflow_list_response.py">Optional</a></code>

## Information

Types:

```python
from tradesignals.types.etfs import Info, InformationRetrieveResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/info">client.etfs.information.<a href="./src/tradesignals/resources/etfs/information.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/etfs/information_retrieve_response.py">Optional</a></code>

## Exposure

Types:

```python
from tradesignals.types.etfs import Exposure, ExposureRetrieveResponse
```

Methods:

- <code title="get /api/etfs/{ticker}/exposure">client.etfs.exposure.<a href="./src/tradesignals/resources/etfs/exposure.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/etfs/exposure_retrieve_response.py">Optional</a></code>

## SectorCountryWeights

Types:

```python
from tradesignals.types.etfs import Weights
```

Methods:

- <code title="get /api/etfs/{ticker}/weights">client.etfs.sector_country_weights.<a href="./src/tradesignals/resources/etfs/sector_country_weights.py">list</a>(ticker) -> <a href="./src/tradesignals/types/etfs/weights.py">Weights</a></code>

# Darkpool

Types:

```python
from tradesignals.types import Trade
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
