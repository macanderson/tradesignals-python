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
from ...types.darkpool import recent_trade_list_params
from ...types.darkpool.recent_trade_list_response import RecentTradeListResponse

__all__ = ["RecentTradesResource", "AsyncRecentTradesResource"]


class RecentTradesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecentTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return RecentTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecentTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return RecentTradesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecentTradeListResponse]:
        """
        -> Returns recent Darkpool trades for all securities listed on either NASDAQ or
        NYSE.

        Args:
          date: Date to filter darkpool transactions.

          limit: How many items to return. Default is 100. Max is 200. Minimum is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/darkpool/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                    },
                    recent_trade_list_params.RecentTradeListParams,
                ),
                post_parser=DataWrapper[Optional[RecentTradeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecentTradeListResponse]], DataWrapper[RecentTradeListResponse]),
        )


class AsyncRecentTradesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecentTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecentTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecentTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncRecentTradesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecentTradeListResponse]:
        """
        -> Returns recent Darkpool trades for all securities listed on either NASDAQ or
        NYSE.

        Args:
          date: Date to filter darkpool transactions.

          limit: How many items to return. Default is 100. Max is 200. Minimum is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/darkpool/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                    },
                    recent_trade_list_params.RecentTradeListParams,
                ),
                post_parser=DataWrapper[Optional[RecentTradeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecentTradeListResponse]], DataWrapper[RecentTradeListResponse]),
        )


class RecentTradesResourceWithRawResponse:
    def __init__(self, recent_trades: RecentTradesResource) -> None:
        self._recent_trades = recent_trades

        self.list = to_raw_response_wrapper(
            recent_trades.list,
        )


class AsyncRecentTradesResourceWithRawResponse:
    def __init__(self, recent_trades: AsyncRecentTradesResource) -> None:
        self._recent_trades = recent_trades

        self.list = async_to_raw_response_wrapper(
            recent_trades.list,
        )


class RecentTradesResourceWithStreamingResponse:
    def __init__(self, recent_trades: RecentTradesResource) -> None:
        self._recent_trades = recent_trades

        self.list = to_streamed_response_wrapper(
            recent_trades.list,
        )


class AsyncRecentTradesResourceWithStreamingResponse:
    def __init__(self, recent_trades: AsyncRecentTradesResource) -> None:
        self._recent_trades = recent_trades

        self.list = async_to_streamed_response_wrapper(
            recent_trades.list,
        )
