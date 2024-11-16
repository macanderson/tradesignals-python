# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import make_request_options
from ...types.market.overview_retrieve_response import OverviewRetrieveResponse

__all__ = ["OverviewResource", "AsyncOverviewResource"]


class OverviewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OverviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OverviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OverviewResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OverviewRetrieveResponse:
        """Retrieve an overview of the current market status."""
        return self._get(
            "/api/market/overview",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverviewRetrieveResponse,
        )


class AsyncOverviewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOverviewResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOverviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverviewResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOverviewResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OverviewRetrieveResponse:
        """Retrieve an overview of the current market status."""
        return await self._get(
            "/api/market/overview",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OverviewRetrieveResponse,
        )


class OverviewResourceWithRawResponse:
    def __init__(self, overview: OverviewResource) -> None:
        self._overview = overview

        self.retrieve = to_raw_response_wrapper(
            overview.retrieve,
        )


class AsyncOverviewResourceWithRawResponse:
    def __init__(self, overview: AsyncOverviewResource) -> None:
        self._overview = overview

        self.retrieve = async_to_raw_response_wrapper(
            overview.retrieve,
        )


class OverviewResourceWithStreamingResponse:
    def __init__(self, overview: OverviewResource) -> None:
        self._overview = overview

        self.retrieve = to_streamed_response_wrapper(
            overview.retrieve,
        )


class AsyncOverviewResourceWithStreamingResponse:
    def __init__(self, overview: AsyncOverviewResource) -> None:
        self._overview = overview

        self.retrieve = async_to_streamed_response_wrapper(
            overview.retrieve,
        )
