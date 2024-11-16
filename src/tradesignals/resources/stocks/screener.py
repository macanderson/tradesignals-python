# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import make_request_options
from ...types.stocks import screener_retrieve_params

__all__ = ["ScreenerResource", "AsyncScreenerResource"]


class ScreenerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return ScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#with_streaming_response
        """
        return ScreenerResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        industry: str | NotGiven = NOT_GIVEN,
        market_cap_max: float | NotGiven = NOT_GIVEN,
        market_cap_min: float | NotGiven = NOT_GIVEN,
        price_max: float | NotGiven = NOT_GIVEN,
        price_min: float | NotGiven = NOT_GIVEN,
        sector: str | NotGiven = NOT_GIVEN,
        volume_max: float | NotGiven = NOT_GIVEN,
        volume_min: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Retrieve stocks that meet specified screening criteria.

        Filter by optional
        market capitalization, price, trading volume, sector, and industry.

        Args:
          industry: Industry to filter stocks.

          market_cap_max: Maximum market capitalization.

          market_cap_min: Minimum market capitalization.

          price_max: Maximum stock price.

          price_min: Minimum stock price.

          sector: Sector to filter stocks.

          volume_max: Maximum trading volume.

          volume_min: Minimum trading volume.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/stocks/screener",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "industry": industry,
                        "market_cap_max": market_cap_max,
                        "market_cap_min": market_cap_min,
                        "price_max": price_max,
                        "price_min": price_min,
                        "sector": sector,
                        "volume_max": volume_max,
                        "volume_min": volume_min,
                    },
                    screener_retrieve_params.ScreenerRetrieveParams,
                ),
            ),
            cast_to=object,
        )


class AsyncScreenerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#with_streaming_response
        """
        return AsyncScreenerResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        industry: str | NotGiven = NOT_GIVEN,
        market_cap_max: float | NotGiven = NOT_GIVEN,
        market_cap_min: float | NotGiven = NOT_GIVEN,
        price_max: float | NotGiven = NOT_GIVEN,
        price_min: float | NotGiven = NOT_GIVEN,
        sector: str | NotGiven = NOT_GIVEN,
        volume_max: float | NotGiven = NOT_GIVEN,
        volume_min: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Retrieve stocks that meet specified screening criteria.

        Filter by optional
        market capitalization, price, trading volume, sector, and industry.

        Args:
          industry: Industry to filter stocks.

          market_cap_max: Maximum market capitalization.

          market_cap_min: Minimum market capitalization.

          price_max: Maximum stock price.

          price_min: Minimum stock price.

          sector: Sector to filter stocks.

          volume_max: Maximum trading volume.

          volume_min: Minimum trading volume.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/stocks/screener",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "industry": industry,
                        "market_cap_max": market_cap_max,
                        "market_cap_min": market_cap_min,
                        "price_max": price_max,
                        "price_min": price_min,
                        "sector": sector,
                        "volume_max": volume_max,
                        "volume_min": volume_min,
                    },
                    screener_retrieve_params.ScreenerRetrieveParams,
                ),
            ),
            cast_to=object,
        )


class ScreenerResourceWithRawResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

        self.retrieve = to_raw_response_wrapper(
            screener.retrieve,
        )


class AsyncScreenerResourceWithRawResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

        self.retrieve = async_to_raw_response_wrapper(
            screener.retrieve,
        )


class ScreenerResourceWithStreamingResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

        self.retrieve = to_streamed_response_wrapper(
            screener.retrieve,
        )


class AsyncScreenerResourceWithStreamingResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

        self.retrieve = async_to_streamed_response_wrapper(
            screener.retrieve,
        )
