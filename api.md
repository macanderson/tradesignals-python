# OptionsFlows

Types:

```python
from tradesignals.types import OptionsFlowRetrieveResponse, OptionsFlowListResponse
```

Methods:

- <code title="get /api/options/flow/{symbol}">client.options_flows.<a href="./src/tradesignals/resources/options_flows.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/options_flow_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/options_flow_retrieve_response.py">object</a></code>
- <code title="get /api/options/flow">client.options_flows.<a href="./src/tradesignals/resources/options_flows.py">list</a>(\*\*<a href="src/tradesignals/types/options_flow_list_params.py">params</a>) -> <a href="./src/tradesignals/types/options_flow_list_response.py">object</a></code>

# OptionsGreekFlows

Types:

```python
from tradesignals.types import OptionsGreekFlowListResponse
```

Methods:

- <code title="get /api/options/greekflow">client.options_greek_flows.<a href="./src/tradesignals/resources/options_greek_flows/options_greek_flows.py">list</a>(\*\*<a href="src/tradesignals/types/options_greek_flow_list_params.py">params</a>) -> <a href="./src/tradesignals/types/options_greek_flow_list_response.py">object</a></code>

## Expiry

Types:

```python
from tradesignals.types.options_greek_flows import ExpiryListResponse
```

Methods:

- <code title="get /api/options/greekflow/expiry">client.options_greek_flows.expiry.<a href="./src/tradesignals/resources/options_greek_flows/expiry.py">list</a>(\*\*<a href="src/tradesignals/types/options_greek_flows/expiry_list_params.py">params</a>) -> <a href="./src/tradesignals/types/options_greek_flows/expiry_list_response.py">object</a></code>

# OptionsOpenInterestChanges

Types:

```python
from tradesignals.types import OptionsOpenInterestChangeRetrieveResponse
```

Methods:

- <code title="get /api/options/oi_change/{symbol}">client.options_open_interest_changes.<a href="./src/tradesignals/resources/options_open_interest_changes.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/options_open_interest_change_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/options_open_interest_change_retrieve_response.py">object</a></code>

# InstitutionalActivities

Types:

```python
from tradesignals.types import InstitutionalActivityListResponse
```

Methods:

- <code title="get /api/institutional/activity">client.institutional_activities.<a href="./src/tradesignals/resources/institutional_activities.py">list</a>(\*\*<a href="src/tradesignals/types/institutional_activity_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institutional_activity_list_response.py">object</a></code>

# InsiderTrades

Types:

```python
from tradesignals.types import InsiderTradeListResponse
```

Methods:

- <code title="get /api/insider/trades">client.insider_trades.<a href="./src/tradesignals/resources/insider_trades.py">list</a>(\*\*<a href="src/tradesignals/types/insider_trade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/insider_trade_list_response.py">object</a></code>

# SpikeDetections

Types:

```python
from tradesignals.types import SpikeDetectionListResponse
```

Methods:

- <code title="get /api/spike/detection">client.spike_detections.<a href="./src/tradesignals/resources/spike_detections.py">list</a>(\*\*<a href="src/tradesignals/types/spike_detection_list_params.py">params</a>) -> <a href="./src/tradesignals/types/spike_detection_list_response.py">object</a></code>

# OptionsTotalVolumes

Types:

```python
from tradesignals.types import OptionsTotalVolumeListResponse
```

Methods:

- <code title="get /api/options/total_volume">client.options_total_volumes.<a href="./src/tradesignals/resources/options_total_volumes.py">list</a>(\*\*<a href="src/tradesignals/types/options_total_volume_list_params.py">params</a>) -> <a href="./src/tradesignals/types/options_total_volume_list_response.py">object</a></code>

# EconomicCalendars

Types:

```python
from tradesignals.types import EconomicCalendarListResponse
```

Methods:

- <code title="get /api/calendar/economic">client.economic_calendars.<a href="./src/tradesignals/resources/economic_calendars.py">list</a>(\*\*<a href="src/tradesignals/types/economic_calendar_list_params.py">params</a>) -> <a href="./src/tradesignals/types/economic_calendar_list_response.py">object</a></code>

# Calendar

Types:

```python
from tradesignals.types import CalendarRetrieveResponse
```

Methods:

- <code title="get /api/calendar/fda">client.calendar.<a href="./src/tradesignals/resources/calendar.py">retrieve</a>(\*\*<a href="src/tradesignals/types/calendar_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/calendar_retrieve_response.py">object</a></code>

# Correlations

Types:

```python
from tradesignals.types import CorrelationRetrieveResponse
```

Methods:

- <code title="get /api/correlations">client.correlations.<a href="./src/tradesignals/resources/correlations.py">retrieve</a>(\*\*<a href="src/tradesignals/types/correlation_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/correlation_retrieve_response.py">object</a></code>

# Etf

Types:

```python
from tradesignals.types import EtfListResponse
```

Methods:

- <code title="get /api/etf/list">client.etf.<a href="./src/tradesignals/resources/etf/etf.py">list</a>() -> <a href="./src/tradesignals/types/etf_list_response.py">object</a></code>

## Tide

Types:

```python
from tradesignals.types.etf import TideRetrieveResponse
```

Methods:

- <code title="get /api/etf/tide">client.etf.tide.<a href="./src/tradesignals/resources/etf/tide.py">retrieve</a>(\*\*<a href="src/tradesignals/types/etf/tide_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/etf/tide_retrieve_response.py">object</a></code>

## Sectors

Types:

```python
from tradesignals.types.etf import SectorRetrieveResponse, SectorListResponse
```

Methods:

- <code title="get /api/etf/sectors">client.etf.sectors.<a href="./src/tradesignals/resources/etf/sectors.py">retrieve</a>(\*\*<a href="src/tradesignals/types/etf/sector_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/etf/sector_retrieve_response.py">object</a></code>
- <code title="get /api/etf/sectors/list">client.etf.sectors.<a href="./src/tradesignals/resources/etf/sectors.py">list</a>() -> <a href="./src/tradesignals/types/etf/sector_list_response.py">object</a></code>

## Holdings

Types:

```python
from tradesignals.types.etf import HoldingListResponse
```

Methods:

- <code title="get /api/etf/holdings">client.etf.holdings.<a href="./src/tradesignals/resources/etf/holdings.py">list</a>(\*\*<a href="src/tradesignals/types/etf/holding_list_params.py">params</a>) -> <a href="./src/tradesignals/types/etf/holding_list_response.py">object</a></code>

# Options

## Chain

Types:

```python
from tradesignals.types.options import ChainRetrieveResponse
```

Methods:

- <code title="get /api/options/chain/{symbol}">client.options.chain.<a href="./src/tradesignals/resources/options/chain.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/options/chain_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/options/chain_retrieve_response.py">object</a></code>

## Expirations

Types:

```python
from tradesignals.types.options import ExpirationRetrieveResponse
```

Methods:

- <code title="get /api/options/expirations/{symbol}">client.options.expirations.<a href="./src/tradesignals/resources/options/expirations.py">retrieve</a>(symbol) -> <a href="./src/tradesignals/types/options/expiration_retrieve_response.py">object</a></code>

## Greeks

Types:

```python
from tradesignals.types.options import GreekRetrieveResponse
```

Methods:

- <code title="get /api/options/greeks/{symbol}">client.options.greeks.<a href="./src/tradesignals/resources/options/greeks.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/options/greek_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/options/greek_retrieve_response.py">object</a></code>

## Historical

Types:

```python
from tradesignals.types.options import HistoricalRetrieveResponse
```

Methods:

- <code title="get /api/options/historical/{symbol}">client.options.historical.<a href="./src/tradesignals/resources/options/historical.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/options/historical_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/options/historical_retrieve_response.py">object</a></code>

## Contract

Types:

```python
from tradesignals.types.options import ContractRetrieveResponse
```

Methods:

- <code title="get /api/options/contract/{optionSymbol}">client.options.contract.<a href="./src/tradesignals/resources/options/contract.py">retrieve</a>(option_symbol) -> <a href="./src/tradesignals/types/options/contract_retrieve_response.py">object</a></code>

## Contracts

Types:

```python
from tradesignals.types.options import ContractListResponse
```

Methods:

- <code title="get /api/options/contracts">client.options.contracts.<a href="./src/tradesignals/resources/options/contracts.py">list</a>(\*\*<a href="src/tradesignals/types/options/contract_list_params.py">params</a>) -> <a href="./src/tradesignals/types/options/contract_list_response.py">object</a></code>

# Stocks

## Price

Types:

```python
from tradesignals.types.stocks import PriceRetrieveResponse
```

Methods:

- <code title="get /api/stocks/price/{symbol}">client.stocks.price.<a href="./src/tradesignals/resources/stocks/price.py">retrieve</a>(symbol) -> <a href="./src/tradesignals/types/stocks/price_retrieve_response.py">object</a></code>

## Quote

Types:

```python
from tradesignals.types.stocks import QuoteRetrieveResponse
```

Methods:

- <code title="get /api/stocks/quote/{symbol}">client.stocks.quote.<a href="./src/tradesignals/resources/stocks/quote.py">retrieve</a>(symbol) -> <a href="./src/tradesignals/types/stocks/quote_retrieve_response.py">object</a></code>

## Historical

Types:

```python
from tradesignals.types.stocks import HistoricalRetrieveResponse
```

Methods:

- <code title="get /api/stocks/historical/{symbol}">client.stocks.historical.<a href="./src/tradesignals/resources/stocks/historical.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/stocks/historical_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/stocks/historical_retrieve_response.py">object</a></code>

## Company

Types:

```python
from tradesignals.types.stocks import CompanyRetrieveResponse
```

Methods:

- <code title="get /api/stocks/company/{symbol}">client.stocks.company.<a href="./src/tradesignals/resources/stocks/company.py">retrieve</a>(symbol) -> <a href="./src/tradesignals/types/stocks/company_retrieve_response.py">object</a></code>

## Financials

Types:

```python
from tradesignals.types.stocks import FinancialRetrieveResponse
```

Methods:

- <code title="get /api/stocks/financials/{symbol}">client.stocks.financials.<a href="./src/tradesignals/resources/stocks/financials.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/stocks/financial_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/stocks/financial_retrieve_response.py">object</a></code>

## Earnings

Types:

```python
from tradesignals.types.stocks import EarningRetrieveResponse
```

Methods:

- <code title="get /api/stocks/earnings/{symbol}">client.stocks.earnings.<a href="./src/tradesignals/resources/stocks/earnings.py">retrieve</a>(symbol) -> <a href="./src/tradesignals/types/stocks/earning_retrieve_response.py">object</a></code>

## Dividends

Types:

```python
from tradesignals.types.stocks import DividendRetrieveResponse
```

Methods:

- <code title="get /api/stocks/dividends/{symbol}">client.stocks.dividends.<a href="./src/tradesignals/resources/stocks/dividends.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/stocks/dividend_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/stocks/dividend_retrieve_response.py">object</a></code>

## Screener

Types:

```python
from tradesignals.types.stocks import ScreenerRetrieveResponse
```

Methods:

- <code title="get /api/stocks/screener">client.stocks.screener.<a href="./src/tradesignals/resources/stocks/screener.py">retrieve</a>(\*\*<a href="src/tradesignals/types/stocks/screener_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/stocks/screener_retrieve_response.py">object</a></code>

# News

Types:

```python
from tradesignals.types import NewsListResponse
```

Methods:

- <code title="get /api/news">client.news.<a href="./src/tradesignals/resources/news.py">list</a>(\*\*<a href="src/tradesignals/types/news_list_params.py">params</a>) -> <a href="./src/tradesignals/types/news_list_response.py">object</a></code>

# Congress

## Trades

Types:

```python
from tradesignals.types.congress import TradeListResponse
```

Methods:

- <code title="get /api/congress/trades">client.congress.trades.<a href="./src/tradesignals/resources/congress/trades.py">list</a>(\*\*<a href="src/tradesignals/types/congress/trade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/congress/trade_list_response.py">object</a></code>

## Members

Types:

```python
from tradesignals.types.congress import MemberListResponse
```

Methods:

- <code title="get /api/congress/members">client.congress.members.<a href="./src/tradesignals/resources/congress/members.py">list</a>() -> <a href="./src/tradesignals/types/congress/member_list_response.py">object</a></code>

# Institutions

Types:

```python
from tradesignals.types import InstitutionListResponse
```

Methods:

- <code title="get /api/institutions/list">client.institutions.<a href="./src/tradesignals/resources/institutions/institutions.py">list</a>() -> <a href="./src/tradesignals/types/institution_list_response.py">object</a></code>

## Trades

Types:

```python
from tradesignals.types.institutions import TradeListResponse
```

Methods:

- <code title="get /api/institutions/trades">client.institutions.trades.<a href="./src/tradesignals/resources/institutions/trades.py">list</a>(\*\*<a href="src/tradesignals/types/institutions/trade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/institutions/trade_list_response.py">object</a></code>

# Darkpool

## Transactions

Types:

```python
from tradesignals.types.darkpool import TransactionRetrieveResponse, TransactionListResponse
```

Methods:

- <code title="get /api/darkpool/transactions/{symbol}">client.darkpool.transactions.<a href="./src/tradesignals/resources/darkpool/transactions.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/darkpool/transaction_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/darkpool/transaction_retrieve_response.py">object</a></code>
- <code title="get /api/darkpool/transactions">client.darkpool.transactions.<a href="./src/tradesignals/resources/darkpool/transactions.py">list</a>(\*\*<a href="src/tradesignals/types/darkpool/transaction_list_params.py">params</a>) -> <a href="./src/tradesignals/types/darkpool/transaction_list_response.py">object</a></code>

# Seasonality

## Stocks

Types:

```python
from tradesignals.types.seasonality import StockRetrieveResponse
```

Methods:

- <code title="get /api/seasonality/stocks/{symbol}">client.seasonality.stocks.<a href="./src/tradesignals/resources/seasonality/stocks.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/seasonality/stock_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/seasonality/stock_retrieve_response.py">object</a></code>

# Analyst

## Ratings

Types:

```python
from tradesignals.types.analyst import RatingRetrieveResponse
```

Methods:

- <code title="get /api/analyst/ratings/{symbol}">client.analyst.ratings.<a href="./src/tradesignals/resources/analyst/ratings.py">retrieve</a>(symbol, \*\*<a href="src/tradesignals/types/analyst/rating_retrieve_params.py">params</a>) -> <a href="./src/tradesignals/types/analyst/rating_retrieve_response.py">object</a></code>

## UpgradesDowngrades

Types:

```python
from tradesignals.types.analyst import UpgradesDowngradeListResponse
```

Methods:

- <code title="get /api/analyst/upgrades_downgrades">client.analyst.upgrades_downgrades.<a href="./src/tradesignals/resources/analyst/upgrades_downgrades.py">list</a>(\*\*<a href="src/tradesignals/types/analyst/upgrades_downgrade_list_params.py">params</a>) -> <a href="./src/tradesignals/types/analyst/upgrades_downgrade_list_response.py">object</a></code>

# Market

## Overview

Types:

```python
from tradesignals.types.market import OverviewRetrieveResponse
```

Methods:

- <code title="get /api/market/overview">client.market.overview.<a href="./src/tradesignals/resources/market/overview.py">retrieve</a>() -> <a href="./src/tradesignals/types/market/overview_retrieve_response.py">object</a></code>

## Indices

Types:

```python
from tradesignals.types.market import IndexListResponse
```

Methods:

- <code title="get /api/market/indices">client.market.indices.<a href="./src/tradesignals/resources/market/indices.py">list</a>() -> <a href="./src/tradesignals/types/market/index_list_response.py">object</a></code>

## Movers

Types:

```python
from tradesignals.types.market import MoverListResponse
```

Methods:

- <code title="get /api/market/movers">client.market.movers.<a href="./src/tradesignals/resources/market/movers.py">list</a>(\*\*<a href="src/tradesignals/types/market/mover_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/mover_list_response.py">object</a></code>

## Sectors

Types:

```python
from tradesignals.types.market import SectorListResponse
```

Methods:

- <code title="get /api/market/sectors">client.market.sectors.<a href="./src/tradesignals/resources/market/sectors.py">list</a>(\*\*<a href="src/tradesignals/types/market/sector_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/sector_list_response.py">object</a></code>

## News

Types:

```python
from tradesignals.types.market import NewsListResponse
```

Methods:

- <code title="get /api/market/news">client.market.news.<a href="./src/tradesignals/resources/market/news.py">list</a>(\*\*<a href="src/tradesignals/types/market/news_list_params.py">params</a>) -> <a href="./src/tradesignals/types/market/news_list_response.py">object</a></code>
