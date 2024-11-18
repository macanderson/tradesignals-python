# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...types.market_data import insider_trade_list_params
from ...types.market_data.insider_trade_list_response import InsiderTradeListResponse

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
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[InsiderTradeListResponse]:
        """
        Returns the total amount of purchases & sells as well as notional values for
        insider transactions across the market.

        Args:
          limit: How many items to return. If no limit is given, returns all matching data.
              Minimum value is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/market/insider-buy-sells",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, insider_trade_list_params.InsiderTradeListParams),
                post_parser=DataWrapper[Optional[InsiderTradeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InsiderTradeListResponse]], DataWrapper[InsiderTradeListResponse]),
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
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[InsiderTradeListResponse]:
        """
        Returns the total amount of purchases & sells as well as notional values for
        insider transactions across the market.

        Args:
          limit: How many items to return. If no limit is given, returns all matching data.
              Minimum value is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/market/insider-buy-sells",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, insider_trade_list_params.InsiderTradeListParams),
                post_parser=DataWrapper[Optional[InsiderTradeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InsiderTradeListResponse]], DataWrapper[InsiderTradeListResponse]),
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
