# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .spike import (
    SpikeResource,
    AsyncSpikeResource,
    SpikeResourceWithRawResponse,
    AsyncSpikeResourceWithRawResponse,
    SpikeResourceWithStreamingResponse,
    AsyncSpikeResourceWithStreamingResponse,
)
from .etf_tide import (
    EtfTideResource,
    AsyncEtfTideResource,
    EtfTideResourceWithRawResponse,
    AsyncEtfTideResourceWithRawResponse,
    EtfTideResourceWithStreamingResponse,
    AsyncEtfTideResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .oi_change import (
    OiChangeResource,
    AsyncOiChangeResource,
    OiChangeResourceWithRawResponse,
    AsyncOiChangeResourceWithRawResponse,
    OiChangeResourceWithStreamingResponse,
    AsyncOiChangeResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .correlation import (
    CorrelationResource,
    AsyncCorrelationResource,
    CorrelationResourceWithRawResponse,
    AsyncCorrelationResourceWithRawResponse,
    CorrelationResourceWithStreamingResponse,
    AsyncCorrelationResourceWithStreamingResponse,
)
from .market_tide import (
    MarketTideResource,
    AsyncMarketTideResource,
    MarketTideResourceWithRawResponse,
    AsyncMarketTideResourceWithRawResponse,
    MarketTideResourceWithStreamingResponse,
    AsyncMarketTideResourceWithStreamingResponse,
)
from .sector_etfs import (
    SectorEtfsResource,
    AsyncSectorEtfsResource,
    SectorEtfsResourceWithRawResponse,
    AsyncSectorEtfsResourceWithRawResponse,
    SectorEtfsResourceWithStreamingResponse,
    AsyncSectorEtfsResourceWithStreamingResponse,
)
from .fda_calendar import (
    FdaCalendarResource,
    AsyncFdaCalendarResource,
    FdaCalendarResourceWithRawResponse,
    AsyncFdaCalendarResourceWithRawResponse,
    FdaCalendarResourceWithStreamingResponse,
    AsyncFdaCalendarResourceWithStreamingResponse,
)
from .insider_trades import (
    InsiderTradesResource,
    AsyncInsiderTradesResource,
    InsiderTradesResourceWithRawResponse,
    AsyncInsiderTradesResourceWithRawResponse,
    InsiderTradesResourceWithStreamingResponse,
    AsyncInsiderTradesResourceWithStreamingResponse,
)
from .economic_calendar import (
    EconomicCalendarResource,
    AsyncEconomicCalendarResource,
    EconomicCalendarResourceWithRawResponse,
    AsyncEconomicCalendarResourceWithRawResponse,
    EconomicCalendarResourceWithStreamingResponse,
    AsyncEconomicCalendarResourceWithStreamingResponse,
)
from .option_trade_volume import (
    OptionTradeVolumeResource,
    AsyncOptionTradeVolumeResource,
    OptionTradeVolumeResourceWithRawResponse,
    AsyncOptionTradeVolumeResourceWithRawResponse,
    OptionTradeVolumeResourceWithStreamingResponse,
    AsyncOptionTradeVolumeResourceWithStreamingResponse,
)

__all__ = ["MarketResource", "AsyncMarketResource"]


class MarketResource(SyncAPIResource):
    @cached_property
    def sector_etfs(self) -> SectorEtfsResource:
        return SectorEtfsResource(self._client)

    @cached_property
    def spike(self) -> SpikeResource:
        return SpikeResource(self._client)

    @cached_property
    def option_trade_volume(self) -> OptionTradeVolumeResource:
        return OptionTradeVolumeResource(self._client)

    @cached_property
    def etf_tide(self) -> EtfTideResource:
        return EtfTideResource(self._client)

    @cached_property
    def market_tide(self) -> MarketTideResource:
        return MarketTideResource(self._client)

    @cached_property
    def oi_change(self) -> OiChangeResource:
        return OiChangeResource(self._client)

    @cached_property
    def insider_trades(self) -> InsiderTradesResource:
        return InsiderTradesResource(self._client)

    @cached_property
    def correlation(self) -> CorrelationResource:
        return CorrelationResource(self._client)

    @cached_property
    def economic_calendar(self) -> EconomicCalendarResource:
        return EconomicCalendarResource(self._client)

    @cached_property
    def fda_calendar(self) -> FdaCalendarResource:
        return FdaCalendarResource(self._client)

    @cached_property
    def with_raw_response(self) -> MarketResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return MarketResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return MarketResourceWithStreamingResponse(self)


class AsyncMarketResource(AsyncAPIResource):
    @cached_property
    def sector_etfs(self) -> AsyncSectorEtfsResource:
        return AsyncSectorEtfsResource(self._client)

    @cached_property
    def spike(self) -> AsyncSpikeResource:
        return AsyncSpikeResource(self._client)

    @cached_property
    def option_trade_volume(self) -> AsyncOptionTradeVolumeResource:
        return AsyncOptionTradeVolumeResource(self._client)

    @cached_property
    def etf_tide(self) -> AsyncEtfTideResource:
        return AsyncEtfTideResource(self._client)

    @cached_property
    def market_tide(self) -> AsyncMarketTideResource:
        return AsyncMarketTideResource(self._client)

    @cached_property
    def oi_change(self) -> AsyncOiChangeResource:
        return AsyncOiChangeResource(self._client)

    @cached_property
    def insider_trades(self) -> AsyncInsiderTradesResource:
        return AsyncInsiderTradesResource(self._client)

    @cached_property
    def correlation(self) -> AsyncCorrelationResource:
        return AsyncCorrelationResource(self._client)

    @cached_property
    def economic_calendar(self) -> AsyncEconomicCalendarResource:
        return AsyncEconomicCalendarResource(self._client)

    @cached_property
    def fda_calendar(self) -> AsyncFdaCalendarResource:
        return AsyncFdaCalendarResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMarketResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncMarketResourceWithStreamingResponse(self)


class MarketResourceWithRawResponse:
    def __init__(self, market: MarketResource) -> None:
        self._market = market

    @cached_property
    def sector_etfs(self) -> SectorEtfsResourceWithRawResponse:
        return SectorEtfsResourceWithRawResponse(self._market.sector_etfs)

    @cached_property
    def spike(self) -> SpikeResourceWithRawResponse:
        return SpikeResourceWithRawResponse(self._market.spike)

    @cached_property
    def option_trade_volume(self) -> OptionTradeVolumeResourceWithRawResponse:
        return OptionTradeVolumeResourceWithRawResponse(self._market.option_trade_volume)

    @cached_property
    def etf_tide(self) -> EtfTideResourceWithRawResponse:
        return EtfTideResourceWithRawResponse(self._market.etf_tide)

    @cached_property
    def market_tide(self) -> MarketTideResourceWithRawResponse:
        return MarketTideResourceWithRawResponse(self._market.market_tide)

    @cached_property
    def oi_change(self) -> OiChangeResourceWithRawResponse:
        return OiChangeResourceWithRawResponse(self._market.oi_change)

    @cached_property
    def insider_trades(self) -> InsiderTradesResourceWithRawResponse:
        return InsiderTradesResourceWithRawResponse(self._market.insider_trades)

    @cached_property
    def correlation(self) -> CorrelationResourceWithRawResponse:
        return CorrelationResourceWithRawResponse(self._market.correlation)

    @cached_property
    def economic_calendar(self) -> EconomicCalendarResourceWithRawResponse:
        return EconomicCalendarResourceWithRawResponse(self._market.economic_calendar)

    @cached_property
    def fda_calendar(self) -> FdaCalendarResourceWithRawResponse:
        return FdaCalendarResourceWithRawResponse(self._market.fda_calendar)


class AsyncMarketResourceWithRawResponse:
    def __init__(self, market: AsyncMarketResource) -> None:
        self._market = market

    @cached_property
    def sector_etfs(self) -> AsyncSectorEtfsResourceWithRawResponse:
        return AsyncSectorEtfsResourceWithRawResponse(self._market.sector_etfs)

    @cached_property
    def spike(self) -> AsyncSpikeResourceWithRawResponse:
        return AsyncSpikeResourceWithRawResponse(self._market.spike)

    @cached_property
    def option_trade_volume(self) -> AsyncOptionTradeVolumeResourceWithRawResponse:
        return AsyncOptionTradeVolumeResourceWithRawResponse(self._market.option_trade_volume)

    @cached_property
    def etf_tide(self) -> AsyncEtfTideResourceWithRawResponse:
        return AsyncEtfTideResourceWithRawResponse(self._market.etf_tide)

    @cached_property
    def market_tide(self) -> AsyncMarketTideResourceWithRawResponse:
        return AsyncMarketTideResourceWithRawResponse(self._market.market_tide)

    @cached_property
    def oi_change(self) -> AsyncOiChangeResourceWithRawResponse:
        return AsyncOiChangeResourceWithRawResponse(self._market.oi_change)

    @cached_property
    def insider_trades(self) -> AsyncInsiderTradesResourceWithRawResponse:
        return AsyncInsiderTradesResourceWithRawResponse(self._market.insider_trades)

    @cached_property
    def correlation(self) -> AsyncCorrelationResourceWithRawResponse:
        return AsyncCorrelationResourceWithRawResponse(self._market.correlation)

    @cached_property
    def economic_calendar(self) -> AsyncEconomicCalendarResourceWithRawResponse:
        return AsyncEconomicCalendarResourceWithRawResponse(self._market.economic_calendar)

    @cached_property
    def fda_calendar(self) -> AsyncFdaCalendarResourceWithRawResponse:
        return AsyncFdaCalendarResourceWithRawResponse(self._market.fda_calendar)


class MarketResourceWithStreamingResponse:
    def __init__(self, market: MarketResource) -> None:
        self._market = market

    @cached_property
    def sector_etfs(self) -> SectorEtfsResourceWithStreamingResponse:
        return SectorEtfsResourceWithStreamingResponse(self._market.sector_etfs)

    @cached_property
    def spike(self) -> SpikeResourceWithStreamingResponse:
        return SpikeResourceWithStreamingResponse(self._market.spike)

    @cached_property
    def option_trade_volume(self) -> OptionTradeVolumeResourceWithStreamingResponse:
        return OptionTradeVolumeResourceWithStreamingResponse(self._market.option_trade_volume)

    @cached_property
    def etf_tide(self) -> EtfTideResourceWithStreamingResponse:
        return EtfTideResourceWithStreamingResponse(self._market.etf_tide)

    @cached_property
    def market_tide(self) -> MarketTideResourceWithStreamingResponse:
        return MarketTideResourceWithStreamingResponse(self._market.market_tide)

    @cached_property
    def oi_change(self) -> OiChangeResourceWithStreamingResponse:
        return OiChangeResourceWithStreamingResponse(self._market.oi_change)

    @cached_property
    def insider_trades(self) -> InsiderTradesResourceWithStreamingResponse:
        return InsiderTradesResourceWithStreamingResponse(self._market.insider_trades)

    @cached_property
    def correlation(self) -> CorrelationResourceWithStreamingResponse:
        return CorrelationResourceWithStreamingResponse(self._market.correlation)

    @cached_property
    def economic_calendar(self) -> EconomicCalendarResourceWithStreamingResponse:
        return EconomicCalendarResourceWithStreamingResponse(self._market.economic_calendar)

    @cached_property
    def fda_calendar(self) -> FdaCalendarResourceWithStreamingResponse:
        return FdaCalendarResourceWithStreamingResponse(self._market.fda_calendar)


class AsyncMarketResourceWithStreamingResponse:
    def __init__(self, market: AsyncMarketResource) -> None:
        self._market = market

    @cached_property
    def sector_etfs(self) -> AsyncSectorEtfsResourceWithStreamingResponse:
        return AsyncSectorEtfsResourceWithStreamingResponse(self._market.sector_etfs)

    @cached_property
    def spike(self) -> AsyncSpikeResourceWithStreamingResponse:
        return AsyncSpikeResourceWithStreamingResponse(self._market.spike)

    @cached_property
    def option_trade_volume(self) -> AsyncOptionTradeVolumeResourceWithStreamingResponse:
        return AsyncOptionTradeVolumeResourceWithStreamingResponse(self._market.option_trade_volume)

    @cached_property
    def etf_tide(self) -> AsyncEtfTideResourceWithStreamingResponse:
        return AsyncEtfTideResourceWithStreamingResponse(self._market.etf_tide)

    @cached_property
    def market_tide(self) -> AsyncMarketTideResourceWithStreamingResponse:
        return AsyncMarketTideResourceWithStreamingResponse(self._market.market_tide)

    @cached_property
    def oi_change(self) -> AsyncOiChangeResourceWithStreamingResponse:
        return AsyncOiChangeResourceWithStreamingResponse(self._market.oi_change)

    @cached_property
    def insider_trades(self) -> AsyncInsiderTradesResourceWithStreamingResponse:
        return AsyncInsiderTradesResourceWithStreamingResponse(self._market.insider_trades)

    @cached_property
    def correlation(self) -> AsyncCorrelationResourceWithStreamingResponse:
        return AsyncCorrelationResourceWithStreamingResponse(self._market.correlation)

    @cached_property
    def economic_calendar(self) -> AsyncEconomicCalendarResourceWithStreamingResponse:
        return AsyncEconomicCalendarResourceWithStreamingResponse(self._market.economic_calendar)

    @cached_property
    def fda_calendar(self) -> AsyncFdaCalendarResourceWithStreamingResponse:
        return AsyncFdaCalendarResourceWithStreamingResponse(self._market.fda_calendar)
