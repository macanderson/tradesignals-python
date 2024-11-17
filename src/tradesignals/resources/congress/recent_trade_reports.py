# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import date

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.congress import recent_trade_report_list_params
from ...types.congress.recent_trade_report_list_response import RecentTradeReportListResponse

__all__ = ["RecentTradeReportsResource", "AsyncRecentTradeReportsResource"]


class RecentTradeReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecentTradeReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return RecentTradeReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecentTradeReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return RecentTradeReportsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecentTradeReportListResponse]:
        """Returns the latest reported trades by congress members.

        If a date is given, will
        only return reports with a transaction date &le; the given input date.

        Args:
          date: A trading date in the format of YYYY-MM-DD. This is optional and by default the
              last trading date.

          limit: How many items to return. Default&colon; 100. Max&colon; 200. Min&colon; 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/congress/recent-reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                    },
                    recent_trade_report_list_params.RecentTradeReportListParams,
                ),
                post_parser=DataWrapper[Optional[RecentTradeReportListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecentTradeReportListResponse]], DataWrapper[RecentTradeReportListResponse]),
        )


class AsyncRecentTradeReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecentTradeReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecentTradeReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecentTradeReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncRecentTradeReportsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecentTradeReportListResponse]:
        """Returns the latest reported trades by congress members.

        If a date is given, will
        only return reports with a transaction date &le; the given input date.

        Args:
          date: A trading date in the format of YYYY-MM-DD. This is optional and by default the
              last trading date.

          limit: How many items to return. Default&colon; 100. Max&colon; 200. Min&colon; 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/congress/recent-reports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                    },
                    recent_trade_report_list_params.RecentTradeReportListParams,
                ),
                post_parser=DataWrapper[Optional[RecentTradeReportListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecentTradeReportListResponse]], DataWrapper[RecentTradeReportListResponse]),
        )


class RecentTradeReportsResourceWithRawResponse:
    def __init__(self, recent_trade_reports: RecentTradeReportsResource) -> None:
        self._recent_trade_reports = recent_trade_reports

        self.list = to_raw_response_wrapper(
            recent_trade_reports.list,
        )


class AsyncRecentTradeReportsResourceWithRawResponse:
    def __init__(self, recent_trade_reports: AsyncRecentTradeReportsResource) -> None:
        self._recent_trade_reports = recent_trade_reports

        self.list = async_to_raw_response_wrapper(
            recent_trade_reports.list,
        )


class RecentTradeReportsResourceWithStreamingResponse:
    def __init__(self, recent_trade_reports: RecentTradeReportsResource) -> None:
        self._recent_trade_reports = recent_trade_reports

        self.list = to_streamed_response_wrapper(
            recent_trade_reports.list,
        )


class AsyncRecentTradeReportsResourceWithStreamingResponse:
    def __init__(self, recent_trade_reports: AsyncRecentTradeReportsResource) -> None:
        self._recent_trade_reports = recent_trade_reports

        self.list = async_to_streamed_response_wrapper(
            recent_trade_reports.list,
        )
