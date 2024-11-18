# Stock

## FlowPerExpiry

Types:

```python
from tradesignals.types.stock import ExpiryFlow, ExpiryFlowResponse, FlowPerExpiryListResponse
```

Methods:

- <code title="get /api/stock/{ticker}/flow-per-expiry">client.stock.flow_per_expiry.<a href="./src/tradesignals/resources/stock/flow_per_expiry.py">list</a>(ticker) -> <a href="./src/tradesignals/types/stock/flow_per_expiry_list_response.py">Optional</a></code>

## OptionAlerts

Types:

```python
from tradesignals.types.stock import OptionAlert, OptionAlertResponse, OptionAlertListResponse
```

Methods:

- <code title="get /api/stock/{ticker}/flow-alerts">client.stock.option_alerts.<a href="./src/tradesignals/resources/stock/option_alerts.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/stock/option_alert_list_params.py">params</a>) -> <a href="./src/tradesignals/types/stock/option_alert_list_response.py">Optional</a></code>

## SectorTickers

Types:

```python
from tradesignals.types.stock import SectorTickersResponse, SectorTickerListResponse
```

Methods:

- <code title="get /api/stock/{sector}/tickers">client.stock.sector_tickers.<a href="./src/tradesignals/resources/stock/sector_tickers.py">list</a>(sector) -> <a href="./src/tradesignals/types/stock/sector_ticker_list_response.py">Optional</a></code>

## AtmChains

Types:

```python
from tradesignals.types.stock import AtmChainEntry, AtmChainsResponse, AtmChainListResponse
```

Methods:

- <code title="get /api/stock/{ticker}/atm-chains">client.stock.atm_chains.<a href="./src/tradesignals/resources/stock/atm_chains.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/stock/atm_chain_list_params.py">params</a>) -> <a href="./src/tradesignals/types/stock/atm_chain_list_response.py">Optional</a></code>

# Seasonality

## TickerSeasonality

Types:

```python
from tradesignals.types.seasonality import (
    MonthlyAverageEntry,
    MonthlyAverageResponse,
    TickerSeasonalityListResponse,
)
```

Methods:

- <code title="get /api/seasonality/{ticker}/monthly">client.seasonality.ticker_seasonality.<a href="./src/tradesignals/resources/seasonality/ticker_seasonality.py">list</a>(ticker) -> <a href="./src/tradesignals/types/seasonality/ticker_seasonality_list_response.py">Optional</a></code>

## YearMonthChange

Types:

```python
from tradesignals.types.seasonality import (
    YearMonthEntry,
    YearMonthResponse,
    YearMonthChangeListResponse,
)
```

Methods:

- <code title="get /api/seasonality/{ticker}/year-month">client.seasonality.year_month_change.<a href="./src/tradesignals/resources/seasonality/year_month_change.py">list</a>(ticker) -> <a href="./src/tradesignals/types/seasonality/year_month_change_list_response.py">Optional</a></code>

## MarketSeasonality

Types:

```python
from tradesignals.types.seasonality import (
    MarketSeasonalityResponse,
    SeasonalityEntry,
    MarketSeasonalityListResponse,
)
```

Methods:

- <code title="get /api/seasonality/market">client.seasonality.market_seasonality.<a href="./src/tradesignals/resources/seasonality/market_seasonality.py">list</a>() -> <a href="./src/tradesignals/types/seasonality/market_seasonality_list_response.py">Optional</a></code>

## TopPerformers

Types:

```python
from tradesignals.types.seasonality import (
    MonthPerformerEntry,
    MonthPerformersResponse,
    TopPerformerListResponse,
)
```

Methods:

- <code title="get /api/seasonality/{month}/performers">client.seasonality.top_performers.<a href="./src/tradesignals/resources/seasonality/top_performers.py">list</a>(month, \*\*<a href="src/tradesignals/types/seasonality/top_performer_list_params.py">params</a>) -> <a href="./src/tradesignals/types/seasonality/top_performer_list_response.py">Optional</a></code>

# Screeners

## StockFinder

Types:

```python
from tradesignals.types.screeners import StockEntry, StockScreenerResponse, StockFinderListResponse
```

Methods:

- <code title="get /api/screener/stocks">client.screeners.stock_finder.<a href="./src/tradesignals/resources/screeners/stock_finder.py">list</a>(\*\*<a href="src/tradesignals/types/screeners/stock_finder_list_params.py">params</a>) -> <a href="./src/tradesignals/types/screeners/stock_finder_list_response.py">Optional</a></code>

## AnalystRatings

Types:

```python
from tradesignals.types.screeners import (
    AnalystRatingEntry,
    AnalystRatingResponse,
    AnalystRatingListResponse,
)
```

Methods:

- <code title="get /api/screener/analysts">client.screeners.analyst_ratings.<a href="./src/tradesignals/resources/screeners/analyst_ratings.py">list</a>(\*\*<a href="src/tradesignals/types/screeners/analyst_rating_list_params.py">params</a>) -> <a href="./src/tradesignals/types/screeners/analyst_rating_list_response.py">Optional</a></code>

## OptionFinder

Types:

```python
from tradesignals.types.screeners import (
    HottestChainEntry,
    HottestChainsResponse,
    OptionFinderListResponse,
)
```

Methods:

- <code title="get /api/screener/option-contracts">client.screeners.option_finder.<a href="./src/tradesignals/resources/screeners/option_finder.py">list</a>(\*\*<a href="src/tradesignals/types/screeners/option_finder_list_params.py">params</a>) -> <a href="./src/tradesignals/types/screeners/option_finder_list_response.py">Optional</a></code>

# OptionTrades

## FlowAlerts

Types:

```python
from tradesignals.types.option_trades import (
    FlowAlertEntry,
    FlowAlertResponse,
    FlowAlertListResponse,
)
```

Methods:

- <code title="get /api/option-trades/flow-alerts">client.option_trades.flow_alerts.<a href="./src/tradesignals/resources/option_trades/flow_alerts.py">list</a>() -> <a href="./src/tradesignals/types/option_trades/flow_alert_list_response.py">Optional</a></code>

# OptionContracts

## UnderlyingChains

Types:

```python
from tradesignals.types.option_contracts import (
    OptionContractsEntry,
    OptionContractsResponse,
    UnderlyingChainListResponse,
)
```

Methods:

- <code title="get /api/stock/{ticker}/option-contracts">client.option_contracts.underlying_chains.<a href="./src/tradesignals/resources/option_contracts/underlying_chains.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/option_contracts/underlying_chain_list_params.py">params</a>) -> <a href="./src/tradesignals/types/option_contracts/underlying_chain_list_response.py">Optional</a></code>

## FlowData

Types:

```python
from tradesignals.types.option_contracts import FlowDataResponse, FlowDataRetrieveResponse
```

Methods:

- <code title="get /api/option-contract/{id}/flow">client.option_contracts.flow_data.<a href="./src/tradesignals/resources/option_contracts/flow_data.py">retrieve</a>(id, \*\*<a href="src/tradesignals/types/option_contracts/flow_data_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/option_contracts/flow_data_retrieve_response.py">Optional</a></code>

## HistoricData

Types:

```python
from tradesignals.types.option_contracts import HistoricDataResponse, HistoricDataRetrieveResponse
```

Methods:

- <code title="get /api/option-contract/{id}/historic">client.option_contracts.historic_data.<a href="./src/tradesignals/resources/option_contracts/historic_data.py">retrieve</a>(id, \*\*<a href="src/tradesignals/types/option_contracts/historic_data_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/option_contracts/historic_data_retrieve_response.py">Optional</a></code>

## ExpiryBreakdown

Types:

```python
from tradesignals.types.option_contracts import (
    ExpiryBreakdownEntry,
    ExpiryBreakdownResponse,
    ExpiryBreakdownListResponse,
)
```

Methods:

- <code title="get /api/stock/{ticker}/expiry-breakdown">client.option_contracts.expiry_breakdown.<a href="./src/tradesignals/resources/option_contracts/expiry_breakdown.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/option_contracts/expiry_breakdown_list_params.py">params</a>) -> <a href="./src/tradesignals/types/option_contracts/expiry_breakdown_list_response.py">Optional</a></code>

# Market

## SectorEtfs

Types:

```python
from tradesignals.types.market import SectorEtfEntry, SectorEtfsResponse, SectorEtfListResponse
```

Methods:

- <code title="get /api/market/sector-etfs">client.market.sector_etfs.<a href="./src/tradesignals/resources/market/sector_etfs.py">list</a>() -> <a href="./src/tradesignals/types/market/sector_etf_list_response.py">Optional</a></code>

## Spike

Types:

```python
from tradesignals.types.market import SpikeEntry, SpikeResponse, SpikeListResponse
```

Methods:

- <code title="get /api/market/spike">client.market.spike.<a href="./src/tradesignals/resources/market/spike.py">list</a>(\*\*<a href="src/tradesignals/types/market/spike_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/spike_list_response.py">Optional</a></code>

## TotalOptionsVolume

Types:

```python
from tradesignals.types.market import (
    TotalOptionsVolumeEntry,
    TotalOptionsVolumeResponse,
    TotalOptionsVolumeListResponse,
)
```

Methods:

- <code title="get /api/market/total-options-volume">client.market.total_options_volume.<a href="./src/tradesignals/resources/market/total_options_volume.py">list</a>(\*\*<a href="src/tradesignals/types/market/total_options_volume_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/total_options_volume_list_response.py">Optional</a></code>

## EtfTide

Types:

```python
from tradesignals.types.market import EtfTideEntry, EtfTideResponse, EtfTideListResponse
```

Methods:

- <code title="get /api/market/{ticker}/etf-tide">client.market.etf_tide.<a href="./src/tradesignals/resources/market/etf_tide.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/market/etf_tide_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/etf_tide_list_response.py">Optional</a></code>

## MarketTide

Types:

```python
from tradesignals.types.market import MarketTideEntry, MarketTideResponse, MarketTideListResponse
```

Methods:

- <code title="get /api/market/market-tide">client.market.market_tide.<a href="./src/tradesignals/resources/market/market_tide.py">list</a>(\*\*<a href="src/tradesignals/types/market/market_tide_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/market_tide_list_response.py">Optional</a></code>

## OiChange

Types:

```python
from tradesignals.types.market import OiChangeEntry, OiChangeResponse, OiChangeListResponse
```

Methods:

- <code title="get /api/market/oi-change">client.market.oi_change.<a href="./src/tradesignals/resources/market/oi_change.py">list</a>(\*\*<a href="src/tradesignals/types/market/oi_change_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/oi_change_list_response.py">Optional</a></code>

## InsiderBuySells

Types:

```python
from tradesignals.types.market import (
    InsiderBuySell,
    InsiderBuySellsResponse,
    InsiderBuySellListResponse,
)
```

Methods:

- <code title="get /api/market/insider-buy-sells">client.market.insider_buy_sells.<a href="./src/tradesignals/resources/market/insider_buy_sells.py">list</a>(\*\*<a href="src/tradesignals/types/market/insider_buy_sell_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/insider_buy_sell_list_response.py">Optional</a></code>

## Correlations

Types:

```python
from tradesignals.types.market import Correlation, CorrelationsResponse, CorrelationListResponse
```

Methods:

- <code title="get /api/market/correlations">client.market.correlations.<a href="./src/tradesignals/resources/market/correlations.py">list</a>(\*\*<a href="src/tradesignals/types/market/correlation_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/correlation_list_response.py">Optional</a></code>

## EconomicCalendar

Types:

```python
from tradesignals.types.market import (
    EconomicCalendarEvent,
    EconomicCalendarResponse,
    EconomicCalendarListResponse,
)
```

Methods:

- <code title="get /api/market/economic-calendar">client.market.economic_calendar.<a href="./src/tradesignals/resources/market/economic_calendar.py">list</a>() -> <a href="./src/tradesignals/types/market/economic_calendar_list_response.py">Optional</a></code>

## FdaCalendar

Types:

```python
from tradesignals.types.market import FdaCalendarEvent, FdaCalendarResponse, FdaCalendarListResponse
```

Methods:

- <code title="get /api/market/fda-calendar">client.market.fda_calendar.<a href="./src/tradesignals/resources/market/fda_calendar.py">list</a>() -> <a href="./src/tradesignals/types/market/fda_calendar_list_response.py">Optional</a></code>

# Institutions

Types:

```python
from tradesignals.types import Institution, InstitutionsResponse, InstitutionListResponse
```

Methods:

- <code title="get /api/institutions">client.institutions.<a href="./src/tradesignals/resources/institutions/institutions.py">list</a>(\*\*<a href="src/tradesignals/types/institution_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institution_list_response.py">Optional</a></code>

## Activity

Types:

```python
from tradesignals.types.institutions import (
    InstitutionActivity,
    InstitutionActivityResponse,
    ActivityListResponse,
)
```

Methods:

- <code title="get /api/institution/{name}/activity">client.institutions.activity.<a href="./src/tradesignals/resources/institutions/activity.py">list</a>(name, \*\*<a href="src/tradesignals/types/institutions/activity_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institutions/activity_list_response.py">Optional</a></code>

## Holdings

Types:

```python
from tradesignals.types.institutions import (
    InstitutionHolding,
    InstitutionHoldingsResponse,
    HoldingListResponse,
)
```

Methods:

- <code title="get /api/institution/{name}/holdings">client.institutions.holdings.<a href="./src/tradesignals/resources/institutions/holdings.py">list</a>(name, \*\*<a href="src/tradesignals/types/institutions/holding_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institutions/holding_list_response.py">Optional</a></code>

## Sectors

Types:

```python
from tradesignals.types.institutions import (
    SectorExposure,
    SectorExposureResponse,
    SectorListResponse,
)
```

Methods:

- <code title="get /api/institution/{name}/sectors">client.institutions.sectors.<a href="./src/tradesignals/resources/institutions/sectors.py">list</a>(name, \*\*<a href="src/tradesignals/types/institutions/sector_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institutions/sector_list_response.py">Optional</a></code>

## Ownership

Types:

```python
from tradesignals.types.institutions import (
    InstitutionOwnership,
    InstitutionOwnershipResponse,
    OwnershipListResponse,
)
```

Methods:

- <code title="get /api/institution/{ticker}/ownership">client.institutions.ownership.<a href="./src/tradesignals/resources/institutions/ownership.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/institutions/ownership_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institutions/ownership_list_response.py">Optional</a></code>

# Earnings

## Afterhours

Types:

```python
from tradesignals.types.earnings import (
    AfterhoursEarningsData,
    AfterhoursEarningsResponse,
    AfterhourListResponse,
)
```

Methods:

- <code title="get /api/earnings/afterhours">client.earnings.afterhours.<a href="./src/tradesignals/resources/earnings/afterhours.py">list</a>(\*\*<a href="src/tradesignals/types/earnings/afterhour_list_params.py">params</a>) -> <a href="./src/tradesignals/types/earnings/afterhour_list_response.py">Optional</a></code>

## Premarket

Types:

```python
from tradesignals.types.earnings import (
    PremarketEarningsData,
    PremarketEarningsResponse,
    PremarketListResponse,
)
```

Methods:

- <code title="get /api/earnings/premarket">client.earnings.premarket.<a href="./src/tradesignals/resources/earnings/premarket.py">list</a>(\*\*<a href="src/tradesignals/types/earnings/premarket_list_params.py">params</a>) -> <a href="./src/tradesignals/types/earnings/premarket_list_response.py">Optional</a></code>

## PastTicker

Types:

```python
from tradesignals.types.earnings import HistoricalEarningsData, HistoricalEarningsResponse
```

Methods:

- <code title="get /api/earnings/{ticker}">client.earnings.past_ticker.<a href="./src/tradesignals/resources/earnings/past_ticker.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/earnings/historical_earnings_response.py">HistoricalEarningsResponse</a></code>

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
