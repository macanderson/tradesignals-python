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
from ...types.etfs.weights import Weights

__all__ = ["SectorCountryWeightsResource", "AsyncSectorCountryWeightsResource"]


class SectorCountryWeightsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SectorCountryWeightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return SectorCountryWeightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SectorCountryWeightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return SectorCountryWeightsResourceWithStreamingResponse(self)

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


class AsyncSectorCountryWeightsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSectorCountryWeightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSectorCountryWeightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSectorCountryWeightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncSectorCountryWeightsResourceWithStreamingResponse(self)

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


class SectorCountryWeightsResourceWithRawResponse:
    def __init__(self, sector_country_weights: SectorCountryWeightsResource) -> None:
        self._sector_country_weights = sector_country_weights

        self.list = to_raw_response_wrapper(
            sector_country_weights.list,
        )


class AsyncSectorCountryWeightsResourceWithRawResponse:
    def __init__(self, sector_country_weights: AsyncSectorCountryWeightsResource) -> None:
        self._sector_country_weights = sector_country_weights

        self.list = async_to_raw_response_wrapper(
            sector_country_weights.list,
        )


class SectorCountryWeightsResourceWithStreamingResponse:
    def __init__(self, sector_country_weights: SectorCountryWeightsResource) -> None:
        self._sector_country_weights = sector_country_weights

        self.list = to_streamed_response_wrapper(
            sector_country_weights.list,
        )


class AsyncSectorCountryWeightsResourceWithStreamingResponse:
    def __init__(self, sector_country_weights: AsyncSectorCountryWeightsResource) -> None:
        self._sector_country_weights = sector_country_weights

        self.list = async_to_streamed_response_wrapper(
            sector_country_weights.list,
        )
