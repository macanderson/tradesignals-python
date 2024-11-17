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
from ...types.earnings import afterhour_list_params
from ...types.earnings.afterhour_list_response import AfterhourListResponse

__all__ = ["AfterhoursResource", "AsyncAfterhoursResource"]


class AfterhoursResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AfterhoursResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AfterhoursResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AfterhoursResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AfterhoursResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AfterhourListResponse]:
        """Returns the next upcoming afterhours earnings for the given date.

        Date must be
        the current or a past date. If no date is given, returns data for the
        current/last market day.

        Args:
          date: A trading date in the format of YYYY-MM-DD. This is optional and defaults to the
              last trading date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/earnings/afterhours",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, afterhour_list_params.AfterhourListParams),
                post_parser=DataWrapper[Optional[AfterhourListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AfterhourListResponse]], DataWrapper[AfterhourListResponse]),
        )


class AsyncAfterhoursResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAfterhoursResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAfterhoursResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAfterhoursResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncAfterhoursResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AfterhourListResponse]:
        """Returns the next upcoming afterhours earnings for the given date.

        Date must be
        the current or a past date. If no date is given, returns data for the
        current/last market day.

        Args:
          date: A trading date in the format of YYYY-MM-DD. This is optional and defaults to the
              last trading date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/earnings/afterhours",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"date": date}, afterhour_list_params.AfterhourListParams),
                post_parser=DataWrapper[Optional[AfterhourListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AfterhourListResponse]], DataWrapper[AfterhourListResponse]),
        )


class AfterhoursResourceWithRawResponse:
    def __init__(self, afterhours: AfterhoursResource) -> None:
        self._afterhours = afterhours

        self.list = to_raw_response_wrapper(
            afterhours.list,
        )


class AsyncAfterhoursResourceWithRawResponse:
    def __init__(self, afterhours: AsyncAfterhoursResource) -> None:
        self._afterhours = afterhours

        self.list = async_to_raw_response_wrapper(
            afterhours.list,
        )


class AfterhoursResourceWithStreamingResponse:
    def __init__(self, afterhours: AfterhoursResource) -> None:
        self._afterhours = afterhours

        self.list = to_streamed_response_wrapper(
            afterhours.list,
        )


class AsyncAfterhoursResourceWithStreamingResponse:
    def __init__(self, afterhours: AsyncAfterhoursResource) -> None:
        self._afterhours = afterhours

        self.list = async_to_streamed_response_wrapper(
            afterhours.list,
        )
