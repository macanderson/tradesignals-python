# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.seasonality.stock_average_return_list_response import StockAverageReturnListResponse

__all__ = ["StockAverageReturnsResource", "AsyncStockAverageReturnsResource"]


class StockAverageReturnsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StockAverageReturnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return StockAverageReturnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StockAverageReturnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return StockAverageReturnsResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[StockAverageReturnListResponse]:
        """
        Returns the average return by month for the given ticker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/seasonality/{ticker}/monthly",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[StockAverageReturnListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StockAverageReturnListResponse]], DataWrapper[StockAverageReturnListResponse]),
        )


class AsyncStockAverageReturnsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStockAverageReturnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStockAverageReturnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStockAverageReturnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncStockAverageReturnsResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[StockAverageReturnListResponse]:
        """
        Returns the average return by month for the given ticker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/seasonality/{ticker}/monthly",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[StockAverageReturnListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StockAverageReturnListResponse]], DataWrapper[StockAverageReturnListResponse]),
        )


class StockAverageReturnsResourceWithRawResponse:
    def __init__(self, stock_average_returns: StockAverageReturnsResource) -> None:
        self._stock_average_returns = stock_average_returns

        self.list = to_raw_response_wrapper(
            stock_average_returns.list,
        )


class AsyncStockAverageReturnsResourceWithRawResponse:
    def __init__(self, stock_average_returns: AsyncStockAverageReturnsResource) -> None:
        self._stock_average_returns = stock_average_returns

        self.list = async_to_raw_response_wrapper(
            stock_average_returns.list,
        )


class StockAverageReturnsResourceWithStreamingResponse:
    def __init__(self, stock_average_returns: StockAverageReturnsResource) -> None:
        self._stock_average_returns = stock_average_returns

        self.list = to_streamed_response_wrapper(
            stock_average_returns.list,
        )


class AsyncStockAverageReturnsResourceWithStreamingResponse:
    def __init__(self, stock_average_returns: AsyncStockAverageReturnsResource) -> None:
        self._stock_average_returns = stock_average_returns

        self.list = async_to_streamed_response_wrapper(
            stock_average_returns.list,
        )
