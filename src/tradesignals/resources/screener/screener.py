# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .stock_screener import (
    StockScreenerResource,
    AsyncStockScreenerResource,
    StockScreenerResourceWithRawResponse,
    AsyncStockScreenerResourceWithRawResponse,
    StockScreenerResourceWithStreamingResponse,
    AsyncStockScreenerResourceWithStreamingResponse,
)
from .option_screener import (
    OptionScreenerResource,
    AsyncOptionScreenerResource,
    OptionScreenerResourceWithRawResponse,
    AsyncOptionScreenerResourceWithRawResponse,
    OptionScreenerResourceWithStreamingResponse,
    AsyncOptionScreenerResourceWithStreamingResponse,
)

__all__ = ["ScreenerResource", "AsyncScreenerResource"]


class ScreenerResource(SyncAPIResource):
    @cached_property
    def stock_screener(self) -> StockScreenerResource:
        return StockScreenerResource(self._client)

    @cached_property
    def option_screener(self) -> OptionScreenerResource:
        return OptionScreenerResource(self._client)

    @cached_property
    def with_raw_response(self) -> ScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return ScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return ScreenerResourceWithStreamingResponse(self)


class AsyncScreenerResource(AsyncAPIResource):
    @cached_property
    def stock_screener(self) -> AsyncStockScreenerResource:
        return AsyncStockScreenerResource(self._client)

    @cached_property
    def option_screener(self) -> AsyncOptionScreenerResource:
        return AsyncOptionScreenerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncScreenerResourceWithStreamingResponse(self)


class ScreenerResourceWithRawResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

    @cached_property
    def stock_screener(self) -> StockScreenerResourceWithRawResponse:
        return StockScreenerResourceWithRawResponse(self._screener.stock_screener)

    @cached_property
    def option_screener(self) -> OptionScreenerResourceWithRawResponse:
        return OptionScreenerResourceWithRawResponse(self._screener.option_screener)


class AsyncScreenerResourceWithRawResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

    @cached_property
    def stock_screener(self) -> AsyncStockScreenerResourceWithRawResponse:
        return AsyncStockScreenerResourceWithRawResponse(self._screener.stock_screener)

    @cached_property
    def option_screener(self) -> AsyncOptionScreenerResourceWithRawResponse:
        return AsyncOptionScreenerResourceWithRawResponse(self._screener.option_screener)


class ScreenerResourceWithStreamingResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

    @cached_property
    def stock_screener(self) -> StockScreenerResourceWithStreamingResponse:
        return StockScreenerResourceWithStreamingResponse(self._screener.stock_screener)

    @cached_property
    def option_screener(self) -> OptionScreenerResourceWithStreamingResponse:
        return OptionScreenerResourceWithStreamingResponse(self._screener.option_screener)


class AsyncScreenerResourceWithStreamingResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

    @cached_property
    def stock_screener(self) -> AsyncStockScreenerResourceWithStreamingResponse:
        return AsyncStockScreenerResourceWithStreamingResponse(self._screener.stock_screener)

    @cached_property
    def option_screener(self) -> AsyncOptionScreenerResourceWithStreamingResponse:
        return AsyncOptionScreenerResourceWithStreamingResponse(self._screener.option_screener)
