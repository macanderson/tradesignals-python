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
from .market_oi_change import (
    MarketOiChangeResource,
    AsyncMarketOiChangeResource,
    MarketOiChangeResourceWithRawResponse,
    AsyncMarketOiChangeResourceWithRawResponse,
    MarketOiChangeResourceWithStreamingResponse,
    AsyncMarketOiChangeResourceWithStreamingResponse,
)
from .economic_calendar import (
    EconomicCalendarResource,
    AsyncEconomicCalendarResource,
    EconomicCalendarResourceWithRawResponse,
    AsyncEconomicCalendarResourceWithRawResponse,
    EconomicCalendarResourceWithStreamingResponse,
    AsyncEconomicCalendarResourceWithStreamingResponse,
)
from .market_option_volume import (
    MarketOptionVolumeResource,
    AsyncMarketOptionVolumeResource,
    MarketOptionVolumeResourceWithRawResponse,
    AsyncMarketOptionVolumeResourceWithRawResponse,
    MarketOptionVolumeResourceWithStreamingResponse,
    AsyncMarketOptionVolumeResourceWithStreamingResponse,
)

__all__ = ["MarketDataResource", "AsyncMarketDataResource"]


class MarketDataResource(SyncAPIResource):
    """
    Market endpoints provide data and insights into the broader stock market and other macro-level indicators.
    """

    @cached_property
    def sector_etfs(self) -> SectorEtfsResource:
        return SectorEtfsResource(self._client)

    @cached_property
    def spike(self) -> SpikeResource:
        return SpikeResource(self._client)

    @cached_property
    def market_option_volume(self) -> MarketOptionVolumeResource:
        return MarketOptionVolumeResource(self._client)

    @cached_property
    def etf_tide(self) -> EtfTideResource:
        return EtfTideResource(self._client)

    @cached_property
    def market_tide(self) -> MarketTideResource:
        return MarketTideResource(self._client)

    @cached_property
    def market_oi_change(self) -> MarketOiChangeResource:
        return MarketOiChangeResource(self._client)

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
    def with_raw_response(self) -> MarketDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return MarketDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return MarketDataResourceWithStreamingResponse(self)


class AsyncMarketDataResource(AsyncAPIResource):
    """
    Market endpoints provide data and insights into the broader stock market and other macro-level indicators.
    """

    @cached_property
    def sector_etfs(self) -> AsyncSectorEtfsResource:
        return AsyncSectorEtfsResource(self._client)

    @cached_property
    def spike(self) -> AsyncSpikeResource:
        return AsyncSpikeResource(self._client)

    @cached_property
    def market_option_volume(self) -> AsyncMarketOptionVolumeResource:
        return AsyncMarketOptionVolumeResource(self._client)

    @cached_property
    def etf_tide(self) -> AsyncEtfTideResource:
        return AsyncEtfTideResource(self._client)

    @cached_property
    def market_tide(self) -> AsyncMarketTideResource:
        return AsyncMarketTideResource(self._client)

    @cached_property
    def market_oi_change(self) -> AsyncMarketOiChangeResource:
        return AsyncMarketOiChangeResource(self._client)

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
    def with_raw_response(self) -> AsyncMarketDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncMarketDataResourceWithStreamingResponse(self)


class MarketDataResourceWithRawResponse:
    def __init__(self, market_data: MarketDataResource) -> None:
        self._market_data = market_data

    @cached_property
    def sector_etfs(self) -> SectorEtfsResourceWithRawResponse:
        return SectorEtfsResourceWithRawResponse(self._market_data.sector_etfs)

    @cached_property
    def spike(self) -> SpikeResourceWithRawResponse:
        return SpikeResourceWithRawResponse(self._market_data.spike)

    @cached_property
    def market_option_volume(self) -> MarketOptionVolumeResourceWithRawResponse:
        return MarketOptionVolumeResourceWithRawResponse(self._market_data.market_option_volume)

    @cached_property
    def etf_tide(self) -> EtfTideResourceWithRawResponse:
        return EtfTideResourceWithRawResponse(self._market_data.etf_tide)

    @cached_property
    def market_tide(self) -> MarketTideResourceWithRawResponse:
        return MarketTideResourceWithRawResponse(self._market_data.market_tide)

    @cached_property
    def market_oi_change(self) -> MarketOiChangeResourceWithRawResponse:
        return MarketOiChangeResourceWithRawResponse(self._market_data.market_oi_change)

    @cached_property
    def insider_trades(self) -> InsiderTradesResourceWithRawResponse:
        return InsiderTradesResourceWithRawResponse(self._market_data.insider_trades)

    @cached_property
    def correlation(self) -> CorrelationResourceWithRawResponse:
        return CorrelationResourceWithRawResponse(self._market_data.correlation)

    @cached_property
    def economic_calendar(self) -> EconomicCalendarResourceWithRawResponse:
        return EconomicCalendarResourceWithRawResponse(self._market_data.economic_calendar)

    @cached_property
    def fda_calendar(self) -> FdaCalendarResourceWithRawResponse:
        return FdaCalendarResourceWithRawResponse(self._market_data.fda_calendar)


class AsyncMarketDataResourceWithRawResponse:
    def __init__(self, market_data: AsyncMarketDataResource) -> None:
        self._market_data = market_data

    @cached_property
    def sector_etfs(self) -> AsyncSectorEtfsResourceWithRawResponse:
        return AsyncSectorEtfsResourceWithRawResponse(self._market_data.sector_etfs)

    @cached_property
    def spike(self) -> AsyncSpikeResourceWithRawResponse:
        return AsyncSpikeResourceWithRawResponse(self._market_data.spike)

    @cached_property
    def market_option_volume(self) -> AsyncMarketOptionVolumeResourceWithRawResponse:
        return AsyncMarketOptionVolumeResourceWithRawResponse(self._market_data.market_option_volume)

    @cached_property
    def etf_tide(self) -> AsyncEtfTideResourceWithRawResponse:
        return AsyncEtfTideResourceWithRawResponse(self._market_data.etf_tide)

    @cached_property
    def market_tide(self) -> AsyncMarketTideResourceWithRawResponse:
        return AsyncMarketTideResourceWithRawResponse(self._market_data.market_tide)

    @cached_property
    def market_oi_change(self) -> AsyncMarketOiChangeResourceWithRawResponse:
        return AsyncMarketOiChangeResourceWithRawResponse(self._market_data.market_oi_change)

    @cached_property
    def insider_trades(self) -> AsyncInsiderTradesResourceWithRawResponse:
        return AsyncInsiderTradesResourceWithRawResponse(self._market_data.insider_trades)

    @cached_property
    def correlation(self) -> AsyncCorrelationResourceWithRawResponse:
        return AsyncCorrelationResourceWithRawResponse(self._market_data.correlation)

    @cached_property
    def economic_calendar(self) -> AsyncEconomicCalendarResourceWithRawResponse:
        return AsyncEconomicCalendarResourceWithRawResponse(self._market_data.economic_calendar)

    @cached_property
    def fda_calendar(self) -> AsyncFdaCalendarResourceWithRawResponse:
        return AsyncFdaCalendarResourceWithRawResponse(self._market_data.fda_calendar)


class MarketDataResourceWithStreamingResponse:
    def __init__(self, market_data: MarketDataResource) -> None:
        self._market_data = market_data

    @cached_property
    def sector_etfs(self) -> SectorEtfsResourceWithStreamingResponse:
        return SectorEtfsResourceWithStreamingResponse(self._market_data.sector_etfs)

    @cached_property
    def spike(self) -> SpikeResourceWithStreamingResponse:
        return SpikeResourceWithStreamingResponse(self._market_data.spike)

    @cached_property
    def market_option_volume(self) -> MarketOptionVolumeResourceWithStreamingResponse:
        return MarketOptionVolumeResourceWithStreamingResponse(self._market_data.market_option_volume)

    @cached_property
    def etf_tide(self) -> EtfTideResourceWithStreamingResponse:
        return EtfTideResourceWithStreamingResponse(self._market_data.etf_tide)

    @cached_property
    def market_tide(self) -> MarketTideResourceWithStreamingResponse:
        return MarketTideResourceWithStreamingResponse(self._market_data.market_tide)

    @cached_property
    def market_oi_change(self) -> MarketOiChangeResourceWithStreamingResponse:
        return MarketOiChangeResourceWithStreamingResponse(self._market_data.market_oi_change)

    @cached_property
    def insider_trades(self) -> InsiderTradesResourceWithStreamingResponse:
        return InsiderTradesResourceWithStreamingResponse(self._market_data.insider_trades)

    @cached_property
    def correlation(self) -> CorrelationResourceWithStreamingResponse:
        return CorrelationResourceWithStreamingResponse(self._market_data.correlation)

    @cached_property
    def economic_calendar(self) -> EconomicCalendarResourceWithStreamingResponse:
        return EconomicCalendarResourceWithStreamingResponse(self._market_data.economic_calendar)

    @cached_property
    def fda_calendar(self) -> FdaCalendarResourceWithStreamingResponse:
        return FdaCalendarResourceWithStreamingResponse(self._market_data.fda_calendar)


class AsyncMarketDataResourceWithStreamingResponse:
    def __init__(self, market_data: AsyncMarketDataResource) -> None:
        self._market_data = market_data

    @cached_property
    def sector_etfs(self) -> AsyncSectorEtfsResourceWithStreamingResponse:
        return AsyncSectorEtfsResourceWithStreamingResponse(self._market_data.sector_etfs)

    @cached_property
    def spike(self) -> AsyncSpikeResourceWithStreamingResponse:
        return AsyncSpikeResourceWithStreamingResponse(self._market_data.spike)

    @cached_property
    def market_option_volume(self) -> AsyncMarketOptionVolumeResourceWithStreamingResponse:
        return AsyncMarketOptionVolumeResourceWithStreamingResponse(self._market_data.market_option_volume)

    @cached_property
    def etf_tide(self) -> AsyncEtfTideResourceWithStreamingResponse:
        return AsyncEtfTideResourceWithStreamingResponse(self._market_data.etf_tide)

    @cached_property
    def market_tide(self) -> AsyncMarketTideResourceWithStreamingResponse:
        return AsyncMarketTideResourceWithStreamingResponse(self._market_data.market_tide)

    @cached_property
    def market_oi_change(self) -> AsyncMarketOiChangeResourceWithStreamingResponse:
        return AsyncMarketOiChangeResourceWithStreamingResponse(self._market_data.market_oi_change)

    @cached_property
    def insider_trades(self) -> AsyncInsiderTradesResourceWithStreamingResponse:
        return AsyncInsiderTradesResourceWithStreamingResponse(self._market_data.insider_trades)

    @cached_property
    def correlation(self) -> AsyncCorrelationResourceWithStreamingResponse:
        return AsyncCorrelationResourceWithStreamingResponse(self._market_data.correlation)

    @cached_property
    def economic_calendar(self) -> AsyncEconomicCalendarResourceWithStreamingResponse:
        return AsyncEconomicCalendarResourceWithStreamingResponse(self._market_data.economic_calendar)

    @cached_property
    def fda_calendar(self) -> AsyncFdaCalendarResourceWithStreamingResponse:
        return AsyncFdaCalendarResourceWithStreamingResponse(self._market_data.fda_calendar)
