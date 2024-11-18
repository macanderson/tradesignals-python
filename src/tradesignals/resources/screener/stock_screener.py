# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
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
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.screener import stock_screener_list_params
from ...types.screener.stock_screener_list_response import StockScreenerListResponse

__all__ = ["StockScreenerResource", "AsyncStockScreenerResource"]


class StockScreenerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StockScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return StockScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StockScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return StockScreenerResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        has_dividends: bool | NotGiven = NOT_GIVEN,
        is_s_p_500: bool | NotGiven = NOT_GIVEN,
        issue_types: List[Literal["Common Stock", "ETF", "Index", "ADR"]] | NotGiven = NOT_GIVEN,
        max_marketcap: int | NotGiven = NOT_GIVEN,
        min_volume: int | NotGiven = NOT_GIVEN,
        order: Literal["premium", "call_volume", "put_volume", "marketcap"] | NotGiven = NOT_GIVEN,
        order_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[StockScreenerListResponse]:
        """
        A stock screener endpoint to screen the market for stocks by a variety of filter
        options.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/screener/stocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "has_dividends": has_dividends,
                        "is_s_p_500": is_s_p_500,
                        "issue_types": issue_types,
                        "max_marketcap": max_marketcap,
                        "min_volume": min_volume,
                        "order": order,
                        "order_direction": order_direction,
                    },
                    stock_screener_list_params.StockScreenerListParams,
                ),
                post_parser=DataWrapper[Optional[StockScreenerListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StockScreenerListResponse]], DataWrapper[StockScreenerListResponse]),
        )


class AsyncStockScreenerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStockScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStockScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStockScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncStockScreenerResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        has_dividends: bool | NotGiven = NOT_GIVEN,
        is_s_p_500: bool | NotGiven = NOT_GIVEN,
        issue_types: List[Literal["Common Stock", "ETF", "Index", "ADR"]] | NotGiven = NOT_GIVEN,
        max_marketcap: int | NotGiven = NOT_GIVEN,
        min_volume: int | NotGiven = NOT_GIVEN,
        order: Literal["premium", "call_volume", "put_volume", "marketcap"] | NotGiven = NOT_GIVEN,
        order_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[StockScreenerListResponse]:
        """
        A stock screener endpoint to screen the market for stocks by a variety of filter
        options.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/screener/stocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "has_dividends": has_dividends,
                        "is_s_p_500": is_s_p_500,
                        "issue_types": issue_types,
                        "max_marketcap": max_marketcap,
                        "min_volume": min_volume,
                        "order": order,
                        "order_direction": order_direction,
                    },
                    stock_screener_list_params.StockScreenerListParams,
                ),
                post_parser=DataWrapper[Optional[StockScreenerListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StockScreenerListResponse]], DataWrapper[StockScreenerListResponse]),
        )


class StockScreenerResourceWithRawResponse:
    def __init__(self, stock_screener: StockScreenerResource) -> None:
        self._stock_screener = stock_screener

        self.list = to_raw_response_wrapper(
            stock_screener.list,
        )


class AsyncStockScreenerResourceWithRawResponse:
    def __init__(self, stock_screener: AsyncStockScreenerResource) -> None:
        self._stock_screener = stock_screener

        self.list = async_to_raw_response_wrapper(
            stock_screener.list,
        )


class StockScreenerResourceWithStreamingResponse:
    def __init__(self, stock_screener: StockScreenerResource) -> None:
        self._stock_screener = stock_screener

        self.list = to_streamed_response_wrapper(
            stock_screener.list,
        )


class AsyncStockScreenerResourceWithStreamingResponse:
    def __init__(self, stock_screener: AsyncStockScreenerResource) -> None:
        self._stock_screener = stock_screener

        self.list = async_to_streamed_response_wrapper(
            stock_screener.list,
        )
