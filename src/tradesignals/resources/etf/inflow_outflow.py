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
from ...types.etf.inflow_outflow_retrieve_response import InflowOutflowRetrieveResponse

__all__ = ["InflowOutflowResource", "AsyncInflowOutflowResource"]


class InflowOutflowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InflowOutflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return InflowOutflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InflowOutflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return InflowOutflowResourceWithStreamingResponse(self)

    def retrieve(
        self,
        ticker: str | NotGiven = NOT_GIVEN,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[InflowOutflowRetrieveResponse]:
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
                post_parser=DataWrapper[Optional[InflowOutflowRetrieveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InflowOutflowRetrieveResponse]], DataWrapper[InflowOutflowRetrieveResponse]),
        )


class AsyncInflowOutflowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInflowOutflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInflowOutflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInflowOutflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncInflowOutflowResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        ticker: str | NotGiven = NOT_GIVEN,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[InflowOutflowRetrieveResponse]:
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
                post_parser=DataWrapper[Optional[InflowOutflowRetrieveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InflowOutflowRetrieveResponse]], DataWrapper[InflowOutflowRetrieveResponse]),
        )


class InflowOutflowResourceWithRawResponse:
    def __init__(self, inflow_outflow: InflowOutflowResource) -> None:
        self._inflow_outflow = inflow_outflow

        self.retrieve = to_raw_response_wrapper(
            inflow_outflow.retrieve,
        )


class AsyncInflowOutflowResourceWithRawResponse:
    def __init__(self, inflow_outflow: AsyncInflowOutflowResource) -> None:
        self._inflow_outflow = inflow_outflow

        self.retrieve = async_to_raw_response_wrapper(
            inflow_outflow.retrieve,
        )


class InflowOutflowResourceWithStreamingResponse:
    def __init__(self, inflow_outflow: InflowOutflowResource) -> None:
        self._inflow_outflow = inflow_outflow

        self.retrieve = to_streamed_response_wrapper(
            inflow_outflow.retrieve,
        )


class AsyncInflowOutflowResourceWithStreamingResponse:
    def __init__(self, inflow_outflow: AsyncInflowOutflowResource) -> None:
        self._inflow_outflow = inflow_outflow

        self.retrieve = async_to_streamed_response_wrapper(
            inflow_outflow.retrieve,
        )
