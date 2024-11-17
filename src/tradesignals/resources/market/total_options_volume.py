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
from ...types.market import total_options_volume_list_params
from ...types.market.total_options_volume_list_response import TotalOptionsVolumeListResponse

__all__ = ["TotalOptionsVolumeResource", "AsyncTotalOptionsVolumeResource"]


class TotalOptionsVolumeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TotalOptionsVolumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return TotalOptionsVolumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TotalOptionsVolumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return TotalOptionsVolumeResourceWithStreamingResponse(self)

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
    ) -> Optional[TotalOptionsVolumeListResponse]:
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
                query=maybe_transform({"limit": limit}, total_options_volume_list_params.TotalOptionsVolumeListParams),
                post_parser=DataWrapper[Optional[TotalOptionsVolumeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TotalOptionsVolumeListResponse]], DataWrapper[TotalOptionsVolumeListResponse]),
        )


class AsyncTotalOptionsVolumeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTotalOptionsVolumeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTotalOptionsVolumeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTotalOptionsVolumeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncTotalOptionsVolumeResourceWithStreamingResponse(self)

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
    ) -> Optional[TotalOptionsVolumeListResponse]:
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
                    {"limit": limit}, total_options_volume_list_params.TotalOptionsVolumeListParams
                ),
                post_parser=DataWrapper[Optional[TotalOptionsVolumeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TotalOptionsVolumeListResponse]], DataWrapper[TotalOptionsVolumeListResponse]),
        )


class TotalOptionsVolumeResourceWithRawResponse:
    def __init__(self, total_options_volume: TotalOptionsVolumeResource) -> None:
        self._total_options_volume = total_options_volume

        self.list = to_raw_response_wrapper(
            total_options_volume.list,
        )


class AsyncTotalOptionsVolumeResourceWithRawResponse:
    def __init__(self, total_options_volume: AsyncTotalOptionsVolumeResource) -> None:
        self._total_options_volume = total_options_volume

        self.list = async_to_raw_response_wrapper(
            total_options_volume.list,
        )


class TotalOptionsVolumeResourceWithStreamingResponse:
    def __init__(self, total_options_volume: TotalOptionsVolumeResource) -> None:
        self._total_options_volume = total_options_volume

        self.list = to_streamed_response_wrapper(
            total_options_volume.list,
        )


class AsyncTotalOptionsVolumeResourceWithStreamingResponse:
    def __init__(self, total_options_volume: AsyncTotalOptionsVolumeResource) -> None:
        self._total_options_volume = total_options_volume

        self.list = async_to_streamed_response_wrapper(
            total_options_volume.list,
        )
