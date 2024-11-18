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
from ...types.seasonality.stock_price_change_list_response import StockPriceChangeListResponse

__all__ = ["StockPriceChangesResource", "AsyncStockPriceChangesResource"]


class StockPriceChangesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StockPriceChangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return StockPriceChangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StockPriceChangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return StockPriceChangesResourceWithStreamingResponse(self)

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
    ) -> Optional[StockPriceChangeListResponse]:
        """
        Returns the relative price change for all past months over multiple years.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/seasonality/{ticker}/year-month",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[StockPriceChangeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StockPriceChangeListResponse]], DataWrapper[StockPriceChangeListResponse]),
        )


class AsyncStockPriceChangesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStockPriceChangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStockPriceChangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStockPriceChangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncStockPriceChangesResourceWithStreamingResponse(self)

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
    ) -> Optional[StockPriceChangeListResponse]:
        """
        Returns the relative price change for all past months over multiple years.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/seasonality/{ticker}/year-month",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[StockPriceChangeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StockPriceChangeListResponse]], DataWrapper[StockPriceChangeListResponse]),
        )


class StockPriceChangesResourceWithRawResponse:
    def __init__(self, stock_price_changes: StockPriceChangesResource) -> None:
        self._stock_price_changes = stock_price_changes

        self.list = to_raw_response_wrapper(
            stock_price_changes.list,
        )


class AsyncStockPriceChangesResourceWithRawResponse:
    def __init__(self, stock_price_changes: AsyncStockPriceChangesResource) -> None:
        self._stock_price_changes = stock_price_changes

        self.list = async_to_raw_response_wrapper(
            stock_price_changes.list,
        )


class StockPriceChangesResourceWithStreamingResponse:
    def __init__(self, stock_price_changes: StockPriceChangesResource) -> None:
        self._stock_price_changes = stock_price_changes

        self.list = to_streamed_response_wrapper(
            stock_price_changes.list,
        )


class AsyncStockPriceChangesResourceWithStreamingResponse:
    def __init__(self, stock_price_changes: AsyncStockPriceChangesResource) -> None:
        self._stock_price_changes = stock_price_changes

        self.list = async_to_streamed_response_wrapper(
            stock_price_changes.list,
        )
