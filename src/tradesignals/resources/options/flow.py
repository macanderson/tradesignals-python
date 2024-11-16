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
from ...types.options import flow_list_params, flow_retrieve_params
from ...types.options.flow_list_response import FlowListResponse
from ...types.options.flow_retrieve_response import FlowRetrieveResponse

__all__ = ["FlowResource", "AsyncFlowResource"]


class FlowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return FlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return FlowResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        max_premium: float | NotGiven = NOT_GIVEN,
        min_premium: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowRetrieveResponse:
        """
        Retrieve options flow data for a specific symbol.

        Args:
          date: Date to filter the options flow data. ISO 8601 format.

          max_premium: Maximum premium to filter the options flow data.

          min_premium: Minimum premium to filter the options flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/api/options/flow/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "max_premium": max_premium,
                        "min_premium": min_premium,
                    },
                    flow_retrieve_params.FlowRetrieveParams,
                ),
            ),
            cast_to=FlowRetrieveResponse,
        )

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        max_premium: float | NotGiven = NOT_GIVEN,
        min_premium: float | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowListResponse:
        """Retrieve options flow data.

        Args:
          date: Date to filter the options flow data.

        ISO 8601 format.

          max_premium: Maximum premium to filter the options flow data.

          min_premium: Minimum premium to filter the options flow data.

          symbol: Stock symbol to filter the options flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/options/flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "max_premium": max_premium,
                        "min_premium": min_premium,
                        "symbol": symbol,
                    },
                    flow_list_params.FlowListParams,
                ),
            ),
            cast_to=FlowListResponse,
        )


class AsyncFlowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncFlowResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        max_premium: float | NotGiven = NOT_GIVEN,
        min_premium: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowRetrieveResponse:
        """
        Retrieve options flow data for a specific symbol.

        Args:
          date: Date to filter the options flow data. ISO 8601 format.

          max_premium: Maximum premium to filter the options flow data.

          min_premium: Minimum premium to filter the options flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/api/options/flow/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "max_premium": max_premium,
                        "min_premium": min_premium,
                    },
                    flow_retrieve_params.FlowRetrieveParams,
                ),
            ),
            cast_to=FlowRetrieveResponse,
        )

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        max_premium: float | NotGiven = NOT_GIVEN,
        min_premium: float | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FlowListResponse:
        """Retrieve options flow data.

        Args:
          date: Date to filter the options flow data.

        ISO 8601 format.

          max_premium: Maximum premium to filter the options flow data.

          min_premium: Minimum premium to filter the options flow data.

          symbol: Stock symbol to filter the options flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/options/flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "max_premium": max_premium,
                        "min_premium": min_premium,
                        "symbol": symbol,
                    },
                    flow_list_params.FlowListParams,
                ),
            ),
            cast_to=FlowListResponse,
        )


class FlowResourceWithRawResponse:
    def __init__(self, flow: FlowResource) -> None:
        self._flow = flow

        self.retrieve = to_raw_response_wrapper(
            flow.retrieve,
        )
        self.list = to_raw_response_wrapper(
            flow.list,
        )


class AsyncFlowResourceWithRawResponse:
    def __init__(self, flow: AsyncFlowResource) -> None:
        self._flow = flow

        self.retrieve = async_to_raw_response_wrapper(
            flow.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            flow.list,
        )


class FlowResourceWithStreamingResponse:
    def __init__(self, flow: FlowResource) -> None:
        self._flow = flow

        self.retrieve = to_streamed_response_wrapper(
            flow.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            flow.list,
        )


class AsyncFlowResourceWithStreamingResponse:
    def __init__(self, flow: AsyncFlowResource) -> None:
        self._flow = flow

        self.retrieve = async_to_streamed_response_wrapper(
            flow.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            flow.list,
        )
