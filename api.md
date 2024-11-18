# Stock

## OiChange

Types:

```python
from tradesignals.types.stock import StockOiChange, StockOiChangeResponse
```

Methods:

- <code title="get /api/stock/{ticker}/oi-change">client.stock.oi_change.<a href="./src/tradesignals/resources/stock/oi_change.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/stock/oi_change_list_params.py">params</a>) -> <a href="./src/tradesignals/types/stock/stock_oi_change_response.py">StockOiChangeResponse</a></code>

## FlowPerStrikeIntraday

Types:

```python
from tradesignals.types.stock import FlowPerStrikeIntradayEntry, FlowPerStrikeIntradayResponse
```

Methods:

- <code title="get /api/stock/{ticker}/flow-per-strike-intraday">client.stock.flow_per_strike_intraday.<a href="./src/tradesignals/resources/stock/flow_per_strike_intraday.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/stock/flow_per_strike_intraday_list_params.py">params</a>) -> <a href="./src/tradesignals/types/stock/flow_per_strike_intraday_response.py">FlowPerStrikeIntradayResponse</a></code>

## FlowPerStrike

Types:

```python
from tradesignals.types.stock import FlowPerStrike, FlowPerStrikeResponse
```

Methods:

- <code title="get /api/stock/{ticker}/flow-per-strike">client.stock.flow_per_strike.<a href="./src/tradesignals/resources/stock/flow_per_strike.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/stock/flow_per_strike_list_params.py">params</a>) -> <a href="./src/tradesignals/types/stock/flow_per_strike_response.py">FlowPerStrikeResponse</a></code>

## FlowByExpiry

Types:

```python
from tradesignals.types.stock import (
    ExpirationOrderFlow,
    ExpirationOrderFlowResponse,
    FlowByExpiryListResponse,
)
```

Methods:

- <code title="get /api/stock/{ticker}/flow-per-expiry">client.stock.flow_by_expiry.<a href="./src/tradesignals/resources/stock/flow_by_expiry.py">list</a>(ticker) -> <a href="./src/tradesignals/types/stock/flow_by_expiry_list_response.py">Optional</a></code>

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

# Analyst

## Ratings

Types:

```python
from tradesignals.types.analyst import AnalystRatingEntry, AnalystRatingResponse, RatingListResponse
```

Methods:

- <code title="get /api/screener/analysts">client.analyst.ratings.<a href="./src/tradesignals/resources/analyst/ratings.py">list</a>(\*\*<a href="src/tradesignals/types/analyst/rating_list_params.py">params</a>) -> <a href="./src/tradesignals/types/analyst/rating_list_response.py">Optional</a></code>

# Seasonality

## MonthlySeasonality

Types:

```python
from tradesignals.types.seasonality import (
    MonthlyAverageEntry,
    MonthlyAverageResponse,
    MonthlySeasonalityListResponse,
)
```

Methods:

- <code title="get /api/seasonality/{ticker}/monthly">client.seasonality.monthly_seasonality.<a href="./src/tradesignals/resources/seasonality/monthly_seasonality.py">list</a>(ticker) -> <a href="./src/tradesignals/types/seasonality/monthly_seasonality_list_response.py">Optional</a></code>

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

# Screener

## StockScreener

Types:

```python
from tradesignals.types.screener import StockEntry, StockScreenerResponse, StockScreenerListResponse
```

Methods:

- <code title="get /api/screener/stocks">client.screener.stock_screener.<a href="./src/tradesignals/resources/screener/stock_screener.py">list</a>(\*\*<a href="src/tradesignals/types/screener/stock_screener_list_params.py">params</a>) -> <a href="./src/tradesignals/types/screener/stock_screener_list_response.py">Optional</a></code>

## OptionScreener

Types:

```python
from tradesignals.types.screener import (
    HottestChainEntry,
    HottestChainsResponse,
    OptionScreenerListResponse,
)
```

Methods:

- <code title="get /api/screener/option-contracts">client.screener.option_screener.<a href="./src/tradesignals/resources/screener/option_screener.py">list</a>(\*\*<a href="src/tradesignals/types/screener/option_screener_list_params.py">params</a>) -> <a href="./src/tradesignals/types/screener/option_screener_list_response.py">Optional</a></code>

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

## OptionTradeVolume

Types:

```python
from tradesignals.types.market import (
    OptionTradeVolume,
    OptionTradeVolumeResponse,
    OptionTradeVolumeListResponse,
)
```

Methods:

- <code title="get /api/market/total-options-volume">client.market.option_trade_volume.<a href="./src/tradesignals/resources/market/option_trade_volume.py">list</a>(\*\*<a href="src/tradesignals/types/market/option_trade_volume_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/option_trade_volume_list_response.py">Optional</a></code>

## EtfTide

Types:

```python
from tradesignals.types.market import EtfTide, EtfTideResponse, EtfTideListResponse
```

Methods:

- <code title="get /api/market/{ticker}/etf-tide">client.market.etf_tide.<a href="./src/tradesignals/resources/market/etf_tide.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/market/etf_tide_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/etf_tide_list_response.py">Optional</a></code>

## MarketTide

Types:

```python
from tradesignals.types.market import MarketTide, MarketTideResponse, MarketTideListResponse
```

Methods:

- <code title="get /api/market/market-tide">client.market.market_tide.<a href="./src/tradesignals/resources/market/market_tide.py">list</a>(\*\*<a href="src/tradesignals/types/market/market_tide_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/market_tide_list_response.py">Optional</a></code>

## OiChange

Types:

```python
from tradesignals.types.market import OiChange, OiChangeResponse, OiChangeListResponse
```

Methods:

- <code title="get /api/market/oi-change">client.market.oi_change.<a href="./src/tradesignals/resources/market/oi_change.py">list</a>(\*\*<a href="src/tradesignals/types/market/oi_change_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/oi_change_list_response.py">Optional</a></code>

## InsiderTrades

Types:

```python
from tradesignals.types.market import InsiderTrade, InsiderTradeResponse, InsiderTradeListResponse
```

Methods:

- <code title="get /api/market/insider-buy-sells">client.market.insider_trades.<a href="./src/tradesignals/resources/market/insider_trades.py">list</a>(\*\*<a href="src/tradesignals/types/market/insider_trade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/insider_trade_list_response.py">Optional</a></code>

## Correlation

Types:

```python
from tradesignals.types.market import Correlation, CorrelationsResponse, CorrelationListResponse
```

Methods:

- <code title="get /api/market/correlations">client.market.correlation.<a href="./src/tradesignals/resources/market/correlation.py">list</a>(\*\*<a href="src/tradesignals/types/market/correlation_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/correlation_list_response.py">Optional</a></code>

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

# Institution

## InstitutionList

Types:

```python
from tradesignals.types.institution import (
    Institution,
    InstitutionListResponse,
    InstitutionListListResponse,
)
```

Methods:

- <code title="get /api/institutions">client.institution.institution_list.<a href="./src/tradesignals/resources/institution/institution_list.py">list</a>(\*\*<a href="src/tradesignals/types/institution/institution_list_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institution/institution_list_list_response.py">Optional</a></code>

## Activity

Types:

```python
from tradesignals.types.institution import Activity, ActivityResponse, ActivityListResponse
```

Methods:

- <code title="get /api/institution/{name}/activity">client.institution.activity.<a href="./src/tradesignals/resources/institution/activity.py">list</a>(name, \*\*<a href="src/tradesignals/types/institution/activity_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institution/activity_list_response.py">Optional</a></code>

## Holdings

Types:

```python
from tradesignals.types.institution import Holdings, HoldingsResponse, HoldingListResponse
```

Methods:

- <code title="get /api/institution/{name}/holdings">client.institution.holdings.<a href="./src/tradesignals/resources/institution/holdings.py">list</a>(name, \*\*<a href="src/tradesignals/types/institution/holding_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institution/holding_list_response.py">Optional</a></code>

## SectorExposure

Types:

```python
from tradesignals.types.institution import (
    SectorExposure,
    SectorExposureResponse,
    SectorExposureListResponse,
)
```

Methods:

- <code title="get /api/institution/{name}/sectors">client.institution.sector_exposure.<a href="./src/tradesignals/resources/institution/sector_exposure.py">list</a>(name, \*\*<a href="src/tradesignals/types/institution/sector_exposure_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institution/sector_exposure_list_response.py">Optional</a></code>

## StockOwnership

Types:

```python
from tradesignals.types.institution import (
    StockOwnership,
    StockOwnershipResponse,
    StockOwnershipListResponse,
)
```

Methods:

- <code title="get /api/institution/{ticker}/ownership">client.institution.stock_ownership.<a href="./src/tradesignals/resources/institution/stock_ownership.py">list</a>(ticker, \*\*<a href="src/tradesignals/types/institution/stock_ownership_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institution/stock_ownership_list_response.py">Optional</a></code>

# Earnings

## AfterhoursEarnings

Types:

```python
from tradesignals.types.earnings import (
    AfterhoursEarningsData,
    AfterhoursEarningsResponse,
    AfterhoursEarningListResponse,
)
```

Methods:

- <code title="get /api/earnings/afterhours">client.earnings.afterhours_earnings.<a href="./src/tradesignals/resources/earnings/afterhours_earnings.py">list</a>(\*\*<a href="src/tradesignals/types/earnings/afterhours_earning_list_params.py">params</a>) -> <a href="./src/tradesignals/types/earnings/afterhours_earning_list_response.py">Optional</a></code>

## PremarketEarnings

Types:

```python
from tradesignals.types.earnings import (
    PremarketEarningsData,
    PremarketEarningsResponse,
    PremarketEarningListResponse,
)
```

Methods:

- <code title="get /api/earnings/premarket">client.earnings.premarket_earnings.<a href="./src/tradesignals/resources/earnings/premarket_earnings.py">list</a>(\*\*<a href="src/tradesignals/types/earnings/premarket_earning_list_params.py">params</a>) -> <a href="./src/tradesignals/types/earnings/premarket_earning_list_response.py">Optional</a></code>

## HistoricalEarnings

Types:

```python
from tradesignals.types.earnings import HistoricalEarningsData, HistoricalEarningsResponse
```

Methods:

- <code title="get /api/earnings/{ticker}">client.earnings.historical_earnings.<a href="./src/tradesignals/resources/earnings/historical_earnings.py">retrieve</a>(ticker) -> <a href="./src/tradesignals/types/earnings/historical_earnings_response.py">HistoricalEarningsResponse</a></code>

# Congress

## RecentTrades

Types:

```python
from tradesignals.types.congress import CongressionalTrade, RecentTradeListResponse
```

Methods:

- <code title="get /api/congress/recent-trades">client.congress.recent_trades.<a href="./src/tradesignals/resources/congress/recent_trades.py">list</a>(\*\*<a href="src/tradesignals/types/congress/recent_trade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/recent_trade_list_response.py">Optional</a></code>

## TradesReportedLate

Types:

```python
from tradesignals.types.congress import LateCongressionalReport, TradesReportedLateListResponse
```

Methods:

- <code title="get /api/congress/late-reports">client.congress.trades_reported_late.<a href="./src/tradesignals/resources/congress/trades_reported_late.py">list</a>(\*\*<a href="src/tradesignals/types/congress/trades_reported_late_list_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/trades_reported_late_list_response.py">Optional</a></code>

## TradesByMember

Types:

```python
from tradesignals.types.congress import CongressionalTraderReport
```

Methods:

- <code title="get /api/congress/congress-trader">client.congress.trades_by_member.<a href="./src/tradesignals/resources/congress/trades_by_member.py">retrieve</a>(\*\*<a href="src/tradesignals/types/congress/trades_by_member_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/congressional_trader_report.py">CongressionalTraderReport</a></code>

## RecentReports

Types:

```python
from tradesignals.types.congress import RecentCongressionalReport, RecentReportListResponse
```

Methods:

- <code title="get /api/congress/recent-reports">client.congress.recent_reports.<a href="./src/tradesignals/resources/congress/recent_reports.py">list</a>(\*\*<a href="src/tradesignals/types/congress/recent_report_list_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/recent_report_list_response.py">Optional</a></code>

# IndustryGroup

## GreekFlow

Types:

```python
from tradesignals.types.industry_group import GroupGreekFlow, GreekFlowListResponse
```

Methods:

- <code title="get /api/group-flow/{flow_group}/greek-flow">client.industry_group.greek_flow.<a href="./src/tradesignals/resources/industry_group/greek_flow.py">list</a>(flow_group, \*\*<a href="src/tradesignals/types/industry_group/greek_flow_list_params.py">params</a>) -> <a href="./src/tradesignals/types/industry_group/greek_flow_list_response.py">Optional</a></code>

## GreekFlowByExpiry

Types:

```python
from tradesignals.types.industry_group import GroupFlowsResponse, GreekFlowByExpiryListResponse
```

Methods:

- <code title="get /api/group-flow/{flow_group}/greek-flow/{expiry}">client.industry_group.greek_flow_by_expiry.<a href="./src/tradesignals/resources/industry_group/greek_flow_by_expiry.py">list</a>(expiry, \*, flow_group, \*\*<a href="src/tradesignals/types/industry_group/greek_flow_by_expiry_list_params.py">params</a>) -> <a href="./src/tradesignals/types/industry_group/greek_flow_by_expiry_list_response.py">Optional</a></code>

# Etf

## Holdings

Types:

```python
from tradesignals.types.etf import EtfHolding, HoldingListResponse
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
