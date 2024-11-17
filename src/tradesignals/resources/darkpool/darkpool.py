# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .recent_trades import (
    RecentTradesResource,
    AsyncRecentTradesResource,
    RecentTradesResourceWithRawResponse,
    AsyncRecentTradesResourceWithRawResponse,
    RecentTradesResourceWithStreamingResponse,
    AsyncRecentTradesResourceWithStreamingResponse,
)
from .trades_by_ticker import (
    TradesByTickerResource,
    AsyncTradesByTickerResource,
    TradesByTickerResourceWithRawResponse,
    AsyncTradesByTickerResourceWithRawResponse,
    TradesByTickerResourceWithStreamingResponse,
    AsyncTradesByTickerResourceWithStreamingResponse,
)

__all__ = ["DarkpoolResource", "AsyncDarkpoolResource"]


class DarkpoolResource(SyncAPIResource):
    @cached_property
    def recent_trades(self) -> RecentTradesResource:
        return RecentTradesResource(self._client)

    @cached_property
    def trades_by_ticker(self) -> TradesByTickerResource:
        return TradesByTickerResource(self._client)

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
    def recent_trades(self) -> AsyncRecentTradesResource:
        return AsyncRecentTradesResource(self._client)

    @cached_property
    def trades_by_ticker(self) -> AsyncTradesByTickerResource:
        return AsyncTradesByTickerResource(self._client)

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
    def recent_trades(self) -> RecentTradesResourceWithRawResponse:
        return RecentTradesResourceWithRawResponse(self._darkpool.recent_trades)

    @cached_property
    def trades_by_ticker(self) -> TradesByTickerResourceWithRawResponse:
        return TradesByTickerResourceWithRawResponse(self._darkpool.trades_by_ticker)


class AsyncDarkpoolResourceWithRawResponse:
    def __init__(self, darkpool: AsyncDarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def recent_trades(self) -> AsyncRecentTradesResourceWithRawResponse:
        return AsyncRecentTradesResourceWithRawResponse(self._darkpool.recent_trades)

    @cached_property
    def trades_by_ticker(self) -> AsyncTradesByTickerResourceWithRawResponse:
        return AsyncTradesByTickerResourceWithRawResponse(self._darkpool.trades_by_ticker)


class DarkpoolResourceWithStreamingResponse:
    def __init__(self, darkpool: DarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def recent_trades(self) -> RecentTradesResourceWithStreamingResponse:
        return RecentTradesResourceWithStreamingResponse(self._darkpool.recent_trades)

    @cached_property
    def trades_by_ticker(self) -> TradesByTickerResourceWithStreamingResponse:
        return TradesByTickerResourceWithStreamingResponse(self._darkpool.trades_by_ticker)


class AsyncDarkpoolResourceWithStreamingResponse:
    def __init__(self, darkpool: AsyncDarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def recent_trades(self) -> AsyncRecentTradesResourceWithStreamingResponse:
        return AsyncRecentTradesResourceWithStreamingResponse(self._darkpool.recent_trades)

    @cached_property
    def trades_by_ticker(self) -> AsyncTradesByTickerResourceWithStreamingResponse:
        return AsyncTradesByTickerResourceWithStreamingResponse(self._darkpool.trades_by_ticker)
