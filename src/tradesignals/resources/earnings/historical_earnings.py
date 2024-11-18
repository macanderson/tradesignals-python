# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import make_request_options
from ...types.earnings.historical_earnings_response import HistoricalEarningsResponse

__all__ = ["HistoricalEarningsResource", "AsyncHistoricalEarningsResource"]


class HistoricalEarningsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoricalEarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return HistoricalEarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoricalEarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return HistoricalEarningsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        ticker: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoricalEarningsResponse:
        """
        Returns the past earnings for the given ticker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/earnings/{ticker}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HistoricalEarningsResponse,
        )


class AsyncHistoricalEarningsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoricalEarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHistoricalEarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoricalEarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncHistoricalEarningsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        ticker: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoricalEarningsResponse:
        """
        Returns the past earnings for the given ticker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/earnings/{ticker}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HistoricalEarningsResponse,
        )


class HistoricalEarningsResourceWithRawResponse:
    def __init__(self, historical_earnings: HistoricalEarningsResource) -> None:
        self._historical_earnings = historical_earnings

        self.retrieve = to_raw_response_wrapper(
            historical_earnings.retrieve,
        )


class AsyncHistoricalEarningsResourceWithRawResponse:
    def __init__(self, historical_earnings: AsyncHistoricalEarningsResource) -> None:
        self._historical_earnings = historical_earnings

        self.retrieve = async_to_raw_response_wrapper(
            historical_earnings.retrieve,
        )


class HistoricalEarningsResourceWithStreamingResponse:
    def __init__(self, historical_earnings: HistoricalEarningsResource) -> None:
        self._historical_earnings = historical_earnings

        self.retrieve = to_streamed_response_wrapper(
            historical_earnings.retrieve,
        )


class AsyncHistoricalEarningsResourceWithStreamingResponse:
    def __init__(self, historical_earnings: AsyncHistoricalEarningsResource) -> None:
        self._historical_earnings = historical_earnings

        self.retrieve = async_to_streamed_response_wrapper(
            historical_earnings.retrieve,
        )
