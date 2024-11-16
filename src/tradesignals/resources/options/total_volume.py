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
from ...types.options import total_volume_list_params
from ...types.options.total_volume_list_response import TotalVolumeListResponse

__all__ = ["TotalVolumeResource", "AsyncTotalVolumeResource"]


class TotalVolumeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TotalVolumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return TotalVolumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TotalVolumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return TotalVolumeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TotalVolumeListResponse:
        """
        Retrieve total options volume for all symbols or a specific symbol.

        Args:
          date: Date to filter total options volume.

          symbol: Stock symbol to filter total options volume.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/options/total_volume",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "symbol": symbol,
                    },
                    total_volume_list_params.TotalVolumeListParams,
                ),
            ),
            cast_to=TotalVolumeListResponse,
        )


class AsyncTotalVolumeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTotalVolumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTotalVolumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTotalVolumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncTotalVolumeResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TotalVolumeListResponse:
        """
        Retrieve total options volume for all symbols or a specific symbol.

        Args:
          date: Date to filter total options volume.

          symbol: Stock symbol to filter total options volume.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/options/total_volume",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "symbol": symbol,
                    },
                    total_volume_list_params.TotalVolumeListParams,
                ),
            ),
            cast_to=TotalVolumeListResponse,
        )


class TotalVolumeResourceWithRawResponse:
    def __init__(self, total_volume: TotalVolumeResource) -> None:
        self._total_volume = total_volume

        self.list = to_raw_response_wrapper(
            total_volume.list,
        )


class AsyncTotalVolumeResourceWithRawResponse:
    def __init__(self, total_volume: AsyncTotalVolumeResource) -> None:
        self._total_volume = total_volume

        self.list = async_to_raw_response_wrapper(
            total_volume.list,
        )


class TotalVolumeResourceWithStreamingResponse:
    def __init__(self, total_volume: TotalVolumeResource) -> None:
        self._total_volume = total_volume

        self.list = to_streamed_response_wrapper(
            total_volume.list,
        )


class AsyncTotalVolumeResourceWithStreamingResponse:
    def __init__(self, total_volume: AsyncTotalVolumeResource) -> None:
        self._total_volume = total_volume

        self.list = async_to_streamed_response_wrapper(
            total_volume.list,
        )
