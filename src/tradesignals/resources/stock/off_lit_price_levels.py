# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ...types.stock import off_lit_price_level_list_params
from ..._base_client import make_request_options
from ...types.stock.off_lit_price_levels_response import OffLitPriceLevelsResponse

__all__ = ["OffLitPriceLevelsResource", "AsyncOffLitPriceLevelsResource"]


class OffLitPriceLevelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OffLitPriceLevelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OffLitPriceLevelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OffLitPriceLevelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OffLitPriceLevelsResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OffLitPriceLevelsResponse:
        """
        Returns the lit & off-lit stock volume per price level for the given ticker.
        Important: The volume does **NOT** represent the full market daily volume. It
        only represents the volume of executed trades on exchanges operated by Nasdaq
        and FINRA off-lit exchanges.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/stock/{ticker}/stock-volume-price-levels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, off_lit_price_level_list_params.OffLitPriceLevelListParams),
            ),
            cast_to=OffLitPriceLevelsResponse,
        )


class AsyncOffLitPriceLevelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOffLitPriceLevelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOffLitPriceLevelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOffLitPriceLevelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOffLitPriceLevelsResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OffLitPriceLevelsResponse:
        """
        Returns the lit & off-lit stock volume per price level for the given ticker.
        Important: The volume does **NOT** represent the full market daily volume. It
        only represents the volume of executed trades on exchanges operated by Nasdaq
        and FINRA off-lit exchanges.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/stock/{ticker}/stock-volume-price-levels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"date": date}, off_lit_price_level_list_params.OffLitPriceLevelListParams
                ),
            ),
            cast_to=OffLitPriceLevelsResponse,
        )


class OffLitPriceLevelsResourceWithRawResponse:
    def __init__(self, off_lit_price_levels: OffLitPriceLevelsResource) -> None:
        self._off_lit_price_levels = off_lit_price_levels

        self.list = to_raw_response_wrapper(
            off_lit_price_levels.list,
        )


class AsyncOffLitPriceLevelsResourceWithRawResponse:
    def __init__(self, off_lit_price_levels: AsyncOffLitPriceLevelsResource) -> None:
        self._off_lit_price_levels = off_lit_price_levels

        self.list = async_to_raw_response_wrapper(
            off_lit_price_levels.list,
        )


class OffLitPriceLevelsResourceWithStreamingResponse:
    def __init__(self, off_lit_price_levels: OffLitPriceLevelsResource) -> None:
        self._off_lit_price_levels = off_lit_price_levels

        self.list = to_streamed_response_wrapper(
            off_lit_price_levels.list,
        )


class AsyncOffLitPriceLevelsResourceWithStreamingResponse:
    def __init__(self, off_lit_price_levels: AsyncOffLitPriceLevelsResource) -> None:
        self._off_lit_price_levels = off_lit_price_levels

        self.list = async_to_streamed_response_wrapper(
            off_lit_price_levels.list,
        )
