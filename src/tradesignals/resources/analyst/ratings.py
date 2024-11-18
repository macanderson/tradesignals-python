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
from ...types.analyst import rating_list_params
from ...types.analyst.rating_list_response import RatingListResponse

__all__ = ["RatingsResource", "AsyncRatingsResource"]


class RatingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RatingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return RatingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RatingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return RatingsResourceWithStreamingResponse(self)

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
    ) -> Optional[RatingListResponse]:
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
                    rating_list_params.RatingListParams,
                ),
                post_parser=DataWrapper[Optional[RatingListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RatingListResponse]], DataWrapper[RatingListResponse]),
        )


class AsyncRatingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRatingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRatingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRatingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncRatingsResourceWithStreamingResponse(self)

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
    ) -> Optional[RatingListResponse]:
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
                    rating_list_params.RatingListParams,
                ),
                post_parser=DataWrapper[Optional[RatingListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RatingListResponse]], DataWrapper[RatingListResponse]),
        )


class RatingsResourceWithRawResponse:
    def __init__(self, ratings: RatingsResource) -> None:
        self._ratings = ratings

        self.list = to_raw_response_wrapper(
            ratings.list,
        )


class AsyncRatingsResourceWithRawResponse:
    def __init__(self, ratings: AsyncRatingsResource) -> None:
        self._ratings = ratings

        self.list = async_to_raw_response_wrapper(
            ratings.list,
        )


class RatingsResourceWithStreamingResponse:
    def __init__(self, ratings: RatingsResource) -> None:
        self._ratings = ratings

        self.list = to_streamed_response_wrapper(
            ratings.list,
        )


class AsyncRatingsResourceWithStreamingResponse:
    def __init__(self, ratings: AsyncRatingsResource) -> None:
        self._ratings = ratings

        self.list = async_to_streamed_response_wrapper(
            ratings.list,
        )
