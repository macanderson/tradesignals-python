# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .trader import (
    TraderResource,
    AsyncTraderResource,
    TraderResourceWithRawResponse,
    AsyncTraderResourceWithRawResponse,
    TraderResourceWithStreamingResponse,
    AsyncTraderResourceWithStreamingResponse,
)
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
from .late_trade_reports import (
    LateTradeReportsResource,
    AsyncLateTradeReportsResource,
    LateTradeReportsResourceWithRawResponse,
    AsyncLateTradeReportsResourceWithRawResponse,
    LateTradeReportsResourceWithStreamingResponse,
    AsyncLateTradeReportsResourceWithStreamingResponse,
)
from .recent_trade_reports import (
    RecentTradeReportsResource,
    AsyncRecentTradeReportsResource,
    RecentTradeReportsResourceWithRawResponse,
    AsyncRecentTradeReportsResourceWithRawResponse,
    RecentTradeReportsResourceWithStreamingResponse,
    AsyncRecentTradeReportsResourceWithStreamingResponse,
)

__all__ = ["CongressResource", "AsyncCongressResource"]


class CongressResource(SyncAPIResource):
    @cached_property
    def recent_trades(self) -> RecentTradesResource:
        return RecentTradesResource(self._client)

    @cached_property
    def late_trade_reports(self) -> LateTradeReportsResource:
        return LateTradeReportsResource(self._client)

    @cached_property
    def trader(self) -> TraderResource:
        return TraderResource(self._client)

    @cached_property
    def recent_trade_reports(self) -> RecentTradeReportsResource:
        return RecentTradeReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CongressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return CongressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CongressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return CongressResourceWithStreamingResponse(self)


class AsyncCongressResource(AsyncAPIResource):
    @cached_property
    def recent_trades(self) -> AsyncRecentTradesResource:
        return AsyncRecentTradesResource(self._client)

    @cached_property
    def late_trade_reports(self) -> AsyncLateTradeReportsResource:
        return AsyncLateTradeReportsResource(self._client)

    @cached_property
    def trader(self) -> AsyncTraderResource:
        return AsyncTraderResource(self._client)

    @cached_property
    def recent_trade_reports(self) -> AsyncRecentTradeReportsResource:
        return AsyncRecentTradeReportsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCongressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCongressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCongressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncCongressResourceWithStreamingResponse(self)


class CongressResourceWithRawResponse:
    def __init__(self, congress: CongressResource) -> None:
        self._congress = congress

    @cached_property
    def recent_trades(self) -> RecentTradesResourceWithRawResponse:
        return RecentTradesResourceWithRawResponse(self._congress.recent_trades)

    @cached_property
    def late_trade_reports(self) -> LateTradeReportsResourceWithRawResponse:
        return LateTradeReportsResourceWithRawResponse(self._congress.late_trade_reports)

    @cached_property
    def trader(self) -> TraderResourceWithRawResponse:
        return TraderResourceWithRawResponse(self._congress.trader)

    @cached_property
    def recent_trade_reports(self) -> RecentTradeReportsResourceWithRawResponse:
        return RecentTradeReportsResourceWithRawResponse(self._congress.recent_trade_reports)


class AsyncCongressResourceWithRawResponse:
    def __init__(self, congress: AsyncCongressResource) -> None:
        self._congress = congress

    @cached_property
    def recent_trades(self) -> AsyncRecentTradesResourceWithRawResponse:
        return AsyncRecentTradesResourceWithRawResponse(self._congress.recent_trades)

    @cached_property
    def late_trade_reports(self) -> AsyncLateTradeReportsResourceWithRawResponse:
        return AsyncLateTradeReportsResourceWithRawResponse(self._congress.late_trade_reports)

    @cached_property
    def trader(self) -> AsyncTraderResourceWithRawResponse:
        return AsyncTraderResourceWithRawResponse(self._congress.trader)

    @cached_property
    def recent_trade_reports(self) -> AsyncRecentTradeReportsResourceWithRawResponse:
        return AsyncRecentTradeReportsResourceWithRawResponse(self._congress.recent_trade_reports)


class CongressResourceWithStreamingResponse:
    def __init__(self, congress: CongressResource) -> None:
        self._congress = congress

    @cached_property
    def recent_trades(self) -> RecentTradesResourceWithStreamingResponse:
        return RecentTradesResourceWithStreamingResponse(self._congress.recent_trades)

    @cached_property
    def late_trade_reports(self) -> LateTradeReportsResourceWithStreamingResponse:
        return LateTradeReportsResourceWithStreamingResponse(self._congress.late_trade_reports)

    @cached_property
    def trader(self) -> TraderResourceWithStreamingResponse:
        return TraderResourceWithStreamingResponse(self._congress.trader)

    @cached_property
    def recent_trade_reports(self) -> RecentTradeReportsResourceWithStreamingResponse:
        return RecentTradeReportsResourceWithStreamingResponse(self._congress.recent_trade_reports)


class AsyncCongressResourceWithStreamingResponse:
    def __init__(self, congress: AsyncCongressResource) -> None:
        self._congress = congress

    @cached_property
    def recent_trades(self) -> AsyncRecentTradesResourceWithStreamingResponse:
        return AsyncRecentTradesResourceWithStreamingResponse(self._congress.recent_trades)

    @cached_property
    def late_trade_reports(self) -> AsyncLateTradeReportsResourceWithStreamingResponse:
        return AsyncLateTradeReportsResourceWithStreamingResponse(self._congress.late_trade_reports)

    @cached_property
    def trader(self) -> AsyncTraderResourceWithStreamingResponse:
        return AsyncTraderResourceWithStreamingResponse(self._congress.trader)

    @cached_property
    def recent_trade_reports(self) -> AsyncRecentTradeReportsResourceWithStreamingResponse:
        return AsyncRecentTradeReportsResourceWithStreamingResponse(self._congress.recent_trade_reports)
