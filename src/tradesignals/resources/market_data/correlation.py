# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...types.market_data import correlation_list_params
from ...types.market_data.correlation_list_response import CorrelationListResponse

__all__ = ["CorrelationResource", "AsyncCorrelationResource"]


class CorrelationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CorrelationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return CorrelationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CorrelationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return CorrelationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        tickers: str,
        interval: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CorrelationListResponse]:
        """Returns the correlations between a list of tickers.

        Date must be the current or
        a past date. If no date is given, returns data for the current/last market day.

        Args:
          tickers: A comma-separated list of tickers. To exclude certain tickers, prefix the first
              ticker with a `-`.

          interval:
              The timeframe of the data to return. Allowed formats:

              - YTD
              - 1D, 2D, etc.
              - 1W, 2W, etc.
              - 1M, 2M, etc.
              - 1Y, 2Y, etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/market/correlations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tickers": tickers,
                        "interval": interval,
                    },
                    correlation_list_params.CorrelationListParams,
                ),
                post_parser=DataWrapper[Optional[CorrelationListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CorrelationListResponse]], DataWrapper[CorrelationListResponse]),
        )


class AsyncCorrelationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCorrelationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCorrelationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCorrelationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncCorrelationResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        tickers: str,
        interval: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CorrelationListResponse]:
        """Returns the correlations between a list of tickers.

        Date must be the current or
        a past date. If no date is given, returns data for the current/last market day.

        Args:
          tickers: A comma-separated list of tickers. To exclude certain tickers, prefix the first
              ticker with a `-`.

          interval:
              The timeframe of the data to return. Allowed formats:

              - YTD
              - 1D, 2D, etc.
              - 1W, 2W, etc.
              - 1M, 2M, etc.
              - 1Y, 2Y, etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/market/correlations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tickers": tickers,
                        "interval": interval,
                    },
                    correlation_list_params.CorrelationListParams,
                ),
                post_parser=DataWrapper[Optional[CorrelationListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CorrelationListResponse]], DataWrapper[CorrelationListResponse]),
        )


class CorrelationResourceWithRawResponse:
    def __init__(self, correlation: CorrelationResource) -> None:
        self._correlation = correlation

        self.list = to_raw_response_wrapper(
            correlation.list,
        )


class AsyncCorrelationResourceWithRawResponse:
    def __init__(self, correlation: AsyncCorrelationResource) -> None:
        self._correlation = correlation

        self.list = async_to_raw_response_wrapper(
            correlation.list,
        )


class CorrelationResourceWithStreamingResponse:
    def __init__(self, correlation: CorrelationResource) -> None:
        self._correlation = correlation

        self.list = to_streamed_response_wrapper(
            correlation.list,
        )


class AsyncCorrelationResourceWithStreamingResponse:
    def __init__(self, correlation: AsyncCorrelationResource) -> None:
        self._correlation = correlation

        self.list = async_to_streamed_response_wrapper(
            correlation.list,
        )
