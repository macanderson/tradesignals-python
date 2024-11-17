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
from ...types.screeners import analyst_rating_list_params
from ...types.screeners.analyst_rating_list_response import AnalystRatingListResponse

__all__ = ["AnalystRatingsResource", "AsyncAnalystRatingsResource"]


class AnalystRatingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnalystRatingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AnalystRatingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalystRatingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AnalystRatingsResourceWithStreamingResponse(self)

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
    ) -> Optional[AnalystRatingListResponse]:
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
                    analyst_rating_list_params.AnalystRatingListParams,
                ),
                post_parser=DataWrapper[Optional[AnalystRatingListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AnalystRatingListResponse]], DataWrapper[AnalystRatingListResponse]),
        )


class AsyncAnalystRatingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnalystRatingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalystRatingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalystRatingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncAnalystRatingsResourceWithStreamingResponse(self)

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
    ) -> Optional[AnalystRatingListResponse]:
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
                    analyst_rating_list_params.AnalystRatingListParams,
                ),
                post_parser=DataWrapper[Optional[AnalystRatingListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AnalystRatingListResponse]], DataWrapper[AnalystRatingListResponse]),
        )


class AnalystRatingsResourceWithRawResponse:
    def __init__(self, analyst_ratings: AnalystRatingsResource) -> None:
        self._analyst_ratings = analyst_ratings

        self.list = to_raw_response_wrapper(
            analyst_ratings.list,
        )


class AsyncAnalystRatingsResourceWithRawResponse:
    def __init__(self, analyst_ratings: AsyncAnalystRatingsResource) -> None:
        self._analyst_ratings = analyst_ratings

        self.list = async_to_raw_response_wrapper(
            analyst_ratings.list,
        )


class AnalystRatingsResourceWithStreamingResponse:
    def __init__(self, analyst_ratings: AnalystRatingsResource) -> None:
        self._analyst_ratings = analyst_ratings

        self.list = to_streamed_response_wrapper(
            analyst_ratings.list,
        )


class AsyncAnalystRatingsResourceWithStreamingResponse:
    def __init__(self, analyst_ratings: AsyncAnalystRatingsResource) -> None:
        self._analyst_ratings = analyst_ratings

        self.list = async_to_streamed_response_wrapper(
            analyst_ratings.list,
        )
