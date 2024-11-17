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
from .correlations import (
    CorrelationsResource,
    AsyncCorrelationsResource,
    CorrelationsResourceWithRawResponse,
    AsyncCorrelationsResourceWithRawResponse,
    CorrelationsResourceWithStreamingResponse,
    AsyncCorrelationsResourceWithStreamingResponse,
)
from .fda_calendar import (
    FdaCalendarResource,
    AsyncFdaCalendarResource,
    FdaCalendarResourceWithRawResponse,
    AsyncFdaCalendarResourceWithRawResponse,
    FdaCalendarResourceWithStreamingResponse,
    AsyncFdaCalendarResourceWithStreamingResponse,
)
from .economic_calendar import (
    EconomicCalendarResource,
    AsyncEconomicCalendarResource,
    EconomicCalendarResourceWithRawResponse,
    AsyncEconomicCalendarResourceWithRawResponse,
    EconomicCalendarResourceWithStreamingResponse,
    AsyncEconomicCalendarResourceWithStreamingResponse,
)
from .insider_buy_sells import (
    InsiderBuySellsResource,
    AsyncInsiderBuySellsResource,
    InsiderBuySellsResourceWithRawResponse,
    AsyncInsiderBuySellsResourceWithRawResponse,
    InsiderBuySellsResourceWithStreamingResponse,
    AsyncInsiderBuySellsResourceWithStreamingResponse,
)
from .total_options_volume import (
    TotalOptionsVolumeResource,
    AsyncTotalOptionsVolumeResource,
    TotalOptionsVolumeResourceWithRawResponse,
    AsyncTotalOptionsVolumeResourceWithRawResponse,
    TotalOptionsVolumeResourceWithStreamingResponse,
    AsyncTotalOptionsVolumeResourceWithStreamingResponse,
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
    def total_options_volume(self) -> TotalOptionsVolumeResource:
        return TotalOptionsVolumeResource(self._client)

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
    def insider_buy_sells(self) -> InsiderBuySellsResource:
        return InsiderBuySellsResource(self._client)

    @cached_property
    def correlations(self) -> CorrelationsResource:
        return CorrelationsResource(self._client)

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
    def total_options_volume(self) -> AsyncTotalOptionsVolumeResource:
        return AsyncTotalOptionsVolumeResource(self._client)

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
    def insider_buy_sells(self) -> AsyncInsiderBuySellsResource:
        return AsyncInsiderBuySellsResource(self._client)

    @cached_property
    def correlations(self) -> AsyncCorrelationsResource:
        return AsyncCorrelationsResource(self._client)

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
    def total_options_volume(self) -> TotalOptionsVolumeResourceWithRawResponse:
        return TotalOptionsVolumeResourceWithRawResponse(self._market.total_options_volume)

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
    def insider_buy_sells(self) -> InsiderBuySellsResourceWithRawResponse:
        return InsiderBuySellsResourceWithRawResponse(self._market.insider_buy_sells)

    @cached_property
    def correlations(self) -> CorrelationsResourceWithRawResponse:
        return CorrelationsResourceWithRawResponse(self._market.correlations)

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
    def total_options_volume(self) -> AsyncTotalOptionsVolumeResourceWithRawResponse:
        return AsyncTotalOptionsVolumeResourceWithRawResponse(self._market.total_options_volume)

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
    def insider_buy_sells(self) -> AsyncInsiderBuySellsResourceWithRawResponse:
        return AsyncInsiderBuySellsResourceWithRawResponse(self._market.insider_buy_sells)

    @cached_property
    def correlations(self) -> AsyncCorrelationsResourceWithRawResponse:
        return AsyncCorrelationsResourceWithRawResponse(self._market.correlations)

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
    def total_options_volume(self) -> TotalOptionsVolumeResourceWithStreamingResponse:
        return TotalOptionsVolumeResourceWithStreamingResponse(self._market.total_options_volume)

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
    def insider_buy_sells(self) -> InsiderBuySellsResourceWithStreamingResponse:
        return InsiderBuySellsResourceWithStreamingResponse(self._market.insider_buy_sells)

    @cached_property
    def correlations(self) -> CorrelationsResourceWithStreamingResponse:
        return CorrelationsResourceWithStreamingResponse(self._market.correlations)

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
    def total_options_volume(self) -> AsyncTotalOptionsVolumeResourceWithStreamingResponse:
        return AsyncTotalOptionsVolumeResourceWithStreamingResponse(self._market.total_options_volume)

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
    def insider_buy_sells(self) -> AsyncInsiderBuySellsResourceWithStreamingResponse:
        return AsyncInsiderBuySellsResourceWithStreamingResponse(self._market.insider_buy_sells)

    @cached_property
    def correlations(self) -> AsyncCorrelationsResourceWithStreamingResponse:
        return AsyncCorrelationsResourceWithStreamingResponse(self._market.correlations)

    @cached_property
    def economic_calendar(self) -> AsyncEconomicCalendarResourceWithStreamingResponse:
        return AsyncEconomicCalendarResourceWithStreamingResponse(self._market.economic_calendar)

    @cached_property
    def fda_calendar(self) -> AsyncFdaCalendarResourceWithStreamingResponse:
        return AsyncFdaCalendarResourceWithStreamingResponse(self._market.fda_calendar)
