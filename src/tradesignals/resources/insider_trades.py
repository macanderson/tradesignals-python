# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import insider_trade_list_params
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
from ..types.insider_trade_list_response import InsiderTradeListResponse

__all__ = ["InsiderTradesResource", "AsyncInsiderTradesResource"]


class InsiderTradesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InsiderTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return InsiderTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsiderTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return InsiderTradesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        insider: str | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        transaction_type: Literal["Buy", "Sell"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsiderTradeListResponse:
        """Retrieve data on insider buys and sells.

        Filter by optional symbol, date, and
        insider name.

        Args:
          date: Date to filter insider trades.

          insider: Name of the insider.

          symbol: Stock symbol to filter insider trades.

          transaction_type: Type of transaction (Buy or Sell).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/insider/trades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "insider": insider,
                        "symbol": symbol,
                        "transaction_type": transaction_type,
                    },
                    insider_trade_list_params.InsiderTradeListParams,
                ),
            ),
            cast_to=InsiderTradeListResponse,
        )


class AsyncInsiderTradesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInsiderTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsiderTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsiderTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncInsiderTradesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        insider: str | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        transaction_type: Literal["Buy", "Sell"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InsiderTradeListResponse:
        """Retrieve data on insider buys and sells.

        Filter by optional symbol, date, and
        insider name.

        Args:
          date: Date to filter insider trades.

          insider: Name of the insider.

          symbol: Stock symbol to filter insider trades.

          transaction_type: Type of transaction (Buy or Sell).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/insider/trades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "insider": insider,
                        "symbol": symbol,
                        "transaction_type": transaction_type,
                    },
                    insider_trade_list_params.InsiderTradeListParams,
                ),
            ),
            cast_to=InsiderTradeListResponse,
        )


class InsiderTradesResourceWithRawResponse:
    def __init__(self, insider_trades: InsiderTradesResource) -> None:
        self._insider_trades = insider_trades

        self.list = to_raw_response_wrapper(
            insider_trades.list,
        )


class AsyncInsiderTradesResourceWithRawResponse:
    def __init__(self, insider_trades: AsyncInsiderTradesResource) -> None:
        self._insider_trades = insider_trades

        self.list = async_to_raw_response_wrapper(
            insider_trades.list,
        )


class InsiderTradesResourceWithStreamingResponse:
    def __init__(self, insider_trades: InsiderTradesResource) -> None:
        self._insider_trades = insider_trades

        self.list = to_streamed_response_wrapper(
            insider_trades.list,
        )


class AsyncInsiderTradesResourceWithStreamingResponse:
    def __init__(self, insider_trades: AsyncInsiderTradesResource) -> None:
        self._insider_trades = insider_trades

        self.list = async_to_streamed_response_wrapper(
            insider_trades.list,
        )
