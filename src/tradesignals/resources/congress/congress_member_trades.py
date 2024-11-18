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
from ...types.congress import congress_member_trade_list_params
from ...types.congress.congress_member_trade_list_response import CongressMemberTradeListResponse

__all__ = ["CongressMemberTradesResource", "AsyncCongressMemberTradesResource"]


class CongressMemberTradesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CongressMemberTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return CongressMemberTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CongressMemberTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return CongressMemberTradesResourceWithStreamingResponse(self)

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
    ) -> Optional[CongressMemberTradeListResponse]:
        """Returns the latest transacted trades by congress members.

        If a date is given,
        will only return reports with a transaction date &le; the given input date.

        Args:
          date: A trading date in the format of YYYY-MM-DD. This is optional and by default the
              last trading date.

          limit: How many items to return. Default&colon; 100. Max&colon; 200. Min&colon; 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/congress/recent-trades",
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
                    congress_member_trade_list_params.CongressMemberTradeListParams,
                ),
                post_parser=DataWrapper[Optional[CongressMemberTradeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CongressMemberTradeListResponse]], DataWrapper[CongressMemberTradeListResponse]),
        )


class AsyncCongressMemberTradesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCongressMemberTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCongressMemberTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCongressMemberTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncCongressMemberTradesResourceWithStreamingResponse(self)

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
    ) -> Optional[CongressMemberTradeListResponse]:
        """Returns the latest transacted trades by congress members.

        If a date is given,
        will only return reports with a transaction date &le; the given input date.

        Args:
          date: A trading date in the format of YYYY-MM-DD. This is optional and by default the
              last trading date.

          limit: How many items to return. Default&colon; 100. Max&colon; 200. Min&colon; 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/congress/recent-trades",
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
                    congress_member_trade_list_params.CongressMemberTradeListParams,
                ),
                post_parser=DataWrapper[Optional[CongressMemberTradeListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CongressMemberTradeListResponse]], DataWrapper[CongressMemberTradeListResponse]),
        )


class CongressMemberTradesResourceWithRawResponse:
    def __init__(self, congress_member_trades: CongressMemberTradesResource) -> None:
        self._congress_member_trades = congress_member_trades

        self.list = to_raw_response_wrapper(
            congress_member_trades.list,
        )


class AsyncCongressMemberTradesResourceWithRawResponse:
    def __init__(self, congress_member_trades: AsyncCongressMemberTradesResource) -> None:
        self._congress_member_trades = congress_member_trades

        self.list = async_to_raw_response_wrapper(
            congress_member_trades.list,
        )


class CongressMemberTradesResourceWithStreamingResponse:
    def __init__(self, congress_member_trades: CongressMemberTradesResource) -> None:
        self._congress_member_trades = congress_member_trades

        self.list = to_streamed_response_wrapper(
            congress_member_trades.list,
        )


class AsyncCongressMemberTradesResourceWithStreamingResponse:
    def __init__(self, congress_member_trades: AsyncCongressMemberTradesResource) -> None:
        self._congress_member_trades = congress_member_trades

        self.list = async_to_streamed_response_wrapper(
            congress_member_trades.list,
        )
