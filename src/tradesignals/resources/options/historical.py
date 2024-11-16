# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ..._base_client import make_request_options
from ...types.options import historical_retrieve_params
from ...types.options.historical_retrieve_response import HistoricalRetrieveResponse

__all__ = ["HistoricalResource", "AsyncHistoricalResource"]


class HistoricalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoricalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return HistoricalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoricalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return HistoricalResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        option_type: Literal["CALL", "PUT"] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        strike: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoricalRetrieveResponse:
        """Retrieve historical options data for a specific stock symbol.

        Filter by optional
        start date, end date, expiration date, strike price, and option type.

        Args:
          end_date: End date for the historical data.

          expiration: Option expiration date to filter the data.

          option_type: Option type (CALL or PUT).

          start_date: Start date for the historical data.

          strike: Option strike price to filter the data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/api/options/historical/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "expiration": expiration,
                        "option_type": option_type,
                        "start_date": start_date,
                        "strike": strike,
                    },
                    historical_retrieve_params.HistoricalRetrieveParams,
                ),
            ),
            cast_to=HistoricalRetrieveResponse,
        )


class AsyncHistoricalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoricalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHistoricalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoricalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncHistoricalResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        option_type: Literal["CALL", "PUT"] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        strike: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HistoricalRetrieveResponse:
        """Retrieve historical options data for a specific stock symbol.

        Filter by optional
        start date, end date, expiration date, strike price, and option type.

        Args:
          end_date: End date for the historical data.

          expiration: Option expiration date to filter the data.

          option_type: Option type (CALL or PUT).

          start_date: Start date for the historical data.

          strike: Option strike price to filter the data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/api/options/historical/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "expiration": expiration,
                        "option_type": option_type,
                        "start_date": start_date,
                        "strike": strike,
                    },
                    historical_retrieve_params.HistoricalRetrieveParams,
                ),
            ),
            cast_to=HistoricalRetrieveResponse,
        )


class HistoricalResourceWithRawResponse:
    def __init__(self, historical: HistoricalResource) -> None:
        self._historical = historical

        self.retrieve = to_raw_response_wrapper(
            historical.retrieve,
        )


class AsyncHistoricalResourceWithRawResponse:
    def __init__(self, historical: AsyncHistoricalResource) -> None:
        self._historical = historical

        self.retrieve = async_to_raw_response_wrapper(
            historical.retrieve,
        )


class HistoricalResourceWithStreamingResponse:
    def __init__(self, historical: HistoricalResource) -> None:
        self._historical = historical

        self.retrieve = to_streamed_response_wrapper(
            historical.retrieve,
        )


class AsyncHistoricalResourceWithStreamingResponse:
    def __init__(self, historical: AsyncHistoricalResource) -> None:
        self._historical = historical

        self.retrieve = async_to_streamed_response_wrapper(
            historical.retrieve,
        )
