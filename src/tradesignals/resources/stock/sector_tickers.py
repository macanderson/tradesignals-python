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
from ...types.stock.sector_ticker_list_response import SectorTickerListResponse

__all__ = ["SectorTickersResource", "AsyncSectorTickersResource"]


class SectorTickersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SectorTickersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return SectorTickersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SectorTickersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return SectorTickersResourceWithStreamingResponse(self)

    def list(
        self,
        sector: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SectorTickerListResponse]:
        """
        Returns a list of tickers which are in the given sector.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sector:
            raise ValueError(f"Expected a non-empty value for `sector` but received {sector!r}")
        return self._get(
            f"/api/stock/{sector}/tickers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[SectorTickerListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SectorTickerListResponse]], DataWrapper[SectorTickerListResponse]),
        )


class AsyncSectorTickersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSectorTickersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSectorTickersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSectorTickersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncSectorTickersResourceWithStreamingResponse(self)

    async def list(
        self,
        sector: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SectorTickerListResponse]:
        """
        Returns a list of tickers which are in the given sector.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not sector:
            raise ValueError(f"Expected a non-empty value for `sector` but received {sector!r}")
        return await self._get(
            f"/api/stock/{sector}/tickers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[SectorTickerListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SectorTickerListResponse]], DataWrapper[SectorTickerListResponse]),
        )


class SectorTickersResourceWithRawResponse:
    def __init__(self, sector_tickers: SectorTickersResource) -> None:
        self._sector_tickers = sector_tickers

        self.list = to_raw_response_wrapper(
            sector_tickers.list,
        )


class AsyncSectorTickersResourceWithRawResponse:
    def __init__(self, sector_tickers: AsyncSectorTickersResource) -> None:
        self._sector_tickers = sector_tickers

        self.list = async_to_raw_response_wrapper(
            sector_tickers.list,
        )


class SectorTickersResourceWithStreamingResponse:
    def __init__(self, sector_tickers: SectorTickersResource) -> None:
        self._sector_tickers = sector_tickers

        self.list = to_streamed_response_wrapper(
            sector_tickers.list,
        )


class AsyncSectorTickersResourceWithStreamingResponse:
    def __init__(self, sector_tickers: AsyncSectorTickersResource) -> None:
        self._sector_tickers = sector_tickers

        self.list = async_to_streamed_response_wrapper(
            sector_tickers.list,
        )
