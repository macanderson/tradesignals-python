# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.options.greek_flow import expiry_list_params
from ....types.options.greek_flow.expiry_list_response import ExpiryListResponse

__all__ = ["ExpiryResource", "AsyncExpiryResource"]


class ExpiryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExpiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return ExpiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExpiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return ExpiryResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExpiryListResponse:
        """
        Retrieve options Greek flow data aggregated by expiration date.

        Args:
          date: Date to filter the Greek flow data. ISO 8601 format.

          expiration: Option expiration date. ISO 8601 format.

          symbol: Stock symbol to filter the Greek flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/options/greekflow/expiry",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "expiration": expiration,
                        "symbol": symbol,
                    },
                    expiry_list_params.ExpiryListParams,
                ),
            ),
            cast_to=ExpiryListResponse,
        )


class AsyncExpiryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExpiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExpiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExpiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncExpiryResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExpiryListResponse:
        """
        Retrieve options Greek flow data aggregated by expiration date.

        Args:
          date: Date to filter the Greek flow data. ISO 8601 format.

          expiration: Option expiration date. ISO 8601 format.

          symbol: Stock symbol to filter the Greek flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/options/greekflow/expiry",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "expiration": expiration,
                        "symbol": symbol,
                    },
                    expiry_list_params.ExpiryListParams,
                ),
            ),
            cast_to=ExpiryListResponse,
        )


class ExpiryResourceWithRawResponse:
    def __init__(self, expiry: ExpiryResource) -> None:
        self._expiry = expiry

        self.list = to_raw_response_wrapper(
            expiry.list,
        )


class AsyncExpiryResourceWithRawResponse:
    def __init__(self, expiry: AsyncExpiryResource) -> None:
        self._expiry = expiry

        self.list = async_to_raw_response_wrapper(
            expiry.list,
        )


class ExpiryResourceWithStreamingResponse:
    def __init__(self, expiry: ExpiryResource) -> None:
        self._expiry = expiry

        self.list = to_streamed_response_wrapper(
            expiry.list,
        )


class AsyncExpiryResourceWithStreamingResponse:
    def __init__(self, expiry: AsyncExpiryResource) -> None:
        self._expiry = expiry

        self.list = async_to_streamed_response_wrapper(
            expiry.list,
        )
