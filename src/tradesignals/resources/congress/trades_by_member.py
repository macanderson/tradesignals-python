# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ..._base_client import make_request_options
from ...types.congress import trades_by_member_retrieve_params
from ...types.congress.congress_trader_response import CongressTraderResponse

__all__ = ["TradesByMemberResource", "AsyncTradesByMemberResource"]


class TradesByMemberResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TradesByMemberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return TradesByMemberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TradesByMemberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return TradesByMemberResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CongressTraderResponse:
        """
        Returns the recent trade disclosures filed by congress member.

        Args:
          date: A trading date in the format of YYYY-MM-DD. This is optional and by default the
              last trading date.

          limit: How many items to return

          name: The full name of a congress member. Cannot contain digits/numbers. Spaces need
              to be replaced with either '+' or '%20'. Defaults to Nancy Pelosi.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/congress/congress-trader",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "name": name,
                    },
                    trades_by_member_retrieve_params.TradesByMemberRetrieveParams,
                ),
            ),
            cast_to=CongressTraderResponse,
        )


class AsyncTradesByMemberResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTradesByMemberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTradesByMemberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTradesByMemberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncTradesByMemberResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CongressTraderResponse:
        """
        Returns the recent trade disclosures filed by congress member.

        Args:
          date: A trading date in the format of YYYY-MM-DD. This is optional and by default the
              last trading date.

          limit: How many items to return

          name: The full name of a congress member. Cannot contain digits/numbers. Spaces need
              to be replaced with either '+' or '%20'. Defaults to Nancy Pelosi.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/congress/congress-trader",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "name": name,
                    },
                    trades_by_member_retrieve_params.TradesByMemberRetrieveParams,
                ),
            ),
            cast_to=CongressTraderResponse,
        )


class TradesByMemberResourceWithRawResponse:
    def __init__(self, trades_by_member: TradesByMemberResource) -> None:
        self._trades_by_member = trades_by_member

        self.retrieve = to_raw_response_wrapper(
            trades_by_member.retrieve,
        )


class AsyncTradesByMemberResourceWithRawResponse:
    def __init__(self, trades_by_member: AsyncTradesByMemberResource) -> None:
        self._trades_by_member = trades_by_member

        self.retrieve = async_to_raw_response_wrapper(
            trades_by_member.retrieve,
        )


class TradesByMemberResourceWithStreamingResponse:
    def __init__(self, trades_by_member: TradesByMemberResource) -> None:
        self._trades_by_member = trades_by_member

        self.retrieve = to_streamed_response_wrapper(
            trades_by_member.retrieve,
        )


class AsyncTradesByMemberResourceWithStreamingResponse:
    def __init__(self, trades_by_member: AsyncTradesByMemberResource) -> None:
        self._trades_by_member = trades_by_member

        self.retrieve = async_to_streamed_response_wrapper(
            trades_by_member.retrieve,
        )
