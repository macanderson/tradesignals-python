# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .late_reports import (
    LateReportsResource,
    AsyncLateReportsResource,
    LateReportsResourceWithRawResponse,
    AsyncLateReportsResourceWithRawResponse,
    LateReportsResourceWithStreamingResponse,
    AsyncLateReportsResourceWithStreamingResponse,
)
from .recent_trades import (
    RecentTradesResource,
    AsyncRecentTradesResource,
    RecentTradesResourceWithRawResponse,
    AsyncRecentTradesResourceWithRawResponse,
    RecentTradesResourceWithStreamingResponse,
    AsyncRecentTradesResourceWithStreamingResponse,
)
from .recent_reports import (
    RecentReportsResource,
    AsyncRecentReportsResource,
    RecentReportsResourceWithRawResponse,
    AsyncRecentReportsResourceWithRawResponse,
    RecentReportsResourceWithStreamingResponse,
    AsyncRecentReportsResourceWithStreamingResponse,
)
from .congress_trader import (
    CongressTraderResource,
    AsyncCongressTraderResource,
    CongressTraderResourceWithRawResponse,
    AsyncCongressTraderResourceWithRawResponse,
    CongressTraderResourceWithStreamingResponse,
    AsyncCongressTraderResourceWithStreamingResponse,
)

__all__ = ["CongressResource", "AsyncCongressResource"]


class CongressResource(SyncAPIResource):
    @cached_property
    def recent_trades(self) -> RecentTradesResource:
        return RecentTradesResource(self._client)

    @cached_property
    def late_reports(self) -> LateReportsResource:
        return LateReportsResource(self._client)

    @cached_property
    def congress_trader(self) -> CongressTraderResource:
        return CongressTraderResource(self._client)

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
    @cached_property
    def recent_trades(self) -> AsyncRecentTradesResource:
        return AsyncRecentTradesResource(self._client)

    @cached_property
    def late_reports(self) -> AsyncLateReportsResource:
        return AsyncLateReportsResource(self._client)

    @cached_property
    def congress_trader(self) -> AsyncCongressTraderResource:
        return AsyncCongressTraderResource(self._client)

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
    def recent_trades(self) -> RecentTradesResourceWithRawResponse:
        return RecentTradesResourceWithRawResponse(self._congress.recent_trades)

    @cached_property
    def late_reports(self) -> LateReportsResourceWithRawResponse:
        return LateReportsResourceWithRawResponse(self._congress.late_reports)

    @cached_property
    def congress_trader(self) -> CongressTraderResourceWithRawResponse:
        return CongressTraderResourceWithRawResponse(self._congress.congress_trader)

    @cached_property
    def recent_reports(self) -> RecentReportsResourceWithRawResponse:
        return RecentReportsResourceWithRawResponse(self._congress.recent_reports)


class AsyncCongressResourceWithRawResponse:
    def __init__(self, congress: AsyncCongressResource) -> None:
        self._congress = congress

    @cached_property
    def recent_trades(self) -> AsyncRecentTradesResourceWithRawResponse:
        return AsyncRecentTradesResourceWithRawResponse(self._congress.recent_trades)

    @cached_property
    def late_reports(self) -> AsyncLateReportsResourceWithRawResponse:
        return AsyncLateReportsResourceWithRawResponse(self._congress.late_reports)

    @cached_property
    def congress_trader(self) -> AsyncCongressTraderResourceWithRawResponse:
        return AsyncCongressTraderResourceWithRawResponse(self._congress.congress_trader)

    @cached_property
    def recent_reports(self) -> AsyncRecentReportsResourceWithRawResponse:
        return AsyncRecentReportsResourceWithRawResponse(self._congress.recent_reports)


class CongressResourceWithStreamingResponse:
    def __init__(self, congress: CongressResource) -> None:
        self._congress = congress

    @cached_property
    def recent_trades(self) -> RecentTradesResourceWithStreamingResponse:
        return RecentTradesResourceWithStreamingResponse(self._congress.recent_trades)

    @cached_property
    def late_reports(self) -> LateReportsResourceWithStreamingResponse:
        return LateReportsResourceWithStreamingResponse(self._congress.late_reports)

    @cached_property
    def congress_trader(self) -> CongressTraderResourceWithStreamingResponse:
        return CongressTraderResourceWithStreamingResponse(self._congress.congress_trader)

    @cached_property
    def recent_reports(self) -> RecentReportsResourceWithStreamingResponse:
        return RecentReportsResourceWithStreamingResponse(self._congress.recent_reports)


class AsyncCongressResourceWithStreamingResponse:
    def __init__(self, congress: AsyncCongressResource) -> None:
        self._congress = congress

    @cached_property
    def recent_trades(self) -> AsyncRecentTradesResourceWithStreamingResponse:
        return AsyncRecentTradesResourceWithStreamingResponse(self._congress.recent_trades)

    @cached_property
    def late_reports(self) -> AsyncLateReportsResourceWithStreamingResponse:
        return AsyncLateReportsResourceWithStreamingResponse(self._congress.late_reports)

    @cached_property
    def congress_trader(self) -> AsyncCongressTraderResourceWithStreamingResponse:
        return AsyncCongressTraderResourceWithStreamingResponse(self._congress.congress_trader)

    @cached_property
    def recent_reports(self) -> AsyncRecentReportsResourceWithStreamingResponse:
        return AsyncRecentReportsResourceWithStreamingResponse(self._congress.recent_reports)
