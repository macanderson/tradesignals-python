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
from ...types.market_data.fda_calendar_list_response import FdaCalendarListResponse

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

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FdaCalendarListResponse]:
        """Returns the FDA calendar for the current week."""
        return self._get(
            "/api/market/fda-calendar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[FdaCalendarListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FdaCalendarListResponse]], DataWrapper[FdaCalendarListResponse]),
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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FdaCalendarListResponse]:
        """Returns the FDA calendar for the current week."""
        return await self._get(
            "/api/market/fda-calendar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[FdaCalendarListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FdaCalendarListResponse]], DataWrapper[FdaCalendarListResponse]),
        )


class FdaCalendarResourceWithRawResponse:
    def __init__(self, fda_calendar: FdaCalendarResource) -> None:
        self._fda_calendar = fda_calendar

        self.list = to_raw_response_wrapper(
            fda_calendar.list,
        )


class AsyncFdaCalendarResourceWithRawResponse:
    def __init__(self, fda_calendar: AsyncFdaCalendarResource) -> None:
        self._fda_calendar = fda_calendar

        self.list = async_to_raw_response_wrapper(
            fda_calendar.list,
        )


class FdaCalendarResourceWithStreamingResponse:
    def __init__(self, fda_calendar: FdaCalendarResource) -> None:
        self._fda_calendar = fda_calendar

        self.list = to_streamed_response_wrapper(
            fda_calendar.list,
        )


class AsyncFdaCalendarResourceWithStreamingResponse:
    def __init__(self, fda_calendar: AsyncFdaCalendarResource) -> None:
        self._fda_calendar = fda_calendar

        self.list = async_to_streamed_response_wrapper(
            fda_calendar.list,
        )
