# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .stocks import (
    StocksResource,
    AsyncStocksResource,
    StocksResourceWithRawResponse,
    AsyncStocksResourceWithRawResponse,
    StocksResourceWithStreamingResponse,
    AsyncStocksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SeasonalityResource", "AsyncSeasonalityResource"]


class SeasonalityResource(SyncAPIResource):
    @cached_property
    def stocks(self) -> StocksResource:
        return StocksResource(self._client)

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
    def stocks(self) -> AsyncStocksResource:
        return AsyncStocksResource(self._client)

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
    def stocks(self) -> StocksResourceWithRawResponse:
        return StocksResourceWithRawResponse(self._seasonality.stocks)


class AsyncSeasonalityResourceWithRawResponse:
    def __init__(self, seasonality: AsyncSeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def stocks(self) -> AsyncStocksResourceWithRawResponse:
        return AsyncStocksResourceWithRawResponse(self._seasonality.stocks)


class SeasonalityResourceWithStreamingResponse:
    def __init__(self, seasonality: SeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def stocks(self) -> StocksResourceWithStreamingResponse:
        return StocksResourceWithStreamingResponse(self._seasonality.stocks)


class AsyncSeasonalityResourceWithStreamingResponse:
    def __init__(self, seasonality: AsyncSeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def stocks(self) -> AsyncStocksResourceWithStreamingResponse:
        return AsyncStocksResourceWithStreamingResponse(self._seasonality.stocks)
