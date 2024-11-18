# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.stock import ticker_options_volume_list_params
from ..._base_client import make_request_options
from ...types.stock.ticker_options_volume_response import TickerOptionsVolumeResponse

__all__ = ["TickerOptionsVolumeResource", "AsyncTickerOptionsVolumeResource"]


class TickerOptionsVolumeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TickerOptionsVolumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return TickerOptionsVolumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TickerOptionsVolumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return TickerOptionsVolumeResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TickerOptionsVolumeResponse:
        """
        Returns the options volume & premium for all trade executions that happened on a
        given trading date for the given ticker. This can be used to build a ticker
        options overview, such as a table or a line chart.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/stock/{ticker}/options-volume",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit}, ticker_options_volume_list_params.TickerOptionsVolumeListParams
                ),
            ),
            cast_to=TickerOptionsVolumeResponse,
        )


class AsyncTickerOptionsVolumeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTickerOptionsVolumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTickerOptionsVolumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTickerOptionsVolumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncTickerOptionsVolumeResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TickerOptionsVolumeResponse:
        """
        Returns the options volume & premium for all trade executions that happened on a
        given trading date for the given ticker. This can be used to build a ticker
        options overview, such as a table or a line chart.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/stock/{ticker}/options-volume",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, ticker_options_volume_list_params.TickerOptionsVolumeListParams
                ),
            ),
            cast_to=TickerOptionsVolumeResponse,
        )


class TickerOptionsVolumeResourceWithRawResponse:
    def __init__(self, ticker_options_volume: TickerOptionsVolumeResource) -> None:
        self._ticker_options_volume = ticker_options_volume

        self.list = to_raw_response_wrapper(
            ticker_options_volume.list,
        )


class AsyncTickerOptionsVolumeResourceWithRawResponse:
    def __init__(self, ticker_options_volume: AsyncTickerOptionsVolumeResource) -> None:
        self._ticker_options_volume = ticker_options_volume

        self.list = async_to_raw_response_wrapper(
            ticker_options_volume.list,
        )


class TickerOptionsVolumeResourceWithStreamingResponse:
    def __init__(self, ticker_options_volume: TickerOptionsVolumeResource) -> None:
        self._ticker_options_volume = ticker_options_volume

        self.list = to_streamed_response_wrapper(
            ticker_options_volume.list,
        )


class AsyncTickerOptionsVolumeResourceWithStreamingResponse:
    def __init__(self, ticker_options_volume: AsyncTickerOptionsVolumeResource) -> None:
        self._ticker_options_volume = ticker_options_volume

        self.list = async_to_streamed_response_wrapper(
            ticker_options_volume.list,
        )
