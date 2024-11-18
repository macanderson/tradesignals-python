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
from ...types.market_data import market_option_volume_list_params
from ...types.market_data.market_option_volume_list_response import MarketOptionVolumeListResponse

__all__ = ["MarketOptionVolumeResource", "AsyncMarketOptionVolumeResource"]


class MarketOptionVolumeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketOptionVolumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return MarketOptionVolumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketOptionVolumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return MarketOptionVolumeResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MarketOptionVolumeListResponse]:
        """
        Returns the total options volume and premium for a given trading date.

        Args:
          limit: How many items to return. Default is 1. Max is 500. Min is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/market/total-options-volume",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, market_option_volume_list_params.MarketOptionVolumeListParams),
                post_parser=DataWrapper[Optional[MarketOptionVolumeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MarketOptionVolumeListResponse]], DataWrapper[MarketOptionVolumeListResponse]),
        )


class AsyncMarketOptionVolumeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketOptionVolumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketOptionVolumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketOptionVolumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncMarketOptionVolumeResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MarketOptionVolumeListResponse]:
        """
        Returns the total options volume and premium for a given trading date.

        Args:
          limit: How many items to return. Default is 1. Max is 500. Min is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/market/total-options-volume",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, market_option_volume_list_params.MarketOptionVolumeListParams
                ),
                post_parser=DataWrapper[Optional[MarketOptionVolumeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MarketOptionVolumeListResponse]], DataWrapper[MarketOptionVolumeListResponse]),
        )


class MarketOptionVolumeResourceWithRawResponse:
    def __init__(self, market_option_volume: MarketOptionVolumeResource) -> None:
        self._market_option_volume = market_option_volume

        self.list = to_raw_response_wrapper(
            market_option_volume.list,
        )


class AsyncMarketOptionVolumeResourceWithRawResponse:
    def __init__(self, market_option_volume: AsyncMarketOptionVolumeResource) -> None:
        self._market_option_volume = market_option_volume

        self.list = async_to_raw_response_wrapper(
            market_option_volume.list,
        )


class MarketOptionVolumeResourceWithStreamingResponse:
    def __init__(self, market_option_volume: MarketOptionVolumeResource) -> None:
        self._market_option_volume = market_option_volume

        self.list = to_streamed_response_wrapper(
            market_option_volume.list,
        )


class AsyncMarketOptionVolumeResourceWithStreamingResponse:
    def __init__(self, market_option_volume: AsyncMarketOptionVolumeResource) -> None:
        self._market_option_volume = market_option_volume

        self.list = async_to_streamed_response_wrapper(
            market_option_volume.list,
        )
