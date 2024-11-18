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
from ...types.stock.flow_per_expiry_list_response import FlowPerExpiryListResponse

__all__ = ["FlowPerExpiryResource", "AsyncFlowPerExpiryResource"]


class FlowPerExpiryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlowPerExpiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return FlowPerExpiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlowPerExpiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return FlowPerExpiryResourceWithStreamingResponse(self)

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
    ) -> Optional[FlowPerExpiryListResponse]:
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
                post_parser=DataWrapper[Optional[FlowPerExpiryListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FlowPerExpiryListResponse]], DataWrapper[FlowPerExpiryListResponse]),
        )


class AsyncFlowPerExpiryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlowPerExpiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlowPerExpiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlowPerExpiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncFlowPerExpiryResourceWithStreamingResponse(self)

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
    ) -> Optional[FlowPerExpiryListResponse]:
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
                post_parser=DataWrapper[Optional[FlowPerExpiryListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FlowPerExpiryListResponse]], DataWrapper[FlowPerExpiryListResponse]),
        )


class FlowPerExpiryResourceWithRawResponse:
    def __init__(self, flow_per_expiry: FlowPerExpiryResource) -> None:
        self._flow_per_expiry = flow_per_expiry

        self.list = to_raw_response_wrapper(
            flow_per_expiry.list,
        )


class AsyncFlowPerExpiryResourceWithRawResponse:
    def __init__(self, flow_per_expiry: AsyncFlowPerExpiryResource) -> None:
        self._flow_per_expiry = flow_per_expiry

        self.list = async_to_raw_response_wrapper(
            flow_per_expiry.list,
        )


class FlowPerExpiryResourceWithStreamingResponse:
    def __init__(self, flow_per_expiry: FlowPerExpiryResource) -> None:
        self._flow_per_expiry = flow_per_expiry

        self.list = to_streamed_response_wrapper(
            flow_per_expiry.list,
        )


class AsyncFlowPerExpiryResourceWithStreamingResponse:
    def __init__(self, flow_per_expiry: AsyncFlowPerExpiryResource) -> None:
        self._flow_per_expiry = flow_per_expiry

        self.list = async_to_streamed_response_wrapper(
            flow_per_expiry.list,
        )
