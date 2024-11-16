# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ..._base_client import make_request_options
from ...types.economic_calendars import fda_calendar_retrieve_params
from ...types.economic_calendars.fda_calendar_retrieve_response import FdaCalendarRetrieveResponse

__all__ = ["FdaCalendarResource", "AsyncFdaCalendarResource"]


class FdaCalendarResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FdaCalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return FdaCalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FdaCalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return FdaCalendarResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FdaCalendarRetrieveResponse:
        """Retrieve upcoming FDA approval dates and drug event data.

        Filter by optional
        start and end dates.

        Args:
          end_date: End date for the FDA calendar data.

          start_date: Start date for the FDA calendar data.

          symbol: Stock symbol to filter FDA events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/calendar/fda",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "symbol": symbol,
                    },
                    fda_calendar_retrieve_params.FdaCalendarRetrieveParams,
                ),
            ),
            cast_to=FdaCalendarRetrieveResponse,
        )


class AsyncFdaCalendarResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFdaCalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFdaCalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFdaCalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncFdaCalendarResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FdaCalendarRetrieveResponse:
        """Retrieve upcoming FDA approval dates and drug event data.

        Filter by optional
        start and end dates.

        Args:
          end_date: End date for the FDA calendar data.

          start_date: Start date for the FDA calendar data.

          symbol: Stock symbol to filter FDA events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/calendar/fda",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "symbol": symbol,
                    },
                    fda_calendar_retrieve_params.FdaCalendarRetrieveParams,
                ),
            ),
            cast_to=FdaCalendarRetrieveResponse,
        )


class FdaCalendarResourceWithRawResponse:
    def __init__(self, fda_calendar: FdaCalendarResource) -> None:
        self._fda_calendar = fda_calendar

        self.retrieve = to_raw_response_wrapper(
            fda_calendar.retrieve,
        )


class AsyncFdaCalendarResourceWithRawResponse:
    def __init__(self, fda_calendar: AsyncFdaCalendarResource) -> None:
        self._fda_calendar = fda_calendar

        self.retrieve = async_to_raw_response_wrapper(
            fda_calendar.retrieve,
        )


class FdaCalendarResourceWithStreamingResponse:
    def __init__(self, fda_calendar: FdaCalendarResource) -> None:
        self._fda_calendar = fda_calendar

        self.retrieve = to_streamed_response_wrapper(
            fda_calendar.retrieve,
        )


class AsyncFdaCalendarResourceWithStreamingResponse:
    def __init__(self, fda_calendar: AsyncFdaCalendarResource) -> None:
        self._fda_calendar = fda_calendar

        self.retrieve = async_to_streamed_response_wrapper(
            fda_calendar.retrieve,
        )
