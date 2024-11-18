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
from ...types.market_data import market_tide_list_params
from ...types.market_data.market_tide_list_response import MarketTideListResponse

__all__ = ["MarketTideResource", "AsyncMarketTideResource"]


class MarketTideResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketTideResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return MarketTideResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketTideResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return MarketTideResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        interval_5m: bool | NotGiven = NOT_GIVEN,
        otm_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MarketTideListResponse]:
        """
        Provides real-time data based on a proprietary formula examining market-wide
        options activity while filtering out noise.

        Args:
          date: A trading date in the format of YYYY-MM-DD. Defaults to the last trading date.

          interval_5m: Return data in 5-minute intervals.

          otm_only: Only include out-of-the-money transactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/market/market-tide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "interval_5m": interval_5m,
                        "otm_only": otm_only,
                    },
                    market_tide_list_params.MarketTideListParams,
                ),
                post_parser=DataWrapper[Optional[MarketTideListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MarketTideListResponse]], DataWrapper[MarketTideListResponse]),
        )


class AsyncMarketTideResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketTideResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketTideResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketTideResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncMarketTideResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        interval_5m: bool | NotGiven = NOT_GIVEN,
        otm_only: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MarketTideListResponse]:
        """
        Provides real-time data based on a proprietary formula examining market-wide
        options activity while filtering out noise.

        Args:
          date: A trading date in the format of YYYY-MM-DD. Defaults to the last trading date.

          interval_5m: Return data in 5-minute intervals.

          otm_only: Only include out-of-the-money transactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/market/market-tide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "interval_5m": interval_5m,
                        "otm_only": otm_only,
                    },
                    market_tide_list_params.MarketTideListParams,
                ),
                post_parser=DataWrapper[Optional[MarketTideListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MarketTideListResponse]], DataWrapper[MarketTideListResponse]),
        )


class MarketTideResourceWithRawResponse:
    def __init__(self, market_tide: MarketTideResource) -> None:
        self._market_tide = market_tide

        self.list = to_raw_response_wrapper(
            market_tide.list,
        )


class AsyncMarketTideResourceWithRawResponse:
    def __init__(self, market_tide: AsyncMarketTideResource) -> None:
        self._market_tide = market_tide

        self.list = async_to_raw_response_wrapper(
            market_tide.list,
        )


class MarketTideResourceWithStreamingResponse:
    def __init__(self, market_tide: MarketTideResource) -> None:
        self._market_tide = market_tide

        self.list = to_streamed_response_wrapper(
            market_tide.list,
        )


class AsyncMarketTideResourceWithStreamingResponse:
    def __init__(self, market_tide: AsyncMarketTideResource) -> None:
        self._market_tide = market_tide

        self.list = async_to_streamed_response_wrapper(
            market_tide.list,
        )
