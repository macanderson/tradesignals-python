# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .news import (
    NewsResource,
    AsyncNewsResource,
    NewsResourceWithRawResponse,
    AsyncNewsResourceWithRawResponse,
    NewsResourceWithStreamingResponse,
    AsyncNewsResourceWithStreamingResponse,
)
from .movers import (
    MoversResource,
    AsyncMoversResource,
    MoversResourceWithRawResponse,
    AsyncMoversResourceWithRawResponse,
    MoversResourceWithStreamingResponse,
    AsyncMoversResourceWithStreamingResponse,
)
from .indices import (
    IndicesResource,
    AsyncIndicesResource,
    IndicesResourceWithRawResponse,
    AsyncIndicesResourceWithRawResponse,
    IndicesResourceWithStreamingResponse,
    AsyncIndicesResourceWithStreamingResponse,
)
from .sectors import (
    SectorsResource,
    AsyncSectorsResource,
    SectorsResourceWithRawResponse,
    AsyncSectorsResourceWithRawResponse,
    SectorsResourceWithStreamingResponse,
    AsyncSectorsResourceWithStreamingResponse,
)
from .overview import (
    OverviewResource,
    AsyncOverviewResource,
    OverviewResourceWithRawResponse,
    AsyncOverviewResourceWithRawResponse,
    OverviewResourceWithStreamingResponse,
    AsyncOverviewResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .spike_detection import (
    SpikeDetectionResource,
    AsyncSpikeDetectionResource,
    SpikeDetectionResourceWithRawResponse,
    AsyncSpikeDetectionResourceWithRawResponse,
    SpikeDetectionResourceWithStreamingResponse,
    AsyncSpikeDetectionResourceWithStreamingResponse,
)

__all__ = ["MarketResource", "AsyncMarketResource"]


class MarketResource(SyncAPIResource):
    @cached_property
    def spike_detection(self) -> SpikeDetectionResource:
        return SpikeDetectionResource(self._client)

    @cached_property
    def overview(self) -> OverviewResource:
        return OverviewResource(self._client)

    @cached_property
    def indices(self) -> IndicesResource:
        return IndicesResource(self._client)

    @cached_property
    def movers(self) -> MoversResource:
        return MoversResource(self._client)

    @cached_property
    def sectors(self) -> SectorsResource:
        return SectorsResource(self._client)

    @cached_property
    def news(self) -> NewsResource:
        return NewsResource(self._client)

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
    def spike_detection(self) -> AsyncSpikeDetectionResource:
        return AsyncSpikeDetectionResource(self._client)

    @cached_property
    def overview(self) -> AsyncOverviewResource:
        return AsyncOverviewResource(self._client)

    @cached_property
    def indices(self) -> AsyncIndicesResource:
        return AsyncIndicesResource(self._client)

    @cached_property
    def movers(self) -> AsyncMoversResource:
        return AsyncMoversResource(self._client)

    @cached_property
    def sectors(self) -> AsyncSectorsResource:
        return AsyncSectorsResource(self._client)

    @cached_property
    def news(self) -> AsyncNewsResource:
        return AsyncNewsResource(self._client)

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
    def spike_detection(self) -> SpikeDetectionResourceWithRawResponse:
        return SpikeDetectionResourceWithRawResponse(self._market.spike_detection)

    @cached_property
    def overview(self) -> OverviewResourceWithRawResponse:
        return OverviewResourceWithRawResponse(self._market.overview)

    @cached_property
    def indices(self) -> IndicesResourceWithRawResponse:
        return IndicesResourceWithRawResponse(self._market.indices)

    @cached_property
    def movers(self) -> MoversResourceWithRawResponse:
        return MoversResourceWithRawResponse(self._market.movers)

    @cached_property
    def sectors(self) -> SectorsResourceWithRawResponse:
        return SectorsResourceWithRawResponse(self._market.sectors)

    @cached_property
    def news(self) -> NewsResourceWithRawResponse:
        return NewsResourceWithRawResponse(self._market.news)


class AsyncMarketResourceWithRawResponse:
    def __init__(self, market: AsyncMarketResource) -> None:
        self._market = market

    @cached_property
    def spike_detection(self) -> AsyncSpikeDetectionResourceWithRawResponse:
        return AsyncSpikeDetectionResourceWithRawResponse(self._market.spike_detection)

    @cached_property
    def overview(self) -> AsyncOverviewResourceWithRawResponse:
        return AsyncOverviewResourceWithRawResponse(self._market.overview)

    @cached_property
    def indices(self) -> AsyncIndicesResourceWithRawResponse:
        return AsyncIndicesResourceWithRawResponse(self._market.indices)

    @cached_property
    def movers(self) -> AsyncMoversResourceWithRawResponse:
        return AsyncMoversResourceWithRawResponse(self._market.movers)

    @cached_property
    def sectors(self) -> AsyncSectorsResourceWithRawResponse:
        return AsyncSectorsResourceWithRawResponse(self._market.sectors)

    @cached_property
    def news(self) -> AsyncNewsResourceWithRawResponse:
        return AsyncNewsResourceWithRawResponse(self._market.news)


class MarketResourceWithStreamingResponse:
    def __init__(self, market: MarketResource) -> None:
        self._market = market

    @cached_property
    def spike_detection(self) -> SpikeDetectionResourceWithStreamingResponse:
        return SpikeDetectionResourceWithStreamingResponse(self._market.spike_detection)

    @cached_property
    def overview(self) -> OverviewResourceWithStreamingResponse:
        return OverviewResourceWithStreamingResponse(self._market.overview)

    @cached_property
    def indices(self) -> IndicesResourceWithStreamingResponse:
        return IndicesResourceWithStreamingResponse(self._market.indices)

    @cached_property
    def movers(self) -> MoversResourceWithStreamingResponse:
        return MoversResourceWithStreamingResponse(self._market.movers)

    @cached_property
    def sectors(self) -> SectorsResourceWithStreamingResponse:
        return SectorsResourceWithStreamingResponse(self._market.sectors)

    @cached_property
    def news(self) -> NewsResourceWithStreamingResponse:
        return NewsResourceWithStreamingResponse(self._market.news)


class AsyncMarketResourceWithStreamingResponse:
    def __init__(self, market: AsyncMarketResource) -> None:
        self._market = market

    @cached_property
    def spike_detection(self) -> AsyncSpikeDetectionResourceWithStreamingResponse:
        return AsyncSpikeDetectionResourceWithStreamingResponse(self._market.spike_detection)

    @cached_property
    def overview(self) -> AsyncOverviewResourceWithStreamingResponse:
        return AsyncOverviewResourceWithStreamingResponse(self._market.overview)

    @cached_property
    def indices(self) -> AsyncIndicesResourceWithStreamingResponse:
        return AsyncIndicesResourceWithStreamingResponse(self._market.indices)

    @cached_property
    def movers(self) -> AsyncMoversResourceWithStreamingResponse:
        return AsyncMoversResourceWithStreamingResponse(self._market.movers)

    @cached_property
    def sectors(self) -> AsyncSectorsResourceWithStreamingResponse:
        return AsyncSectorsResourceWithStreamingResponse(self._market.sectors)

    @cached_property
    def news(self) -> AsyncNewsResourceWithStreamingResponse:
        return AsyncNewsResourceWithStreamingResponse(self._market.news)
