# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import make_request_options
from ...types.etf.weights import Weights

__all__ = ["WeightsResource", "AsyncWeightsResource"]


class WeightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WeightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return WeightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WeightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return WeightsResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Weights:
        """
        Returns the sector and country weights for the given ETF ticker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/etfs/{ticker}/weights",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Weights,
        )


class AsyncWeightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWeightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWeightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWeightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncWeightsResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Weights:
        """
        Returns the sector and country weights for the given ETF ticker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/etfs/{ticker}/weights",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Weights,
        )


class WeightsResourceWithRawResponse:
    def __init__(self, weights: WeightsResource) -> None:
        self._weights = weights

        self.list = to_raw_response_wrapper(
            weights.list,
        )


class AsyncWeightsResourceWithRawResponse:
    def __init__(self, weights: AsyncWeightsResource) -> None:
        self._weights = weights

        self.list = async_to_raw_response_wrapper(
            weights.list,
        )


class WeightsResourceWithStreamingResponse:
    def __init__(self, weights: WeightsResource) -> None:
        self._weights = weights

        self.list = to_streamed_response_wrapper(
            weights.list,
        )


class AsyncWeightsResourceWithStreamingResponse:
    def __init__(self, weights: AsyncWeightsResource) -> None:
        self._weights = weights

        self.list = async_to_streamed_response_wrapper(
            weights.list,
        )
