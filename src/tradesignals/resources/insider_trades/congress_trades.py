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
from ...types.insider_trades import congress_trade_list_params
from ...types.insider_trades.congress_trade_list_response import CongressTradeListResponse

__all__ = ["CongressTradesResource", "AsyncCongressTradesResource"]


class CongressTradesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CongressTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return CongressTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CongressTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return CongressTradesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        member: str | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CongressTradeListResponse:
        """Retrieve trading data reported by members of Congress.

        Filter by optional member
        and symbol.

        Args:
          date: Date to filter trades.

          member: Name of the Congress member to filter trades.

          symbol: Stock symbol to filter trades.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/congress/trades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "member": member,
                        "symbol": symbol,
                    },
                    congress_trade_list_params.CongressTradeListParams,
                ),
            ),
            cast_to=CongressTradeListResponse,
        )


class AsyncCongressTradesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCongressTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCongressTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCongressTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncCongressTradesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        member: str | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CongressTradeListResponse:
        """Retrieve trading data reported by members of Congress.

        Filter by optional member
        and symbol.

        Args:
          date: Date to filter trades.

          member: Name of the Congress member to filter trades.

          symbol: Stock symbol to filter trades.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/congress/trades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "member": member,
                        "symbol": symbol,
                    },
                    congress_trade_list_params.CongressTradeListParams,
                ),
            ),
            cast_to=CongressTradeListResponse,
        )


class CongressTradesResourceWithRawResponse:
    def __init__(self, congress_trades: CongressTradesResource) -> None:
        self._congress_trades = congress_trades

        self.list = to_raw_response_wrapper(
            congress_trades.list,
        )


class AsyncCongressTradesResourceWithRawResponse:
    def __init__(self, congress_trades: AsyncCongressTradesResource) -> None:
        self._congress_trades = congress_trades

        self.list = async_to_raw_response_wrapper(
            congress_trades.list,
        )


class CongressTradesResourceWithStreamingResponse:
    def __init__(self, congress_trades: CongressTradesResource) -> None:
        self._congress_trades = congress_trades

        self.list = to_streamed_response_wrapper(
            congress_trades.list,
        )


class AsyncCongressTradesResourceWithStreamingResponse:
    def __init__(self, congress_trades: AsyncCongressTradesResource) -> None:
        self._congress_trades = congress_trades

        self.list = async_to_streamed_response_wrapper(
            congress_trades.list,
        )
