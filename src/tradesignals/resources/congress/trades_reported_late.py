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
from ...types.congress import trades_reported_late_list_params
from ...types.congress.trades_reported_late_list_response import TradesReportedLateListResponse

__all__ = ["TradesReportedLateResource", "AsyncTradesReportedLateResource"]


class TradesReportedLateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TradesReportedLateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return TradesReportedLateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TradesReportedLateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return TradesReportedLateResourceWithStreamingResponse(self)

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
    ) -> Optional[TradesReportedLateListResponse]:
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
                    trades_reported_late_list_params.TradesReportedLateListParams,
                ),
                post_parser=DataWrapper[Optional[TradesReportedLateListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TradesReportedLateListResponse]], DataWrapper[TradesReportedLateListResponse]),
        )


class AsyncTradesReportedLateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTradesReportedLateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTradesReportedLateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTradesReportedLateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncTradesReportedLateResourceWithStreamingResponse(self)

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
    ) -> Optional[TradesReportedLateListResponse]:
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
                    trades_reported_late_list_params.TradesReportedLateListParams,
                ),
                post_parser=DataWrapper[Optional[TradesReportedLateListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TradesReportedLateListResponse]], DataWrapper[TradesReportedLateListResponse]),
        )


class TradesReportedLateResourceWithRawResponse:
    def __init__(self, trades_reported_late: TradesReportedLateResource) -> None:
        self._trades_reported_late = trades_reported_late

        self.list = to_raw_response_wrapper(
            trades_reported_late.list,
        )


class AsyncTradesReportedLateResourceWithRawResponse:
    def __init__(self, trades_reported_late: AsyncTradesReportedLateResource) -> None:
        self._trades_reported_late = trades_reported_late

        self.list = async_to_raw_response_wrapper(
            trades_reported_late.list,
        )


class TradesReportedLateResourceWithStreamingResponse:
    def __init__(self, trades_reported_late: TradesReportedLateResource) -> None:
        self._trades_reported_late = trades_reported_late

        self.list = to_streamed_response_wrapper(
            trades_reported_late.list,
        )


class AsyncTradesReportedLateResourceWithStreamingResponse:
    def __init__(self, trades_reported_late: AsyncTradesReportedLateResource) -> None:
        self._trades_reported_late = trades_reported_late

        self.list = async_to_streamed_response_wrapper(
            trades_reported_late.list,
        )
