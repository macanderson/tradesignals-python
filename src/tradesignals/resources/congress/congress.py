# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .recent_reports import (
    RecentReportsResource,
    AsyncRecentReportsResource,
    RecentReportsResourceWithRawResponse,
    AsyncRecentReportsResourceWithRawResponse,
    RecentReportsResourceWithStreamingResponse,
    AsyncRecentReportsResourceWithStreamingResponse,
)
from .trades_by_member import (
    TradesByMemberResource,
    AsyncTradesByMemberResource,
    TradesByMemberResourceWithRawResponse,
    AsyncTradesByMemberResourceWithRawResponse,
    TradesByMemberResourceWithStreamingResponse,
    AsyncTradesByMemberResourceWithStreamingResponse,
)
from .trades_reported_late import (
    TradesReportedLateResource,
    AsyncTradesReportedLateResource,
    TradesReportedLateResourceWithRawResponse,
    AsyncTradesReportedLateResourceWithRawResponse,
    TradesReportedLateResourceWithStreamingResponse,
    AsyncTradesReportedLateResourceWithStreamingResponse,
)
from .congress_member_trades import (
    CongressMemberTradesResource,
    AsyncCongressMemberTradesResource,
    CongressMemberTradesResourceWithRawResponse,
    AsyncCongressMemberTradesResourceWithRawResponse,
    CongressMemberTradesResourceWithStreamingResponse,
    AsyncCongressMemberTradesResourceWithStreamingResponse,
)

__all__ = ["CongressResource", "AsyncCongressResource"]


class CongressResource(SyncAPIResource):
    """
    -> Congress endpoints provides insights into the trading activity of members of congress including the US Senate and the US House of Representatives.
    """

    @cached_property
    def congress_member_trades(self) -> CongressMemberTradesResource:
        return CongressMemberTradesResource(self._client)

    @cached_property
    def trades_reported_late(self) -> TradesReportedLateResource:
        return TradesReportedLateResource(self._client)

    @cached_property
    def trades_by_member(self) -> TradesByMemberResource:
        return TradesByMemberResource(self._client)

    @cached_property
    def recent_reports(self) -> RecentReportsResource:
        return RecentReportsResource(self._client)

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
    """
    -> Congress endpoints provides insights into the trading activity of members of congress including the US Senate and the US House of Representatives.
    """

    @cached_property
    def congress_member_trades(self) -> AsyncCongressMemberTradesResource:
        return AsyncCongressMemberTradesResource(self._client)

    @cached_property
    def trades_reported_late(self) -> AsyncTradesReportedLateResource:
        return AsyncTradesReportedLateResource(self._client)

    @cached_property
    def trades_by_member(self) -> AsyncTradesByMemberResource:
        return AsyncTradesByMemberResource(self._client)

    @cached_property
    def recent_reports(self) -> AsyncRecentReportsResource:
        return AsyncRecentReportsResource(self._client)

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
    def congress_member_trades(self) -> CongressMemberTradesResourceWithRawResponse:
        return CongressMemberTradesResourceWithRawResponse(self._congress.congress_member_trades)

    @cached_property
    def trades_reported_late(self) -> TradesReportedLateResourceWithRawResponse:
        return TradesReportedLateResourceWithRawResponse(self._congress.trades_reported_late)

    @cached_property
    def trades_by_member(self) -> TradesByMemberResourceWithRawResponse:
        return TradesByMemberResourceWithRawResponse(self._congress.trades_by_member)

    @cached_property
    def recent_reports(self) -> RecentReportsResourceWithRawResponse:
        return RecentReportsResourceWithRawResponse(self._congress.recent_reports)


class AsyncCongressResourceWithRawResponse:
    def __init__(self, congress: AsyncCongressResource) -> None:
        self._congress = congress

    @cached_property
    def congress_member_trades(self) -> AsyncCongressMemberTradesResourceWithRawResponse:
        return AsyncCongressMemberTradesResourceWithRawResponse(self._congress.congress_member_trades)

    @cached_property
    def trades_reported_late(self) -> AsyncTradesReportedLateResourceWithRawResponse:
        return AsyncTradesReportedLateResourceWithRawResponse(self._congress.trades_reported_late)

    @cached_property
    def trades_by_member(self) -> AsyncTradesByMemberResourceWithRawResponse:
        return AsyncTradesByMemberResourceWithRawResponse(self._congress.trades_by_member)

    @cached_property
    def recent_reports(self) -> AsyncRecentReportsResourceWithRawResponse:
        return AsyncRecentReportsResourceWithRawResponse(self._congress.recent_reports)


class CongressResourceWithStreamingResponse:
    def __init__(self, congress: CongressResource) -> None:
        self._congress = congress

    @cached_property
    def congress_member_trades(self) -> CongressMemberTradesResourceWithStreamingResponse:
        return CongressMemberTradesResourceWithStreamingResponse(self._congress.congress_member_trades)

    @cached_property
    def trades_reported_late(self) -> TradesReportedLateResourceWithStreamingResponse:
        return TradesReportedLateResourceWithStreamingResponse(self._congress.trades_reported_late)

    @cached_property
    def trades_by_member(self) -> TradesByMemberResourceWithStreamingResponse:
        return TradesByMemberResourceWithStreamingResponse(self._congress.trades_by_member)

    @cached_property
    def recent_reports(self) -> RecentReportsResourceWithStreamingResponse:
        return RecentReportsResourceWithStreamingResponse(self._congress.recent_reports)


class AsyncCongressResourceWithStreamingResponse:
    def __init__(self, congress: AsyncCongressResource) -> None:
        self._congress = congress

    @cached_property
    def congress_member_trades(self) -> AsyncCongressMemberTradesResourceWithStreamingResponse:
        return AsyncCongressMemberTradesResourceWithStreamingResponse(self._congress.congress_member_trades)

    @cached_property
    def trades_reported_late(self) -> AsyncTradesReportedLateResourceWithStreamingResponse:
        return AsyncTradesReportedLateResourceWithStreamingResponse(self._congress.trades_reported_late)

    @cached_property
    def trades_by_member(self) -> AsyncTradesByMemberResourceWithStreamingResponse:
        return AsyncTradesByMemberResourceWithStreamingResponse(self._congress.trades_by_member)

    @cached_property
    def recent_reports(self) -> AsyncRecentReportsResourceWithStreamingResponse:
        return AsyncRecentReportsResourceWithStreamingResponse(self._congress.recent_reports)
