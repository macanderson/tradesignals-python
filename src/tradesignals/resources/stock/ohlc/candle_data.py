# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.stock.ohlc import candle_data_list_params
from ....types.stock.ohlc.ohlc_response import OhlcResponse

__all__ = ["CandleDataResource", "AsyncCandleDataResource"]


class CandleDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CandleDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return CandleDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CandleDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return CandleDataResourceWithStreamingResponse(self)

    def list(
        self,
        candle_size: Literal["1m", "5m", "10m", "15m", "30m", "1h", "4h"],
        *,
        ticker: str,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeframe: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OhlcResponse:
        """
        Returns the Open High Low Close (OHLC) candle data for a given ticker.

        Args:
          timeframe:
              The timeframe of the data to return. Allowed formats:

              - YTD
              - 1D, 2D, etc.
              - 1W, 2W, etc.
              - 1M, 2M, etc.
              - 1Y, 2Y, etc. Default: `1Y`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        if not candle_size:
            raise ValueError(f"Expected a non-empty value for `candle_size` but received {candle_size!r}")
        return self._get(
            f"/api/stock/{ticker}/ohlc/{candle_size}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "end_date": end_date,
                        "limit": limit,
                        "timeframe": timeframe,
                    },
                    candle_data_list_params.CandleDataListParams,
                ),
            ),
            cast_to=OhlcResponse,
        )


class AsyncCandleDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCandleDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCandleDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCandleDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncCandleDataResourceWithStreamingResponse(self)

    async def list(
        self,
        candle_size: Literal["1m", "5m", "10m", "15m", "30m", "1h", "4h"],
        *,
        ticker: str,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeframe: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OhlcResponse:
        """
        Returns the Open High Low Close (OHLC) candle data for a given ticker.

        Args:
          timeframe:
              The timeframe of the data to return. Allowed formats:

              - YTD
              - 1D, 2D, etc.
              - 1W, 2W, etc.
              - 1M, 2M, etc.
              - 1Y, 2Y, etc. Default: `1Y`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        if not candle_size:
            raise ValueError(f"Expected a non-empty value for `candle_size` but received {candle_size!r}")
        return await self._get(
            f"/api/stock/{ticker}/ohlc/{candle_size}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "end_date": end_date,
                        "limit": limit,
                        "timeframe": timeframe,
                    },
                    candle_data_list_params.CandleDataListParams,
                ),
            ),
            cast_to=OhlcResponse,
        )


class CandleDataResourceWithRawResponse:
    def __init__(self, candle_data: CandleDataResource) -> None:
        self._candle_data = candle_data

        self.list = to_raw_response_wrapper(
            candle_data.list,
        )


class AsyncCandleDataResourceWithRawResponse:
    def __init__(self, candle_data: AsyncCandleDataResource) -> None:
        self._candle_data = candle_data

        self.list = async_to_raw_response_wrapper(
            candle_data.list,
        )


class CandleDataResourceWithStreamingResponse:
    def __init__(self, candle_data: CandleDataResource) -> None:
        self._candle_data = candle_data

        self.list = to_streamed_response_wrapper(
            candle_data.list,
        )


class AsyncCandleDataResourceWithStreamingResponse:
    def __init__(self, candle_data: AsyncCandleDataResource) -> None:
        self._candle_data = candle_data

        self.list = async_to_streamed_response_wrapper(
            candle_data.list,
        )
