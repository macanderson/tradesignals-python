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
from ...types.stock import net_prem_tick_list_params
from ..._base_client import make_request_options
from ...types.stock.net_prem_ticks_response import NetPremTicksResponse

__all__ = ["NetPremTicksResource", "AsyncNetPremTicksResource"]


class NetPremTicksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetPremTicksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return NetPremTicksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetPremTicksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return NetPremTicksResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetPremTicksResponse:
        """
        Returns the net premium ticks for a given ticker, useful for building a Net
        Premium chart.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/stock/{ticker}/net-prem-ticks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, net_prem_tick_list_params.NetPremTickListParams),
            ),
            cast_to=NetPremTicksResponse,
        )


class AsyncNetPremTicksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetPremTicksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetPremTicksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetPremTicksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncNetPremTicksResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetPremTicksResponse:
        """
        Returns the net premium ticks for a given ticker, useful for building a Net
        Premium chart.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/stock/{ticker}/net-prem-ticks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"date": date}, net_prem_tick_list_params.NetPremTickListParams),
            ),
            cast_to=NetPremTicksResponse,
        )


class NetPremTicksResourceWithRawResponse:
    def __init__(self, net_prem_ticks: NetPremTicksResource) -> None:
        self._net_prem_ticks = net_prem_ticks

        self.list = to_raw_response_wrapper(
            net_prem_ticks.list,
        )


class AsyncNetPremTicksResourceWithRawResponse:
    def __init__(self, net_prem_ticks: AsyncNetPremTicksResource) -> None:
        self._net_prem_ticks = net_prem_ticks

        self.list = async_to_raw_response_wrapper(
            net_prem_ticks.list,
        )


class NetPremTicksResourceWithStreamingResponse:
    def __init__(self, net_prem_ticks: NetPremTicksResource) -> None:
        self._net_prem_ticks = net_prem_ticks

        self.list = to_streamed_response_wrapper(
            net_prem_ticks.list,
        )


class AsyncNetPremTicksResourceWithStreamingResponse:
    def __init__(self, net_prem_ticks: AsyncNetPremTicksResource) -> None:
        self._net_prem_ticks = net_prem_ticks

        self.list = async_to_streamed_response_wrapper(
            net_prem_ticks.list,
        )