# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import make_request_options
from ...types.stocks.price_retrieve_response import PriceRetrieveResponse

__all__ = ["PriceResource", "AsyncPriceResource"]


class PriceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PriceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return PriceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PriceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return PriceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceRetrieveResponse:
        """
        Retrieve the current price for a stock symbol.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/api/stocks/price/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceRetrieveResponse,
        )


class AsyncPriceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPriceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPriceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPriceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncPriceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriceRetrieveResponse:
        """
        Retrieve the current price for a stock symbol.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/api/stocks/price/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriceRetrieveResponse,
        )


class PriceResourceWithRawResponse:
    def __init__(self, price: PriceResource) -> None:
        self._price = price

        self.retrieve = to_raw_response_wrapper(
            price.retrieve,
        )


class AsyncPriceResourceWithRawResponse:
    def __init__(self, price: AsyncPriceResource) -> None:
        self._price = price

        self.retrieve = async_to_raw_response_wrapper(
            price.retrieve,
        )


class PriceResourceWithStreamingResponse:
    def __init__(self, price: PriceResource) -> None:
        self._price = price

        self.retrieve = to_streamed_response_wrapper(
            price.retrieve,
        )


class AsyncPriceResourceWithStreamingResponse:
    def __init__(self, price: AsyncPriceResource) -> None:
        self._price = price

        self.retrieve = async_to_streamed_response_wrapper(
            price.retrieve,
        )
