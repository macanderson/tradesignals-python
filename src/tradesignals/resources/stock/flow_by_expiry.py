# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.stock.flow_by_expiry_list_response import FlowByExpiryListResponse

__all__ = ["FlowByExpiryResource", "AsyncFlowByExpiryResource"]


class FlowByExpiryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlowByExpiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return FlowByExpiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlowByExpiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return FlowByExpiryResourceWithStreamingResponse(self)

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
    ) -> Optional[FlowByExpiryListResponse]:
        """
        Returns the option flow per expiry for the last trading day.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/stock/{ticker}/flow-per-expiry",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[FlowByExpiryListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FlowByExpiryListResponse]], DataWrapper[FlowByExpiryListResponse]),
        )


class AsyncFlowByExpiryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlowByExpiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlowByExpiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlowByExpiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncFlowByExpiryResourceWithStreamingResponse(self)

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
    ) -> Optional[FlowByExpiryListResponse]:
        """
        Returns the option flow per expiry for the last trading day.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/stock/{ticker}/flow-per-expiry",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[FlowByExpiryListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FlowByExpiryListResponse]], DataWrapper[FlowByExpiryListResponse]),
        )


class FlowByExpiryResourceWithRawResponse:
    def __init__(self, flow_by_expiry: FlowByExpiryResource) -> None:
        self._flow_by_expiry = flow_by_expiry

        self.list = to_raw_response_wrapper(
            flow_by_expiry.list,
        )


class AsyncFlowByExpiryResourceWithRawResponse:
    def __init__(self, flow_by_expiry: AsyncFlowByExpiryResource) -> None:
        self._flow_by_expiry = flow_by_expiry

        self.list = async_to_raw_response_wrapper(
            flow_by_expiry.list,
        )


class FlowByExpiryResourceWithStreamingResponse:
    def __init__(self, flow_by_expiry: FlowByExpiryResource) -> None:
        self._flow_by_expiry = flow_by_expiry

        self.list = to_streamed_response_wrapper(
            flow_by_expiry.list,
        )


class AsyncFlowByExpiryResourceWithStreamingResponse:
    def __init__(self, flow_by_expiry: AsyncFlowByExpiryResource) -> None:
        self._flow_by_expiry = flow_by_expiry

        self.list = async_to_streamed_response_wrapper(
            flow_by_expiry.list,
        )
