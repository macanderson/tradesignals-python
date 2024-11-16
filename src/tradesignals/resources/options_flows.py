# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import options_flow_list_params, options_flow_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.options_flow_list_response import OptionsFlowListResponse
from ..types.options_flow_retrieve_response import OptionsFlowRetrieveResponse

__all__ = ["OptionsFlowsResource", "AsyncOptionsFlowsResource"]


class OptionsFlowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptionsFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionsFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OptionsFlowsResourceWithStreamingResponse(self)

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
    ) -> OptionsFlowRetrieveResponse:
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
                    options_flow_retrieve_params.OptionsFlowRetrieveParams,
                ),
            ),
            cast_to=OptionsFlowRetrieveResponse,
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
    ) -> OptionsFlowListResponse:
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
                    options_flow_list_params.OptionsFlowListParams,
                ),
            ),
            cast_to=OptionsFlowListResponse,
        )


class AsyncOptionsFlowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptionsFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOptionsFlowsResourceWithStreamingResponse(self)

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
    ) -> OptionsFlowRetrieveResponse:
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
                    options_flow_retrieve_params.OptionsFlowRetrieveParams,
                ),
            ),
            cast_to=OptionsFlowRetrieveResponse,
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
    ) -> OptionsFlowListResponse:
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
                    options_flow_list_params.OptionsFlowListParams,
                ),
            ),
            cast_to=OptionsFlowListResponse,
        )


class OptionsFlowsResourceWithRawResponse:
    def __init__(self, options_flows: OptionsFlowsResource) -> None:
        self._options_flows = options_flows

        self.retrieve = to_raw_response_wrapper(
            options_flows.retrieve,
        )
        self.list = to_raw_response_wrapper(
            options_flows.list,
        )


class AsyncOptionsFlowsResourceWithRawResponse:
    def __init__(self, options_flows: AsyncOptionsFlowsResource) -> None:
        self._options_flows = options_flows

        self.retrieve = async_to_raw_response_wrapper(
            options_flows.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            options_flows.list,
        )


class OptionsFlowsResourceWithStreamingResponse:
    def __init__(self, options_flows: OptionsFlowsResource) -> None:
        self._options_flows = options_flows

        self.retrieve = to_streamed_response_wrapper(
            options_flows.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            options_flows.list,
        )


class AsyncOptionsFlowsResourceWithStreamingResponse:
    def __init__(self, options_flows: AsyncOptionsFlowsResource) -> None:
        self._options_flows = options_flows

        self.retrieve = async_to_streamed_response_wrapper(
            options_flows.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            options_flows.list,
        )
