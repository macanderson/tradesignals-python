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
from ...types.stock import flow_per_strike_list_params
from ..._base_client import make_request_options
from ...types.stock.flow_per_strike_response import FlowPerStrikeResponse

__all__ = ["FlowPerStrikeResource", "AsyncFlowPerStrikeResource"]


class FlowPerStrikeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlowPerStrikeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return FlowPerStrikeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlowPerStrikeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return FlowPerStrikeResourceWithStreamingResponse(self)

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
    ) -> FlowPerStrikeResponse:
        """
        Returns the option flow per strike for a given trading day.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/stock/{ticker}/flow-per-strike",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, flow_per_strike_list_params.FlowPerStrikeListParams),
            ),
            cast_to=FlowPerStrikeResponse,
        )


class AsyncFlowPerStrikeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlowPerStrikeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlowPerStrikeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlowPerStrikeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncFlowPerStrikeResourceWithStreamingResponse(self)

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
    ) -> FlowPerStrikeResponse:
        """
        Returns the option flow per strike for a given trading day.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/stock/{ticker}/flow-per-strike",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"date": date}, flow_per_strike_list_params.FlowPerStrikeListParams),
            ),
            cast_to=FlowPerStrikeResponse,
        )


class FlowPerStrikeResourceWithRawResponse:
    def __init__(self, flow_per_strike: FlowPerStrikeResource) -> None:
        self._flow_per_strike = flow_per_strike

        self.list = to_raw_response_wrapper(
            flow_per_strike.list,
        )


class AsyncFlowPerStrikeResourceWithRawResponse:
    def __init__(self, flow_per_strike: AsyncFlowPerStrikeResource) -> None:
        self._flow_per_strike = flow_per_strike

        self.list = async_to_raw_response_wrapper(
            flow_per_strike.list,
        )


class FlowPerStrikeResourceWithStreamingResponse:
    def __init__(self, flow_per_strike: FlowPerStrikeResource) -> None:
        self._flow_per_strike = flow_per_strike

        self.list = to_streamed_response_wrapper(
            flow_per_strike.list,
        )


class AsyncFlowPerStrikeResourceWithStreamingResponse:
    def __init__(self, flow_per_strike: AsyncFlowPerStrikeResource) -> None:
        self._flow_per_strike = flow_per_strike

        self.list = async_to_streamed_response_wrapper(
            flow_per_strike.list,
        )
