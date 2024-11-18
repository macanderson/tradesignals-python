# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast
from datetime import date
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
from ...types.institution import holding_list_params
from ...types.institution.holding_list_response import HoldingListResponse

__all__ = ["HoldingsResource", "AsyncHoldingsResource"]


class HoldingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HoldingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return HoldingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HoldingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return HoldingsResourceWithStreamingResponse(self)

    def list(
        self,
        name: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal[
            "date",
            "ticker",
            "security_type",
            "put_call",
            "first_buy",
            "price_first_buy",
            "units",
            "units_change",
            "historical_units",
            "value",
            "avg_price",
            "close",
            "shares_outstanding",
        ]
        | NotGiven = NOT_GIVEN,
        order_direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        security_types: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HoldingListResponse]:
        """
        Returns the holdings for a given institution.

        Args:
          date: A trading date in the format of YYYY-MM-DD. Defaults to the last trading date if
              not provided.

          limit: How many items to return. Default 500. Max 500. Min 1.

          order: Optional columns to order the result by.

          order_direction: Whether to sort descending or ascending. Default is descending.

          page: Page number (use with limit). Starts on page 0.

          security_types: An array of security types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/api/institution/{name}/holdings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "order": order,
                        "order_direction": order_direction,
                        "page": page,
                        "security_types": security_types,
                    },
                    holding_list_params.HoldingListParams,
                ),
                post_parser=DataWrapper[Optional[HoldingListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HoldingListResponse]], DataWrapper[HoldingListResponse]),
        )


class AsyncHoldingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHoldingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHoldingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHoldingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncHoldingsResourceWithStreamingResponse(self)

    async def list(
        self,
        name: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal[
            "date",
            "ticker",
            "security_type",
            "put_call",
            "first_buy",
            "price_first_buy",
            "units",
            "units_change",
            "historical_units",
            "value",
            "avg_price",
            "close",
            "shares_outstanding",
        ]
        | NotGiven = NOT_GIVEN,
        order_direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        security_types: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HoldingListResponse]:
        """
        Returns the holdings for a given institution.

        Args:
          date: A trading date in the format of YYYY-MM-DD. Defaults to the last trading date if
              not provided.

          limit: How many items to return. Default 500. Max 500. Min 1.

          order: Optional columns to order the result by.

          order_direction: Whether to sort descending or ascending. Default is descending.

          page: Page number (use with limit). Starts on page 0.

          security_types: An array of security types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/api/institution/{name}/holdings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "order": order,
                        "order_direction": order_direction,
                        "page": page,
                        "security_types": security_types,
                    },
                    holding_list_params.HoldingListParams,
                ),
                post_parser=DataWrapper[Optional[HoldingListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HoldingListResponse]], DataWrapper[HoldingListResponse]),
        )


class HoldingsResourceWithRawResponse:
    def __init__(self, holdings: HoldingsResource) -> None:
        self._holdings = holdings

        self.list = to_raw_response_wrapper(
            holdings.list,
        )


class AsyncHoldingsResourceWithRawResponse:
    def __init__(self, holdings: AsyncHoldingsResource) -> None:
        self._holdings = holdings

        self.list = async_to_raw_response_wrapper(
            holdings.list,
        )


class HoldingsResourceWithStreamingResponse:
    def __init__(self, holdings: HoldingsResource) -> None:
        self._holdings = holdings

        self.list = to_streamed_response_wrapper(
            holdings.list,
        )


class AsyncHoldingsResourceWithStreamingResponse:
    def __init__(self, holdings: AsyncHoldingsResource) -> None:
        self._holdings = holdings

        self.list = async_to_streamed_response_wrapper(
            holdings.list,
        )
