# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .recent_darkpool_trades import (
    RecentDarkpoolTradesResource,
    AsyncRecentDarkpoolTradesResource,
    RecentDarkpoolTradesResourceWithRawResponse,
    AsyncRecentDarkpoolTradesResourceWithRawResponse,
    RecentDarkpoolTradesResourceWithStreamingResponse,
    AsyncRecentDarkpoolTradesResourceWithStreamingResponse,
)
from .ticker_darkpool_trades import (
    TickerDarkpoolTradesResource,
    AsyncTickerDarkpoolTradesResource,
    TickerDarkpoolTradesResourceWithRawResponse,
    AsyncTickerDarkpoolTradesResourceWithRawResponse,
    TickerDarkpoolTradesResourceWithStreamingResponse,
    AsyncTickerDarkpoolTradesResourceWithStreamingResponse,
)

__all__ = ["DarkpoolResource", "AsyncDarkpoolResource"]


class DarkpoolResource(SyncAPIResource):
    @cached_property
    def recent_darkpool_trades(self) -> RecentDarkpoolTradesResource:
        return RecentDarkpoolTradesResource(self._client)

    @cached_property
    def ticker_darkpool_trades(self) -> TickerDarkpoolTradesResource:
        return TickerDarkpoolTradesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DarkpoolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return DarkpoolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DarkpoolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return DarkpoolResourceWithStreamingResponse(self)


class AsyncDarkpoolResource(AsyncAPIResource):
    @cached_property
    def recent_darkpool_trades(self) -> AsyncRecentDarkpoolTradesResource:
        return AsyncRecentDarkpoolTradesResource(self._client)

    @cached_property
    def ticker_darkpool_trades(self) -> AsyncTickerDarkpoolTradesResource:
        return AsyncTickerDarkpoolTradesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDarkpoolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDarkpoolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDarkpoolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncDarkpoolResourceWithStreamingResponse(self)


class DarkpoolResourceWithRawResponse:
    def __init__(self, darkpool: DarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def recent_darkpool_trades(self) -> RecentDarkpoolTradesResourceWithRawResponse:
        return RecentDarkpoolTradesResourceWithRawResponse(self._darkpool.recent_darkpool_trades)

    @cached_property
    def ticker_darkpool_trades(self) -> TickerDarkpoolTradesResourceWithRawResponse:
        return TickerDarkpoolTradesResourceWithRawResponse(self._darkpool.ticker_darkpool_trades)


class AsyncDarkpoolResourceWithRawResponse:
    def __init__(self, darkpool: AsyncDarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def recent_darkpool_trades(self) -> AsyncRecentDarkpoolTradesResourceWithRawResponse:
        return AsyncRecentDarkpoolTradesResourceWithRawResponse(self._darkpool.recent_darkpool_trades)

    @cached_property
    def ticker_darkpool_trades(self) -> AsyncTickerDarkpoolTradesResourceWithRawResponse:
        return AsyncTickerDarkpoolTradesResourceWithRawResponse(self._darkpool.ticker_darkpool_trades)


class DarkpoolResourceWithStreamingResponse:
    def __init__(self, darkpool: DarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def recent_darkpool_trades(self) -> RecentDarkpoolTradesResourceWithStreamingResponse:
        return RecentDarkpoolTradesResourceWithStreamingResponse(self._darkpool.recent_darkpool_trades)

    @cached_property
    def ticker_darkpool_trades(self) -> TickerDarkpoolTradesResourceWithStreamingResponse:
        return TickerDarkpoolTradesResourceWithStreamingResponse(self._darkpool.ticker_darkpool_trades)


class AsyncDarkpoolResourceWithStreamingResponse:
    def __init__(self, darkpool: AsyncDarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def recent_darkpool_trades(self) -> AsyncRecentDarkpoolTradesResourceWithStreamingResponse:
        return AsyncRecentDarkpoolTradesResourceWithStreamingResponse(self._darkpool.recent_darkpool_trades)

    @cached_property
    def ticker_darkpool_trades(self) -> AsyncTickerDarkpoolTradesResourceWithStreamingResponse:
        return AsyncTickerDarkpoolTradesResourceWithStreamingResponse(self._darkpool.ticker_darkpool_trades)
