# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import date
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
from ...types.market_data import market_oi_change_list_params
from ...types.market_data.market_oi_change_list_response import MarketOiChangeListResponse

__all__ = ["MarketOiChangeResource", "AsyncMarketOiChangeResource"]


class MarketOiChangeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketOiChangeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return MarketOiChangeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketOiChangeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return MarketOiChangeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MarketOiChangeListResponse]:
        """
        Returns non-Index/non-ETF contracts and OI change data with the highest OI
        change.

        Args:
          date: A trading date in the format of YYYY-MM-DD. Defaults to the last trading date.

          limit: How many items to return. Default is 100. Max is 200. Min is 1.

          order: Whether to sort descending or ascending. Default is descending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/market/oi-change",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "order": order,
                    },
                    market_oi_change_list_params.MarketOiChangeListParams,
                ),
                post_parser=DataWrapper[Optional[MarketOiChangeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MarketOiChangeListResponse]], DataWrapper[MarketOiChangeListResponse]),
        )


class AsyncMarketOiChangeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketOiChangeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketOiChangeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketOiChangeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncMarketOiChangeResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MarketOiChangeListResponse]:
        """
        Returns non-Index/non-ETF contracts and OI change data with the highest OI
        change.

        Args:
          date: A trading date in the format of YYYY-MM-DD. Defaults to the last trading date.

          limit: How many items to return. Default is 100. Max is 200. Min is 1.

          order: Whether to sort descending or ascending. Default is descending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/market/oi-change",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "order": order,
                    },
                    market_oi_change_list_params.MarketOiChangeListParams,
                ),
                post_parser=DataWrapper[Optional[MarketOiChangeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MarketOiChangeListResponse]], DataWrapper[MarketOiChangeListResponse]),
        )


class MarketOiChangeResourceWithRawResponse:
    def __init__(self, market_oi_change: MarketOiChangeResource) -> None:
        self._market_oi_change = market_oi_change

        self.list = to_raw_response_wrapper(
            market_oi_change.list,
        )


class AsyncMarketOiChangeResourceWithRawResponse:
    def __init__(self, market_oi_change: AsyncMarketOiChangeResource) -> None:
        self._market_oi_change = market_oi_change

        self.list = async_to_raw_response_wrapper(
            market_oi_change.list,
        )


class MarketOiChangeResourceWithStreamingResponse:
    def __init__(self, market_oi_change: MarketOiChangeResource) -> None:
        self._market_oi_change = market_oi_change

        self.list = to_streamed_response_wrapper(
            market_oi_change.list,
        )


class AsyncMarketOiChangeResourceWithStreamingResponse:
    def __init__(self, market_oi_change: AsyncMarketOiChangeResource) -> None:
        self._market_oi_change = market_oi_change

        self.list = async_to_streamed_response_wrapper(
            market_oi_change.list,
        )
