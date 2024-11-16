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
from ...types.market import spike_detection_retrieve_params
from ...types.market.spike_detection_retrieve_response import SpikeDetectionRetrieveResponse

__all__ = ["SpikeDetectionResource", "AsyncSpikeDetectionResource"]


class SpikeDetectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpikeDetectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return SpikeDetectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpikeDetectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return SpikeDetectionResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpikeDetectionRetrieveResponse:
        """Retrieve data on detected spikes in trading activity.

        Filter by optional symbol
        and date.

        Args:
          date: Date to filter spike data.

          symbol: Stock symbol to filter spike data.

          threshold: Threshold for spike detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/spike/detection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "symbol": symbol,
                        "threshold": threshold,
                    },
                    spike_detection_retrieve_params.SpikeDetectionRetrieveParams,
                ),
            ),
            cast_to=SpikeDetectionRetrieveResponse,
        )


class AsyncSpikeDetectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpikeDetectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpikeDetectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpikeDetectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncSpikeDetectionResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpikeDetectionRetrieveResponse:
        """Retrieve data on detected spikes in trading activity.

        Filter by optional symbol
        and date.

        Args:
          date: Date to filter spike data.

          symbol: Stock symbol to filter spike data.

          threshold: Threshold for spike detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/spike/detection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "symbol": symbol,
                        "threshold": threshold,
                    },
                    spike_detection_retrieve_params.SpikeDetectionRetrieveParams,
                ),
            ),
            cast_to=SpikeDetectionRetrieveResponse,
        )


class SpikeDetectionResourceWithRawResponse:
    def __init__(self, spike_detection: SpikeDetectionResource) -> None:
        self._spike_detection = spike_detection

        self.retrieve = to_raw_response_wrapper(
            spike_detection.retrieve,
        )


class AsyncSpikeDetectionResourceWithRawResponse:
    def __init__(self, spike_detection: AsyncSpikeDetectionResource) -> None:
        self._spike_detection = spike_detection

        self.retrieve = async_to_raw_response_wrapper(
            spike_detection.retrieve,
        )


class SpikeDetectionResourceWithStreamingResponse:
    def __init__(self, spike_detection: SpikeDetectionResource) -> None:
        self._spike_detection = spike_detection

        self.retrieve = to_streamed_response_wrapper(
            spike_detection.retrieve,
        )


class AsyncSpikeDetectionResourceWithStreamingResponse:
    def __init__(self, spike_detection: AsyncSpikeDetectionResource) -> None:
        self._spike_detection = spike_detection

        self.retrieve = async_to_streamed_response_wrapper(
            spike_detection.retrieve,
        )
