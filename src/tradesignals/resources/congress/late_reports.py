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
from ...types.congress import late_report_list_params
from ...types.congress.late_report_list_response import LateReportListResponse

__all__ = ["LateReportsResource", "AsyncLateReportsResource"]


class LateReportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LateReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return LateReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LateReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return LateReportsResourceWithStreamingResponse(self)

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
    ) -> Optional[LateReportListResponse]:
        """Returns the recent late reports by congress members.

        If a date is given, will
        only return reports with a report date &le; the given input date.

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
            "/api/congress/late-reports",
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
                    late_report_list_params.LateReportListParams,
                ),
                post_parser=DataWrapper[Optional[LateReportListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LateReportListResponse]], DataWrapper[LateReportListResponse]),
        )


class AsyncLateReportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLateReportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLateReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLateReportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncLateReportsResourceWithStreamingResponse(self)

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
    ) -> Optional[LateReportListResponse]:
        """Returns the recent late reports by congress members.

        If a date is given, will
        only return reports with a report date &le; the given input date.

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
            "/api/congress/late-reports",
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
                    late_report_list_params.LateReportListParams,
                ),
                post_parser=DataWrapper[Optional[LateReportListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LateReportListResponse]], DataWrapper[LateReportListResponse]),
        )


class LateReportsResourceWithRawResponse:
    def __init__(self, late_reports: LateReportsResource) -> None:
        self._late_reports = late_reports

        self.list = to_raw_response_wrapper(
            late_reports.list,
        )


class AsyncLateReportsResourceWithRawResponse:
    def __init__(self, late_reports: AsyncLateReportsResource) -> None:
        self._late_reports = late_reports

        self.list = async_to_raw_response_wrapper(
            late_reports.list,
        )


class LateReportsResourceWithStreamingResponse:
    def __init__(self, late_reports: LateReportsResource) -> None:
        self._late_reports = late_reports

        self.list = to_streamed_response_wrapper(
            late_reports.list,
        )


class AsyncLateReportsResourceWithStreamingResponse:
    def __init__(self, late_reports: AsyncLateReportsResource) -> None:
        self._late_reports = late_reports

        self.list = async_to_streamed_response_wrapper(
            late_reports.list,
        )
