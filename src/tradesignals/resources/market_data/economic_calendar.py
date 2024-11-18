# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.market_data.economic_calendar_list_response import EconomicCalendarListResponse

__all__ = ["EconomicCalendarResource", "AsyncEconomicCalendarResource"]


class EconomicCalendarResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EconomicCalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return EconomicCalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EconomicCalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return EconomicCalendarResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EconomicCalendarListResponse]:
        """Returns the economic calendar for the current and next week."""
        return self._get(
            "/api/market/economic-calendar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[EconomicCalendarListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EconomicCalendarListResponse]], DataWrapper[EconomicCalendarListResponse]),
        )


class AsyncEconomicCalendarResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEconomicCalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEconomicCalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEconomicCalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncEconomicCalendarResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EconomicCalendarListResponse]:
        """Returns the economic calendar for the current and next week."""
        return await self._get(
            "/api/market/economic-calendar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[EconomicCalendarListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EconomicCalendarListResponse]], DataWrapper[EconomicCalendarListResponse]),
        )


class EconomicCalendarResourceWithRawResponse:
    def __init__(self, economic_calendar: EconomicCalendarResource) -> None:
        self._economic_calendar = economic_calendar

        self.list = to_raw_response_wrapper(
            economic_calendar.list,
        )


class AsyncEconomicCalendarResourceWithRawResponse:
    def __init__(self, economic_calendar: AsyncEconomicCalendarResource) -> None:
        self._economic_calendar = economic_calendar

        self.list = async_to_raw_response_wrapper(
            economic_calendar.list,
        )


class EconomicCalendarResourceWithStreamingResponse:
    def __init__(self, economic_calendar: EconomicCalendarResource) -> None:
        self._economic_calendar = economic_calendar

        self.list = to_streamed_response_wrapper(
            economic_calendar.list,
        )


class AsyncEconomicCalendarResourceWithStreamingResponse:
    def __init__(self, economic_calendar: AsyncEconomicCalendarResource) -> None:
        self._economic_calendar = economic_calendar

        self.list = async_to_streamed_response_wrapper(
            economic_calendar.list,
        )
