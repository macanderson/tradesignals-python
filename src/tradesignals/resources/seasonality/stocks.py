# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.seasonality import stock_retrieve_params
from ...types.seasonality.stock_retrieve_response import StockRetrieveResponse

__all__ = ["StocksResource", "AsyncStocksResource"]


class StocksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return StocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return StocksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        time_frame: Literal["daily", "weekly", "monthly", "yearly"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StockRetrieveResponse:
        """Retrieve seasonality data for a specific stock symbol.

        Filter by optional time
        frame.

        Args:
          time_frame: Time frame for seasonality data (e.g., 'monthly', 'weekly').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/api/seasonality/stocks/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"time_frame": time_frame}, stock_retrieve_params.StockRetrieveParams),
            ),
            cast_to=StockRetrieveResponse,
        )


class AsyncStocksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncStocksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        time_frame: Literal["daily", "weekly", "monthly", "yearly"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StockRetrieveResponse:
        """Retrieve seasonality data for a specific stock symbol.

        Filter by optional time
        frame.

        Args:
          time_frame: Time frame for seasonality data (e.g., 'monthly', 'weekly').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/api/seasonality/stocks/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"time_frame": time_frame}, stock_retrieve_params.StockRetrieveParams
                ),
            ),
            cast_to=StockRetrieveResponse,
        )


class StocksResourceWithRawResponse:
    def __init__(self, stocks: StocksResource) -> None:
        self._stocks = stocks

        self.retrieve = to_raw_response_wrapper(
            stocks.retrieve,
        )


class AsyncStocksResourceWithRawResponse:
    def __init__(self, stocks: AsyncStocksResource) -> None:
        self._stocks = stocks

        self.retrieve = async_to_raw_response_wrapper(
            stocks.retrieve,
        )


class StocksResourceWithStreamingResponse:
    def __init__(self, stocks: StocksResource) -> None:
        self._stocks = stocks

        self.retrieve = to_streamed_response_wrapper(
            stocks.retrieve,
        )


class AsyncStocksResourceWithStreamingResponse:
    def __init__(self, stocks: AsyncStocksResource) -> None:
        self._stocks = stocks

        self.retrieve = async_to_streamed_response_wrapper(
            stocks.retrieve,
        )
