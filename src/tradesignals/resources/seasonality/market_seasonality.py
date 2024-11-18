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
from ...types.seasonality.market_seasonality_list_response import MarketSeasonalityListResponse

__all__ = ["MarketSeasonalityResource", "AsyncMarketSeasonalityResource"]


class MarketSeasonalityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketSeasonalityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return MarketSeasonalityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketSeasonalityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return MarketSeasonalityResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MarketSeasonalityListResponse]:
        """
        Returns the average return by month for the tickers SPY, QQQ, IWM, XLE, XLC,
        XLK, XLV, XLP, XLY, XLRE, XLF, XLI, XLB.
        """
        return self._get(
            "/api/seasonality/market",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[MarketSeasonalityListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MarketSeasonalityListResponse]], DataWrapper[MarketSeasonalityListResponse]),
        )


class AsyncMarketSeasonalityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketSeasonalityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketSeasonalityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketSeasonalityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncMarketSeasonalityResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MarketSeasonalityListResponse]:
        """
        Returns the average return by month for the tickers SPY, QQQ, IWM, XLE, XLC,
        XLK, XLV, XLP, XLY, XLRE, XLF, XLI, XLB.
        """
        return await self._get(
            "/api/seasonality/market",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[MarketSeasonalityListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MarketSeasonalityListResponse]], DataWrapper[MarketSeasonalityListResponse]),
        )


class MarketSeasonalityResourceWithRawResponse:
    def __init__(self, market_seasonality: MarketSeasonalityResource) -> None:
        self._market_seasonality = market_seasonality

        self.list = to_raw_response_wrapper(
            market_seasonality.list,
        )


class AsyncMarketSeasonalityResourceWithRawResponse:
    def __init__(self, market_seasonality: AsyncMarketSeasonalityResource) -> None:
        self._market_seasonality = market_seasonality

        self.list = async_to_raw_response_wrapper(
            market_seasonality.list,
        )


class MarketSeasonalityResourceWithStreamingResponse:
    def __init__(self, market_seasonality: MarketSeasonalityResource) -> None:
        self._market_seasonality = market_seasonality

        self.list = to_streamed_response_wrapper(
            market_seasonality.list,
        )


class AsyncMarketSeasonalityResourceWithStreamingResponse:
    def __init__(self, market_seasonality: AsyncMarketSeasonalityResource) -> None:
        self._market_seasonality = market_seasonality

        self.list = async_to_streamed_response_wrapper(
            market_seasonality.list,
        )
