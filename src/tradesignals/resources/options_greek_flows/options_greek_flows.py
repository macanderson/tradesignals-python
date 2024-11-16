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
from ...types import options_greek_flow_list_params
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
from ...types.options_greek_flow_list_response import OptionsGreekFlowListResponse

__all__ = ["OptionsGreekFlowsResource", "AsyncOptionsGreekFlowsResource"]


class OptionsGreekFlowsResource(SyncAPIResource):
    @cached_property
    def expiry(self) -> ExpiryResource:
        return ExpiryResource(self._client)

    @cached_property
    def with_raw_response(self) -> OptionsGreekFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionsGreekFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsGreekFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OptionsGreekFlowsResourceWithStreamingResponse(self)

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
    ) -> OptionsGreekFlowListResponse:
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
                    options_greek_flow_list_params.OptionsGreekFlowListParams,
                ),
            ),
            cast_to=OptionsGreekFlowListResponse,
        )


class AsyncOptionsGreekFlowsResource(AsyncAPIResource):
    @cached_property
    def expiry(self) -> AsyncExpiryResource:
        return AsyncExpiryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOptionsGreekFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsGreekFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsGreekFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOptionsGreekFlowsResourceWithStreamingResponse(self)

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
    ) -> OptionsGreekFlowListResponse:
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
                    options_greek_flow_list_params.OptionsGreekFlowListParams,
                ),
            ),
            cast_to=OptionsGreekFlowListResponse,
        )


class OptionsGreekFlowsResourceWithRawResponse:
    def __init__(self, options_greek_flows: OptionsGreekFlowsResource) -> None:
        self._options_greek_flows = options_greek_flows

        self.list = to_raw_response_wrapper(
            options_greek_flows.list,
        )

    @cached_property
    def expiry(self) -> ExpiryResourceWithRawResponse:
        return ExpiryResourceWithRawResponse(self._options_greek_flows.expiry)


class AsyncOptionsGreekFlowsResourceWithRawResponse:
    def __init__(self, options_greek_flows: AsyncOptionsGreekFlowsResource) -> None:
        self._options_greek_flows = options_greek_flows

        self.list = async_to_raw_response_wrapper(
            options_greek_flows.list,
        )

    @cached_property
    def expiry(self) -> AsyncExpiryResourceWithRawResponse:
        return AsyncExpiryResourceWithRawResponse(self._options_greek_flows.expiry)


class OptionsGreekFlowsResourceWithStreamingResponse:
    def __init__(self, options_greek_flows: OptionsGreekFlowsResource) -> None:
        self._options_greek_flows = options_greek_flows

        self.list = to_streamed_response_wrapper(
            options_greek_flows.list,
        )

    @cached_property
    def expiry(self) -> ExpiryResourceWithStreamingResponse:
        return ExpiryResourceWithStreamingResponse(self._options_greek_flows.expiry)


class AsyncOptionsGreekFlowsResourceWithStreamingResponse:
    def __init__(self, options_greek_flows: AsyncOptionsGreekFlowsResource) -> None:
        self._options_greek_flows = options_greek_flows

        self.list = async_to_streamed_response_wrapper(
            options_greek_flows.list,
        )

    @cached_property
    def expiry(self) -> AsyncExpiryResourceWithStreamingResponse:
        return AsyncExpiryResourceWithStreamingResponse(self._options_greek_flows.expiry)
