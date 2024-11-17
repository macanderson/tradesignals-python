# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import date

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
from ...types.institutions import activity_list_params
from ...types.institutions.activity_list_response import ActivityListResponse

__all__ = ["ActivityResource", "AsyncActivityResource"]


class ActivityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return ActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return ActivityResourceWithStreamingResponse(self)

    def list(
        self,
        name: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ActivityListResponse]:
        """
        Fetches the trading activities for a given institution.

        Args:
          date: A date in the format of YYYY-MM-DD.

          limit: How many items to return. Default 500. Max 500. Min 1.

          page: Page number (use with limit). Starts on page 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/api/institution/{name}/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                    },
                    activity_list_params.ActivityListParams,
                ),
                post_parser=DataWrapper[Optional[ActivityListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ActivityListResponse]], DataWrapper[ActivityListResponse]),
        )


class AsyncActivityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncActivityResourceWithStreamingResponse(self)

    async def list(
        self,
        name: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ActivityListResponse]:
        """
        Fetches the trading activities for a given institution.

        Args:
          date: A date in the format of YYYY-MM-DD.

          limit: How many items to return. Default 500. Max 500. Min 1.

          page: Page number (use with limit). Starts on page 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/api/institution/{name}/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                    },
                    activity_list_params.ActivityListParams,
                ),
                post_parser=DataWrapper[Optional[ActivityListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ActivityListResponse]], DataWrapper[ActivityListResponse]),
        )


class ActivityResourceWithRawResponse:
    def __init__(self, activity: ActivityResource) -> None:
        self._activity = activity

        self.list = to_raw_response_wrapper(
            activity.list,
        )


class AsyncActivityResourceWithRawResponse:
    def __init__(self, activity: AsyncActivityResource) -> None:
        self._activity = activity

        self.list = async_to_raw_response_wrapper(
            activity.list,
        )


class ActivityResourceWithStreamingResponse:
    def __init__(self, activity: ActivityResource) -> None:
        self._activity = activity

        self.list = to_streamed_response_wrapper(
            activity.list,
        )


class AsyncActivityResourceWithStreamingResponse:
    def __init__(self, activity: AsyncActivityResource) -> None:
        self._activity = activity

        self.list = async_to_streamed_response_wrapper(
            activity.list,
        )
