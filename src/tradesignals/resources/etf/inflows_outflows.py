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
from ...types.etf.inflows_outflow_list_response import InflowsOutflowListResponse

__all__ = ["InflowsOutflowsResource", "AsyncInflowsOutflowsResource"]


class InflowsOutflowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InflowsOutflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return InflowsOutflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InflowsOutflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return InflowsOutflowsResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str | NotGiven = NOT_GIVEN,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[InflowsOutflowListResponse]:
        """
        Returns an ETF's inflow and outflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/etfs/{ticker}/in-outflow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[InflowsOutflowListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InflowsOutflowListResponse]], DataWrapper[InflowsOutflowListResponse]),
        )


class AsyncInflowsOutflowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInflowsOutflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInflowsOutflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInflowsOutflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncInflowsOutflowsResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str | NotGiven = NOT_GIVEN,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[InflowsOutflowListResponse]:
        """
        Returns an ETF's inflow and outflow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/etfs/{ticker}/in-outflow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[InflowsOutflowListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InflowsOutflowListResponse]], DataWrapper[InflowsOutflowListResponse]),
        )


class InflowsOutflowsResourceWithRawResponse:
    def __init__(self, inflows_outflows: InflowsOutflowsResource) -> None:
        self._inflows_outflows = inflows_outflows

        self.list = to_raw_response_wrapper(
            inflows_outflows.list,
        )


class AsyncInflowsOutflowsResourceWithRawResponse:
    def __init__(self, inflows_outflows: AsyncInflowsOutflowsResource) -> None:
        self._inflows_outflows = inflows_outflows

        self.list = async_to_raw_response_wrapper(
            inflows_outflows.list,
        )


class InflowsOutflowsResourceWithStreamingResponse:
    def __init__(self, inflows_outflows: InflowsOutflowsResource) -> None:
        self._inflows_outflows = inflows_outflows

        self.list = to_streamed_response_wrapper(
            inflows_outflows.list,
        )


class AsyncInflowsOutflowsResourceWithStreamingResponse:
    def __init__(self, inflows_outflows: AsyncInflowsOutflowsResource) -> None:
        self._inflows_outflows = inflows_outflows

        self.list = async_to_streamed_response_wrapper(
            inflows_outflows.list,
        )
