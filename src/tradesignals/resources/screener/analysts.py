# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ...types.screener import analyst_list_params
from ...types.screener.analyst_list_response import AnalystListResponse

__all__ = ["AnalystsResource", "AsyncAnalystsResource"]


class AnalystsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalystsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AnalystsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalystsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AnalystsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        action: Literal["initiated", "reiterated", "downgraded", "upgraded", "maintained"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        recommendation: Literal["buy", "hold", "sell"] | NotGiven = NOT_GIVEN,
        ticker: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AnalystListResponse]:
        """
        Returns the latest analyst ratings for the given ticker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/screener/analysts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "limit": limit,
                        "recommendation": recommendation,
                        "ticker": ticker,
                    },
                    analyst_list_params.AnalystListParams,
                ),
                post_parser=DataWrapper[Optional[AnalystListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AnalystListResponse]], DataWrapper[AnalystListResponse]),
        )


class AsyncAnalystsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalystsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalystsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalystsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncAnalystsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        action: Literal["initiated", "reiterated", "downgraded", "upgraded", "maintained"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        recommendation: Literal["buy", "hold", "sell"] | NotGiven = NOT_GIVEN,
        ticker: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AnalystListResponse]:
        """
        Returns the latest analyst ratings for the given ticker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/screener/analysts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "action": action,
                        "limit": limit,
                        "recommendation": recommendation,
                        "ticker": ticker,
                    },
                    analyst_list_params.AnalystListParams,
                ),
                post_parser=DataWrapper[Optional[AnalystListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AnalystListResponse]], DataWrapper[AnalystListResponse]),
        )


class AnalystsResourceWithRawResponse:
    def __init__(self, analysts: AnalystsResource) -> None:
        self._analysts = analysts

        self.list = to_raw_response_wrapper(
            analysts.list,
        )


class AsyncAnalystsResourceWithRawResponse:
    def __init__(self, analysts: AsyncAnalystsResource) -> None:
        self._analysts = analysts

        self.list = async_to_raw_response_wrapper(
            analysts.list,
        )


class AnalystsResourceWithStreamingResponse:
    def __init__(self, analysts: AnalystsResource) -> None:
        self._analysts = analysts

        self.list = to_streamed_response_wrapper(
            analysts.list,
        )


class AsyncAnalystsResourceWithStreamingResponse:
    def __init__(self, analysts: AsyncAnalystsResource) -> None:
        self._analysts = analysts

        self.list = async_to_streamed_response_wrapper(
            analysts.list,
        )
