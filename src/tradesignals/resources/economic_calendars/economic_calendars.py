# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ...types import economic_calendar_list_params
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
from .fda_calendar import (
    FdaCalendarResource,
    AsyncFdaCalendarResource,
    FdaCalendarResourceWithRawResponse,
    AsyncFdaCalendarResourceWithRawResponse,
    FdaCalendarResourceWithStreamingResponse,
    AsyncFdaCalendarResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.economic_calendar_list_response import EconomicCalendarListResponse

__all__ = ["EconomicCalendarsResource", "AsyncEconomicCalendarsResource"]


class EconomicCalendarsResource(SyncAPIResource):
    @cached_property
    def fda_calendar(self) -> FdaCalendarResource:
        return FdaCalendarResource(self._client)

    @cached_property
    def with_raw_response(self) -> EconomicCalendarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return EconomicCalendarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EconomicCalendarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return EconomicCalendarsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        country: str | NotGiven = NOT_GIVEN,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EconomicCalendarListResponse:
        """Retrieve upcoming economic events and data releases.

        Filter by optional start
        and end dates.

        Args:
          country: Country to filter events.

          end_date: End date for the economic calendar data.

          start_date: Start date for the economic calendar data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/calendar/economic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    economic_calendar_list_params.EconomicCalendarListParams,
                ),
            ),
            cast_to=EconomicCalendarListResponse,
        )


class AsyncEconomicCalendarsResource(AsyncAPIResource):
    @cached_property
    def fda_calendar(self) -> AsyncFdaCalendarResource:
        return AsyncFdaCalendarResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEconomicCalendarsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEconomicCalendarsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEconomicCalendarsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncEconomicCalendarsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        country: str | NotGiven = NOT_GIVEN,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EconomicCalendarListResponse:
        """Retrieve upcoming economic events and data releases.

        Filter by optional start
        and end dates.

        Args:
          country: Country to filter events.

          end_date: End date for the economic calendar data.

          start_date: Start date for the economic calendar data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/calendar/economic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    economic_calendar_list_params.EconomicCalendarListParams,
                ),
            ),
            cast_to=EconomicCalendarListResponse,
        )


class EconomicCalendarsResourceWithRawResponse:
    def __init__(self, economic_calendars: EconomicCalendarsResource) -> None:
        self._economic_calendars = economic_calendars

        self.list = to_raw_response_wrapper(
            economic_calendars.list,
        )

    @cached_property
    def fda_calendar(self) -> FdaCalendarResourceWithRawResponse:
        return FdaCalendarResourceWithRawResponse(self._economic_calendars.fda_calendar)


class AsyncEconomicCalendarsResourceWithRawResponse:
    def __init__(self, economic_calendars: AsyncEconomicCalendarsResource) -> None:
        self._economic_calendars = economic_calendars

        self.list = async_to_raw_response_wrapper(
            economic_calendars.list,
        )

    @cached_property
    def fda_calendar(self) -> AsyncFdaCalendarResourceWithRawResponse:
        return AsyncFdaCalendarResourceWithRawResponse(self._economic_calendars.fda_calendar)


class EconomicCalendarsResourceWithStreamingResponse:
    def __init__(self, economic_calendars: EconomicCalendarsResource) -> None:
        self._economic_calendars = economic_calendars

        self.list = to_streamed_response_wrapper(
            economic_calendars.list,
        )

    @cached_property
    def fda_calendar(self) -> FdaCalendarResourceWithStreamingResponse:
        return FdaCalendarResourceWithStreamingResponse(self._economic_calendars.fda_calendar)


class AsyncEconomicCalendarsResourceWithStreamingResponse:
    def __init__(self, economic_calendars: AsyncEconomicCalendarsResource) -> None:
        self._economic_calendars = economic_calendars

        self.list = async_to_streamed_response_wrapper(
            economic_calendars.list,
        )

    @cached_property
    def fda_calendar(self) -> AsyncFdaCalendarResourceWithStreamingResponse:
        return AsyncFdaCalendarResourceWithStreamingResponse(self._economic_calendars.fda_calendar)
