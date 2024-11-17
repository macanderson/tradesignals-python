# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .stock_finder import (
    StockFinderResource,
    AsyncStockFinderResource,
    StockFinderResourceWithRawResponse,
    AsyncStockFinderResourceWithRawResponse,
    StockFinderResourceWithStreamingResponse,
    AsyncStockFinderResourceWithStreamingResponse,
)
from .option_finder import (
    OptionFinderResource,
    AsyncOptionFinderResource,
    OptionFinderResourceWithRawResponse,
    AsyncOptionFinderResourceWithRawResponse,
    OptionFinderResourceWithStreamingResponse,
    AsyncOptionFinderResourceWithStreamingResponse,
)
from .analyst_ratings import (
    AnalystRatingsResource,
    AsyncAnalystRatingsResource,
    AnalystRatingsResourceWithRawResponse,
    AsyncAnalystRatingsResourceWithRawResponse,
    AnalystRatingsResourceWithStreamingResponse,
    AsyncAnalystRatingsResourceWithStreamingResponse,
)

__all__ = ["ScreenersResource", "AsyncScreenersResource"]


class ScreenersResource(SyncAPIResource):
    @cached_property
    def stock_finder(self) -> StockFinderResource:
        return StockFinderResource(self._client)

    @cached_property
    def analyst_ratings(self) -> AnalystRatingsResource:
        return AnalystRatingsResource(self._client)

    @cached_property
    def option_finder(self) -> OptionFinderResource:
        return OptionFinderResource(self._client)

    @cached_property
    def with_raw_response(self) -> ScreenersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return ScreenersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return ScreenersResourceWithStreamingResponse(self)


class AsyncScreenersResource(AsyncAPIResource):
    @cached_property
    def stock_finder(self) -> AsyncStockFinderResource:
        return AsyncStockFinderResource(self._client)

    @cached_property
    def analyst_ratings(self) -> AsyncAnalystRatingsResource:
        return AsyncAnalystRatingsResource(self._client)

    @cached_property
    def option_finder(self) -> AsyncOptionFinderResource:
        return AsyncOptionFinderResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScreenersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScreenersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncScreenersResourceWithStreamingResponse(self)


class ScreenersResourceWithRawResponse:
    def __init__(self, screeners: ScreenersResource) -> None:
        self._screeners = screeners

    @cached_property
    def stock_finder(self) -> StockFinderResourceWithRawResponse:
        return StockFinderResourceWithRawResponse(self._screeners.stock_finder)

    @cached_property
    def analyst_ratings(self) -> AnalystRatingsResourceWithRawResponse:
        return AnalystRatingsResourceWithRawResponse(self._screeners.analyst_ratings)

    @cached_property
    def option_finder(self) -> OptionFinderResourceWithRawResponse:
        return OptionFinderResourceWithRawResponse(self._screeners.option_finder)


class AsyncScreenersResourceWithRawResponse:
    def __init__(self, screeners: AsyncScreenersResource) -> None:
        self._screeners = screeners

    @cached_property
    def stock_finder(self) -> AsyncStockFinderResourceWithRawResponse:
        return AsyncStockFinderResourceWithRawResponse(self._screeners.stock_finder)

    @cached_property
    def analyst_ratings(self) -> AsyncAnalystRatingsResourceWithRawResponse:
        return AsyncAnalystRatingsResourceWithRawResponse(self._screeners.analyst_ratings)

    @cached_property
    def option_finder(self) -> AsyncOptionFinderResourceWithRawResponse:
        return AsyncOptionFinderResourceWithRawResponse(self._screeners.option_finder)


class ScreenersResourceWithStreamingResponse:
    def __init__(self, screeners: ScreenersResource) -> None:
        self._screeners = screeners

    @cached_property
    def stock_finder(self) -> StockFinderResourceWithStreamingResponse:
        return StockFinderResourceWithStreamingResponse(self._screeners.stock_finder)

    @cached_property
    def analyst_ratings(self) -> AnalystRatingsResourceWithStreamingResponse:
        return AnalystRatingsResourceWithStreamingResponse(self._screeners.analyst_ratings)

    @cached_property
    def option_finder(self) -> OptionFinderResourceWithStreamingResponse:
        return OptionFinderResourceWithStreamingResponse(self._screeners.option_finder)


class AsyncScreenersResourceWithStreamingResponse:
    def __init__(self, screeners: AsyncScreenersResource) -> None:
        self._screeners = screeners

    @cached_property
    def stock_finder(self) -> AsyncStockFinderResourceWithStreamingResponse:
        return AsyncStockFinderResourceWithStreamingResponse(self._screeners.stock_finder)

    @cached_property
    def analyst_ratings(self) -> AsyncAnalystRatingsResourceWithStreamingResponse:
        return AsyncAnalystRatingsResourceWithStreamingResponse(self._screeners.analyst_ratings)

    @cached_property
    def option_finder(self) -> AsyncOptionFinderResourceWithStreamingResponse:
        return AsyncOptionFinderResourceWithStreamingResponse(self._screeners.option_finder)
