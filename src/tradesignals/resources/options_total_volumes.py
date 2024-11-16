# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import options_total_volume_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.options_total_volume_list_response import OptionsTotalVolumeListResponse

__all__ = ["OptionsTotalVolumesResource", "AsyncOptionsTotalVolumesResource"]


class OptionsTotalVolumesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptionsTotalVolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionsTotalVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsTotalVolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#with_streaming_response
        """
        return OptionsTotalVolumesResourceWithStreamingResponse(self)

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
    ) -> OptionsTotalVolumeListResponse:
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
                    options_total_volume_list_params.OptionsTotalVolumeListParams,
                ),
            ),
            cast_to=OptionsTotalVolumeListResponse,
        )


class AsyncOptionsTotalVolumesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptionsTotalVolumesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsTotalVolumesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsTotalVolumesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#with_streaming_response
        """
        return AsyncOptionsTotalVolumesResourceWithStreamingResponse(self)

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
    ) -> OptionsTotalVolumeListResponse:
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
                    options_total_volume_list_params.OptionsTotalVolumeListParams,
                ),
            ),
            cast_to=OptionsTotalVolumeListResponse,
        )


class OptionsTotalVolumesResourceWithRawResponse:
    def __init__(self, options_total_volumes: OptionsTotalVolumesResource) -> None:
        self._options_total_volumes = options_total_volumes

        self.list = to_raw_response_wrapper(
            options_total_volumes.list,
        )


class AsyncOptionsTotalVolumesResourceWithRawResponse:
    def __init__(self, options_total_volumes: AsyncOptionsTotalVolumesResource) -> None:
        self._options_total_volumes = options_total_volumes

        self.list = async_to_raw_response_wrapper(
            options_total_volumes.list,
        )


class OptionsTotalVolumesResourceWithStreamingResponse:
    def __init__(self, options_total_volumes: OptionsTotalVolumesResource) -> None:
        self._options_total_volumes = options_total_volumes

        self.list = to_streamed_response_wrapper(
            options_total_volumes.list,
        )


class AsyncOptionsTotalVolumesResourceWithStreamingResponse:
    def __init__(self, options_total_volumes: AsyncOptionsTotalVolumesResource) -> None:
        self._options_total_volumes = options_total_volumes

        self.list = async_to_streamed_response_wrapper(
            options_total_volumes.list,
        )
