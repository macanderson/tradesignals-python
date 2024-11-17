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
from ...types.market import correlation_list_params
from ...types.market.correlation_list_response import CorrelationListResponse

__all__ = ["CorrelationsResource", "AsyncCorrelationsResource"]


class CorrelationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CorrelationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return CorrelationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CorrelationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return CorrelationsResourceWithStreamingResponse(self)

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


class AsyncCorrelationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCorrelationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCorrelationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCorrelationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncCorrelationsResourceWithStreamingResponse(self)

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


class CorrelationsResourceWithRawResponse:
    def __init__(self, correlations: CorrelationsResource) -> None:
        self._correlations = correlations

        self.list = to_raw_response_wrapper(
            correlations.list,
        )


class AsyncCorrelationsResourceWithRawResponse:
    def __init__(self, correlations: AsyncCorrelationsResource) -> None:
        self._correlations = correlations

        self.list = async_to_raw_response_wrapper(
            correlations.list,
        )


class CorrelationsResourceWithStreamingResponse:
    def __init__(self, correlations: CorrelationsResource) -> None:
        self._correlations = correlations

        self.list = to_streamed_response_wrapper(
            correlations.list,
        )


class AsyncCorrelationsResourceWithStreamingResponse:
    def __init__(self, correlations: AsyncCorrelationsResource) -> None:
        self._correlations = correlations

        self.list = async_to_streamed_response_wrapper(
            correlations.list,
        )
