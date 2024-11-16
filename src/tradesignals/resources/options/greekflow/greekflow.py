# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from .expiry import (
    ExpiryResource,
    AsyncExpiryResource,
    ExpiryResourceWithRawResponse,
    AsyncExpiryResourceWithRawResponse,
    ExpiryResourceWithStreamingResponse,
    AsyncExpiryResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.options import greekflow_list_params
from ....types.options.greekflow_list_response import GreekflowListResponse

__all__ = ["GreekflowResource", "AsyncGreekflowResource"]


class GreekflowResource(SyncAPIResource):
    @cached_property
    def expiry(self) -> ExpiryResource:
        return ExpiryResource(self._client)

    @cached_property
    def with_raw_response(self) -> GreekflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return GreekflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GreekflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return GreekflowResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        max_delta: float | NotGiven = NOT_GIVEN,
        min_delta: float | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreekflowListResponse:
        """
        Retrieve options flow data with Greek calculations.

        Args:
          date: Date to filter the Greek flow data. ISO 8601 format.

          max_delta: Maximum delta value.

          min_delta: Minimum delta value.

          symbol: Stock symbol to filter the Greek flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/options/greekflow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "max_delta": max_delta,
                        "min_delta": min_delta,
                        "symbol": symbol,
                    },
                    greekflow_list_params.GreekflowListParams,
                ),
            ),
            cast_to=GreekflowListResponse,
        )


class AsyncGreekflowResource(AsyncAPIResource):
    @cached_property
    def expiry(self) -> AsyncExpiryResource:
        return AsyncExpiryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGreekflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGreekflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGreekflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncGreekflowResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        max_delta: float | NotGiven = NOT_GIVEN,
        min_delta: float | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreekflowListResponse:
        """
        Retrieve options flow data with Greek calculations.

        Args:
          date: Date to filter the Greek flow data. ISO 8601 format.

          max_delta: Maximum delta value.

          min_delta: Minimum delta value.

          symbol: Stock symbol to filter the Greek flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/options/greekflow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "max_delta": max_delta,
                        "min_delta": min_delta,
                        "symbol": symbol,
                    },
                    greekflow_list_params.GreekflowListParams,
                ),
            ),
            cast_to=GreekflowListResponse,
        )


class GreekflowResourceWithRawResponse:
    def __init__(self, greekflow: GreekflowResource) -> None:
        self._greekflow = greekflow

        self.list = to_raw_response_wrapper(
            greekflow.list,
        )

    @cached_property
    def expiry(self) -> ExpiryResourceWithRawResponse:
        return ExpiryResourceWithRawResponse(self._greekflow.expiry)


class AsyncGreekflowResourceWithRawResponse:
    def __init__(self, greekflow: AsyncGreekflowResource) -> None:
        self._greekflow = greekflow

        self.list = async_to_raw_response_wrapper(
            greekflow.list,
        )

    @cached_property
    def expiry(self) -> AsyncExpiryResourceWithRawResponse:
        return AsyncExpiryResourceWithRawResponse(self._greekflow.expiry)


class GreekflowResourceWithStreamingResponse:
    def __init__(self, greekflow: GreekflowResource) -> None:
        self._greekflow = greekflow

        self.list = to_streamed_response_wrapper(
            greekflow.list,
        )

    @cached_property
    def expiry(self) -> ExpiryResourceWithStreamingResponse:
        return ExpiryResourceWithStreamingResponse(self._greekflow.expiry)


class AsyncGreekflowResourceWithStreamingResponse:
    def __init__(self, greekflow: AsyncGreekflowResource) -> None:
        self._greekflow = greekflow

        self.list = async_to_streamed_response_wrapper(
            greekflow.list,
        )

    @cached_property
    def expiry(self) -> AsyncExpiryResourceWithStreamingResponse:
        return AsyncExpiryResourceWithStreamingResponse(self._greekflow.expiry)
