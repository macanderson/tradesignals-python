# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
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
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.darkpool import trades_by_ticker_list_params
from ...types.darkpool.trades_by_ticker_list_response import TradesByTickerListResponse

__all__ = ["TradesByTickerResource", "AsyncTradesByTickerResource"]


class TradesByTickerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TradesByTickerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return TradesByTickerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TradesByTickerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return TradesByTickerResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        newer_than: str | NotGiven = NOT_GIVEN,
        older_than: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TradesByTickerListResponse]:
        """-> Returns the darkpool trades for the given ticker on a given day.

        Date must be
        the current or a past date. If no date is given, returns data for the
        current/last market day.

        Args:
          date: Date to filter darkpool transactions.

          limit: How many items to return. Default is 100. Max is 200. Minimum is 1.

          newer_than: The unix time in milliseconds or seconds at which no older results will be
              returned. Can be used with newer_than to paginate by time. Also accepts an ISO
              date example "2024-01-25".

          older_than: The unix time in milliseconds or seconds at which no newer results will be
              returned. Can be used with newer_than to paginate by time. Also accepts an ISO
              date example "2024-01-25".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/darkpool/{ticker}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "newer_than": newer_than,
                        "older_than": older_than,
                    },
                    trades_by_ticker_list_params.TradesByTickerListParams,
                ),
                post_parser=DataWrapper[Optional[TradesByTickerListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TradesByTickerListResponse]], DataWrapper[TradesByTickerListResponse]),
        )


class AsyncTradesByTickerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTradesByTickerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTradesByTickerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTradesByTickerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncTradesByTickerResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        newer_than: str | NotGiven = NOT_GIVEN,
        older_than: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TradesByTickerListResponse]:
        """-> Returns the darkpool trades for the given ticker on a given day.

        Date must be
        the current or a past date. If no date is given, returns data for the
        current/last market day.

        Args:
          date: Date to filter darkpool transactions.

          limit: How many items to return. Default is 100. Max is 200. Minimum is 1.

          newer_than: The unix time in milliseconds or seconds at which no older results will be
              returned. Can be used with newer_than to paginate by time. Also accepts an ISO
              date example "2024-01-25".

          older_than: The unix time in milliseconds or seconds at which no newer results will be
              returned. Can be used with newer_than to paginate by time. Also accepts an ISO
              date example "2024-01-25".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/darkpool/{ticker}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "newer_than": newer_than,
                        "older_than": older_than,
                    },
                    trades_by_ticker_list_params.TradesByTickerListParams,
                ),
                post_parser=DataWrapper[Optional[TradesByTickerListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TradesByTickerListResponse]], DataWrapper[TradesByTickerListResponse]),
        )


class TradesByTickerResourceWithRawResponse:
    def __init__(self, trades_by_ticker: TradesByTickerResource) -> None:
        self._trades_by_ticker = trades_by_ticker

        self.list = to_raw_response_wrapper(
            trades_by_ticker.list,
        )


class AsyncTradesByTickerResourceWithRawResponse:
    def __init__(self, trades_by_ticker: AsyncTradesByTickerResource) -> None:
        self._trades_by_ticker = trades_by_ticker

        self.list = async_to_raw_response_wrapper(
            trades_by_ticker.list,
        )


class TradesByTickerResourceWithStreamingResponse:
    def __init__(self, trades_by_ticker: TradesByTickerResource) -> None:
        self._trades_by_ticker = trades_by_ticker

        self.list = to_streamed_response_wrapper(
            trades_by_ticker.list,
        )


class AsyncTradesByTickerResourceWithStreamingResponse:
    def __init__(self, trades_by_ticker: AsyncTradesByTickerResource) -> None:
        self._trades_by_ticker = trades_by_ticker

        self.list = async_to_streamed_response_wrapper(
            trades_by_ticker.list,
        )
