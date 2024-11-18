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
from ...types.earnings import premarket_earning_list_params
from ...types.earnings.premarket_earning_list_response import PremarketEarningListResponse

__all__ = ["PremarketEarningsResource", "AsyncPremarketEarningsResource"]


class PremarketEarningsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PremarketEarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return PremarketEarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PremarketEarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return PremarketEarningsResourceWithStreamingResponse(self)

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
    ) -> Optional[PremarketEarningListResponse]:
        """Returns the next upcoming premarket earnings for the given date.

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
            "/api/earnings/premarket",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, premarket_earning_list_params.PremarketEarningListParams),
                post_parser=DataWrapper[Optional[PremarketEarningListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PremarketEarningListResponse]], DataWrapper[PremarketEarningListResponse]),
        )


class AsyncPremarketEarningsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPremarketEarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPremarketEarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPremarketEarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncPremarketEarningsResourceWithStreamingResponse(self)

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
    ) -> Optional[PremarketEarningListResponse]:
        """Returns the next upcoming premarket earnings for the given date.

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
            "/api/earnings/premarket",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"date": date}, premarket_earning_list_params.PremarketEarningListParams
                ),
                post_parser=DataWrapper[Optional[PremarketEarningListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PremarketEarningListResponse]], DataWrapper[PremarketEarningListResponse]),
        )


class PremarketEarningsResourceWithRawResponse:
    def __init__(self, premarket_earnings: PremarketEarningsResource) -> None:
        self._premarket_earnings = premarket_earnings

        self.list = to_raw_response_wrapper(
            premarket_earnings.list,
        )


class AsyncPremarketEarningsResourceWithRawResponse:
    def __init__(self, premarket_earnings: AsyncPremarketEarningsResource) -> None:
        self._premarket_earnings = premarket_earnings

        self.list = async_to_raw_response_wrapper(
            premarket_earnings.list,
        )


class PremarketEarningsResourceWithStreamingResponse:
    def __init__(self, premarket_earnings: PremarketEarningsResource) -> None:
        self._premarket_earnings = premarket_earnings

        self.list = to_streamed_response_wrapper(
            premarket_earnings.list,
        )


class AsyncPremarketEarningsResourceWithStreamingResponse:
    def __init__(self, premarket_earnings: AsyncPremarketEarningsResource) -> None:
        self._premarket_earnings = premarket_earnings

        self.list = async_to_streamed_response_wrapper(
            premarket_earnings.list,
        )
