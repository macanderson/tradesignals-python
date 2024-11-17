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
from ...types.screeners import stock_finder_list_params
from ...types.screeners.stock_finder_list_response import StockFinderListResponse

__all__ = ["StockFinderResource", "AsyncStockFinderResource"]


class StockFinderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StockFinderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return StockFinderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StockFinderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return StockFinderResourceWithStreamingResponse(self)

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
    ) -> Optional[StockFinderListResponse]:
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
                    stock_finder_list_params.StockFinderListParams,
                ),
                post_parser=DataWrapper[Optional[StockFinderListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StockFinderListResponse]], DataWrapper[StockFinderListResponse]),
        )


class AsyncStockFinderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStockFinderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStockFinderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStockFinderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncStockFinderResourceWithStreamingResponse(self)

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
    ) -> Optional[StockFinderListResponse]:
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
                    stock_finder_list_params.StockFinderListParams,
                ),
                post_parser=DataWrapper[Optional[StockFinderListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[StockFinderListResponse]], DataWrapper[StockFinderListResponse]),
        )


class StockFinderResourceWithRawResponse:
    def __init__(self, stock_finder: StockFinderResource) -> None:
        self._stock_finder = stock_finder

        self.list = to_raw_response_wrapper(
            stock_finder.list,
        )


class AsyncStockFinderResourceWithRawResponse:
    def __init__(self, stock_finder: AsyncStockFinderResource) -> None:
        self._stock_finder = stock_finder

        self.list = async_to_raw_response_wrapper(
            stock_finder.list,
        )


class StockFinderResourceWithStreamingResponse:
    def __init__(self, stock_finder: StockFinderResource) -> None:
        self._stock_finder = stock_finder

        self.list = to_streamed_response_wrapper(
            stock_finder.list,
        )


class AsyncStockFinderResourceWithStreamingResponse:
    def __init__(self, stock_finder: AsyncStockFinderResource) -> None:
        self._stock_finder = stock_finder

        self.list = async_to_streamed_response_wrapper(
            stock_finder.list,
        )
