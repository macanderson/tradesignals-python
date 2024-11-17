# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .market import (
    MarketResource,
    AsyncMarketResource,
    MarketResourceWithRawResponse,
    AsyncMarketResourceWithRawResponse,
    MarketResourceWithStreamingResponse,
    AsyncMarketResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .performers import (
    PerformersResource,
    AsyncPerformersResource,
    PerformersResourceWithRawResponse,
    AsyncPerformersResourceWithRawResponse,
    PerformersResourceWithStreamingResponse,
    AsyncPerformersResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SeasonalityResource", "AsyncSeasonalityResource"]


class SeasonalityResource(SyncAPIResource):
    @cached_property
    def market(self) -> MarketResource:
        return MarketResource(self._client)

    @cached_property
    def performers(self) -> PerformersResource:
        return PerformersResource(self._client)

    @cached_property
    def with_raw_response(self) -> SeasonalityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return SeasonalityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeasonalityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return SeasonalityResourceWithStreamingResponse(self)


class AsyncSeasonalityResource(AsyncAPIResource):
    @cached_property
    def market(self) -> AsyncMarketResource:
        return AsyncMarketResource(self._client)

    @cached_property
    def performers(self) -> AsyncPerformersResource:
        return AsyncPerformersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSeasonalityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSeasonalityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeasonalityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncSeasonalityResourceWithStreamingResponse(self)


class SeasonalityResourceWithRawResponse:
    def __init__(self, seasonality: SeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def market(self) -> MarketResourceWithRawResponse:
        return MarketResourceWithRawResponse(self._seasonality.market)

    @cached_property
    def performers(self) -> PerformersResourceWithRawResponse:
        return PerformersResourceWithRawResponse(self._seasonality.performers)


class AsyncSeasonalityResourceWithRawResponse:
    def __init__(self, seasonality: AsyncSeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def market(self) -> AsyncMarketResourceWithRawResponse:
        return AsyncMarketResourceWithRawResponse(self._seasonality.market)

    @cached_property
    def performers(self) -> AsyncPerformersResourceWithRawResponse:
        return AsyncPerformersResourceWithRawResponse(self._seasonality.performers)


class SeasonalityResourceWithStreamingResponse:
    def __init__(self, seasonality: SeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def market(self) -> MarketResourceWithStreamingResponse:
        return MarketResourceWithStreamingResponse(self._seasonality.market)

    @cached_property
    def performers(self) -> PerformersResourceWithStreamingResponse:
        return PerformersResourceWithStreamingResponse(self._seasonality.performers)


class AsyncSeasonalityResourceWithStreamingResponse:
    def __init__(self, seasonality: AsyncSeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def market(self) -> AsyncMarketResourceWithStreamingResponse:
        return AsyncMarketResourceWithStreamingResponse(self._seasonality.market)

    @cached_property
    def performers(self) -> AsyncPerformersResourceWithStreamingResponse:
        return AsyncPerformersResourceWithStreamingResponse(self._seasonality.performers)
