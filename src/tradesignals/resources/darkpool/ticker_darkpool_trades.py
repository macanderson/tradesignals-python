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
from ...types.darkpool import ticker_darkpool_trade_list_params
from ...types.darkpool.ticker_darkpool_trade_list_response import TickerDarkpoolTradeListResponse

__all__ = ["TickerDarkpoolTradesResource", "AsyncTickerDarkpoolTradesResource"]


class TickerDarkpoolTradesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TickerDarkpoolTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return TickerDarkpoolTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TickerDarkpoolTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return TickerDarkpoolTradesResourceWithStreamingResponse(self)

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
    ) -> Optional[TickerDarkpoolTradeListResponse]:
        """-> Returns the darkpool trades for the given ticker on a given day.

        Date must be
        the current or a past date. If no date is given, returns data for the
        current/last market day.

        Args:
          date: Date to filter darkpool transactions.

          limit: How many items to return. Default is 100. Max is 200. Minimum is 1.

          newer_than: -> The unix time in milliseconds or seconds at which no older results will be
              returned. Can be used with newer_than to paginate by time. Also accepts an ISO
              date example "2024-01-25".

          older_than: -> The unix time in milliseconds or seconds at which no newer results will be
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
                    ticker_darkpool_trade_list_params.TickerDarkpoolTradeListParams,
                ),
                post_parser=DataWrapper[Optional[TickerDarkpoolTradeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TickerDarkpoolTradeListResponse]], DataWrapper[TickerDarkpoolTradeListResponse]),
        )


class AsyncTickerDarkpoolTradesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTickerDarkpoolTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTickerDarkpoolTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTickerDarkpoolTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncTickerDarkpoolTradesResourceWithStreamingResponse(self)

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
    ) -> Optional[TickerDarkpoolTradeListResponse]:
        """-> Returns the darkpool trades for the given ticker on a given day.

        Date must be
        the current or a past date. If no date is given, returns data for the
        current/last market day.

        Args:
          date: Date to filter darkpool transactions.

          limit: How many items to return. Default is 100. Max is 200. Minimum is 1.

          newer_than: -> The unix time in milliseconds or seconds at which no older results will be
              returned. Can be used with newer_than to paginate by time. Also accepts an ISO
              date example "2024-01-25".

          older_than: -> The unix time in milliseconds or seconds at which no newer results will be
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
                    ticker_darkpool_trade_list_params.TickerDarkpoolTradeListParams,
                ),
                post_parser=DataWrapper[Optional[TickerDarkpoolTradeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TickerDarkpoolTradeListResponse]], DataWrapper[TickerDarkpoolTradeListResponse]),
        )


class TickerDarkpoolTradesResourceWithRawResponse:
    def __init__(self, ticker_darkpool_trades: TickerDarkpoolTradesResource) -> None:
        self._ticker_darkpool_trades = ticker_darkpool_trades

        self.list = to_raw_response_wrapper(
            ticker_darkpool_trades.list,
        )


class AsyncTickerDarkpoolTradesResourceWithRawResponse:
    def __init__(self, ticker_darkpool_trades: AsyncTickerDarkpoolTradesResource) -> None:
        self._ticker_darkpool_trades = ticker_darkpool_trades

        self.list = async_to_raw_response_wrapper(
            ticker_darkpool_trades.list,
        )


class TickerDarkpoolTradesResourceWithStreamingResponse:
    def __init__(self, ticker_darkpool_trades: TickerDarkpoolTradesResource) -> None:
        self._ticker_darkpool_trades = ticker_darkpool_trades

        self.list = to_streamed_response_wrapper(
            ticker_darkpool_trades.list,
        )


class AsyncTickerDarkpoolTradesResourceWithStreamingResponse:
    def __init__(self, ticker_darkpool_trades: AsyncTickerDarkpoolTradesResource) -> None:
        self._ticker_darkpool_trades = ticker_darkpool_trades

        self.list = async_to_streamed_response_wrapper(
            ticker_darkpool_trades.list,
        )
