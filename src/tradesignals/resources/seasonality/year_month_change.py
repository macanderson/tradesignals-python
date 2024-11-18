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
from ...types.seasonality.year_month_change_list_response import YearMonthChangeListResponse

__all__ = ["YearMonthChangeResource", "AsyncYearMonthChangeResource"]


class YearMonthChangeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> YearMonthChangeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return YearMonthChangeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> YearMonthChangeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return YearMonthChangeResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[YearMonthChangeListResponse]:
        """
        Returns the relative price change for all past months over multiple years.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/seasonality/{ticker}/year-month",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[YearMonthChangeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[YearMonthChangeListResponse]], DataWrapper[YearMonthChangeListResponse]),
        )


class AsyncYearMonthChangeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncYearMonthChangeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncYearMonthChangeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncYearMonthChangeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncYearMonthChangeResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[YearMonthChangeListResponse]:
        """
        Returns the relative price change for all past months over multiple years.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/seasonality/{ticker}/year-month",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[YearMonthChangeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[YearMonthChangeListResponse]], DataWrapper[YearMonthChangeListResponse]),
        )


class YearMonthChangeResourceWithRawResponse:
    def __init__(self, year_month_change: YearMonthChangeResource) -> None:
        self._year_month_change = year_month_change

        self.list = to_raw_response_wrapper(
            year_month_change.list,
        )


class AsyncYearMonthChangeResourceWithRawResponse:
    def __init__(self, year_month_change: AsyncYearMonthChangeResource) -> None:
        self._year_month_change = year_month_change

        self.list = async_to_raw_response_wrapper(
            year_month_change.list,
        )


class YearMonthChangeResourceWithStreamingResponse:
    def __init__(self, year_month_change: YearMonthChangeResource) -> None:
        self._year_month_change = year_month_change

        self.list = to_streamed_response_wrapper(
            year_month_change.list,
        )


class AsyncYearMonthChangeResourceWithStreamingResponse:
    def __init__(self, year_month_change: AsyncYearMonthChangeResource) -> None:
        self._year_month_change = year_month_change

        self.list = async_to_streamed_response_wrapper(
            year_month_change.list,
        )
