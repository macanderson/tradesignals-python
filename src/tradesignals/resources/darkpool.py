# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import darkpool_list_params, darkpool_retrieve_params
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
from ..types.darkpool_list_response import DarkpoolListResponse
from ..types.darkpool_retrieve_response import DarkpoolRetrieveResponse

__all__ = ["DarkpoolResource", "AsyncDarkpoolResource"]


class DarkpoolResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DarkpoolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return DarkpoolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DarkpoolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return DarkpoolResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        newer_than: str | NotGiven = NOT_GIVEN,
        older_than: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DarkpoolRetrieveResponse:
        """-> Returns the darkpool trades for the given ticker on a given day.

        Date must be
        the current or a past date. If no date is given, returns data for the
        current/last market day.

        Args:
          date: Date to filter darkpool transactions.

          limit: How many items to return. Default is 100. Max is 200. Minimum is 1.

          newer_than: -> The unix time in milliseconds or seconds at which no older results will be
              returned. Can be used with newer_than to paginate by time. Also accepts an ISO
              date example "2024-01-25".

          older_than: -> The unix time in milliseconds or seconds at which no newer results will be
              returned. Can be used with newer_than to paginate by time. Also accepts an ISO
              date example "2024-01-25".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/api/darkpool/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "newer_than": newer_than,
                        "older_than": older_than,
                    },
                    darkpool_retrieve_params.DarkpoolRetrieveParams,
                ),
            ),
            cast_to=DarkpoolRetrieveResponse,
        )

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DarkpoolListResponse:
        """
        Returns recent Darkpool trades for all securities listed on either NASDAQ or
        NYSE.

        Args:
          date: Date to filter darkpool transactions.

          limit: How many items to return. Default is 100. Max is 200. Minimum is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/darkpool/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                    },
                    darkpool_list_params.DarkpoolListParams,
                ),
            ),
            cast_to=DarkpoolListResponse,
        )


class AsyncDarkpoolResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDarkpoolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDarkpoolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDarkpoolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncDarkpoolResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        newer_than: str | NotGiven = NOT_GIVEN,
        older_than: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DarkpoolRetrieveResponse:
        """-> Returns the darkpool trades for the given ticker on a given day.

        Date must be
        the current or a past date. If no date is given, returns data for the
        current/last market day.

        Args:
          date: Date to filter darkpool transactions.

          limit: How many items to return. Default is 100. Max is 200. Minimum is 1.

          newer_than: -> The unix time in milliseconds or seconds at which no older results will be
              returned. Can be used with newer_than to paginate by time. Also accepts an ISO
              date example "2024-01-25".

          older_than: -> The unix time in milliseconds or seconds at which no newer results will be
              returned. Can be used with newer_than to paginate by time. Also accepts an ISO
              date example "2024-01-25".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/api/darkpool/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "newer_than": newer_than,
                        "older_than": older_than,
                    },
                    darkpool_retrieve_params.DarkpoolRetrieveParams,
                ),
            ),
            cast_to=DarkpoolRetrieveResponse,
        )

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DarkpoolListResponse:
        """
        Returns recent Darkpool trades for all securities listed on either NASDAQ or
        NYSE.

        Args:
          date: Date to filter darkpool transactions.

          limit: How many items to return. Default is 100. Max is 200. Minimum is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/darkpool/recent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                    },
                    darkpool_list_params.DarkpoolListParams,
                ),
            ),
            cast_to=DarkpoolListResponse,
        )


class DarkpoolResourceWithRawResponse:
    def __init__(self, darkpool: DarkpoolResource) -> None:
        self._darkpool = darkpool

        self.retrieve = to_raw_response_wrapper(
            darkpool.retrieve,
        )
        self.list = to_raw_response_wrapper(
            darkpool.list,
        )


class AsyncDarkpoolResourceWithRawResponse:
    def __init__(self, darkpool: AsyncDarkpoolResource) -> None:
        self._darkpool = darkpool

        self.retrieve = async_to_raw_response_wrapper(
            darkpool.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            darkpool.list,
        )


class DarkpoolResourceWithStreamingResponse:
    def __init__(self, darkpool: DarkpoolResource) -> None:
        self._darkpool = darkpool

        self.retrieve = to_streamed_response_wrapper(
            darkpool.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            darkpool.list,
        )


class AsyncDarkpoolResourceWithStreamingResponse:
    def __init__(self, darkpool: AsyncDarkpoolResource) -> None:
        self._darkpool = darkpool

        self.retrieve = async_to_streamed_response_wrapper(
            darkpool.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            darkpool.list,
        )
