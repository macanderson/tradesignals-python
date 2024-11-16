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
from ..._base_client import make_request_options
from ...types.stocks import dividend_retrieve_params
from ...types.stocks.dividend_retrieve_response import DividendRetrieveResponse

__all__ = ["DividendsResource", "AsyncDividendsResource"]


class DividendsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DividendsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return DividendsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DividendsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return DividendsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DividendRetrieveResponse:
        """Retrieve dividend history for a specific stock symbol.

        Filter by optional start
        date.

        Args:
          end_date: End date for the dividend data.

          start_date: Start date for the dividend data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/api/stocks/dividends/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    dividend_retrieve_params.DividendRetrieveParams,
                ),
            ),
            cast_to=DividendRetrieveResponse,
        )


class AsyncDividendsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDividendsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDividendsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDividendsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncDividendsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DividendRetrieveResponse:
        """Retrieve dividend history for a specific stock symbol.

        Filter by optional start
        date.

        Args:
          end_date: End date for the dividend data.

          start_date: Start date for the dividend data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/api/stocks/dividends/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    dividend_retrieve_params.DividendRetrieveParams,
                ),
            ),
            cast_to=DividendRetrieveResponse,
        )


class DividendsResourceWithRawResponse:
    def __init__(self, dividends: DividendsResource) -> None:
        self._dividends = dividends

        self.retrieve = to_raw_response_wrapper(
            dividends.retrieve,
        )


class AsyncDividendsResourceWithRawResponse:
    def __init__(self, dividends: AsyncDividendsResource) -> None:
        self._dividends = dividends

        self.retrieve = async_to_raw_response_wrapper(
            dividends.retrieve,
        )


class DividendsResourceWithStreamingResponse:
    def __init__(self, dividends: DividendsResource) -> None:
        self._dividends = dividends

        self.retrieve = to_streamed_response_wrapper(
            dividends.retrieve,
        )


class AsyncDividendsResourceWithStreamingResponse:
    def __init__(self, dividends: AsyncDividendsResource) -> None:
        self._dividends = dividends

        self.retrieve = async_to_streamed_response_wrapper(
            dividends.retrieve,
        )
