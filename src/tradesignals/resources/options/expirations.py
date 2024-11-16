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
from ...types.options.expiration_retrieve_response import ExpirationRetrieveResponse

__all__ = ["ExpirationsResource", "AsyncExpirationsResource"]


class ExpirationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExpirationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return ExpirationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExpirationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return ExpirationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExpirationRetrieveResponse:
        """
        Retrieve available option expiration dates for a specific stock symbol.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/api/options/expirations/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpirationRetrieveResponse,
        )


class AsyncExpirationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExpirationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExpirationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExpirationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncExpirationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExpirationRetrieveResponse:
        """
        Retrieve available option expiration dates for a specific stock symbol.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/api/options/expirations/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExpirationRetrieveResponse,
        )


class ExpirationsResourceWithRawResponse:
    def __init__(self, expirations: ExpirationsResource) -> None:
        self._expirations = expirations

        self.retrieve = to_raw_response_wrapper(
            expirations.retrieve,
        )


class AsyncExpirationsResourceWithRawResponse:
    def __init__(self, expirations: AsyncExpirationsResource) -> None:
        self._expirations = expirations

        self.retrieve = async_to_raw_response_wrapper(
            expirations.retrieve,
        )


class ExpirationsResourceWithStreamingResponse:
    def __init__(self, expirations: ExpirationsResource) -> None:
        self._expirations = expirations

        self.retrieve = to_streamed_response_wrapper(
            expirations.retrieve,
        )


class AsyncExpirationsResourceWithStreamingResponse:
    def __init__(self, expirations: AsyncExpirationsResource) -> None:
        self._expirations = expirations

        self.retrieve = async_to_streamed_response_wrapper(
            expirations.retrieve,
        )
