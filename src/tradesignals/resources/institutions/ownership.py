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
from ...types.institutions import ownership_list_params
from ...types.institutions.ownership_list_response import OwnershipListResponse

__all__ = ["OwnershipResource", "AsyncOwnershipResource"]


class OwnershipResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OwnershipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OwnershipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OwnershipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OwnershipResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal[
            "name",
            "short_name",
            "first_buy",
            "units",
            "units_change",
            "units_changed",
            "value",
            "avg_price",
            "perc_outstanding",
            "perc_units_changed",
            "activity",
            "perc_inst_value",
            "perc_share_value",
        ]
        | NotGiven = NOT_GIVEN,
        order_direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OwnershipListResponse]:
        """
        Returns the institutional ownership of a given ticker.

        Args:
          date: A trading date in the format of YYYY-MM-DD. Defaults to the last trading date if
              not provided.

          limit: How many items to return. Default 500. Max 500. Min 1.

          order: Optional columns to order the result by.

          order_direction: Whether to sort descending or ascending. Default is descending.

          page: Page number (use with limit). Starts on page 0.

          tags: An array of institution tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/institution/{ticker}/ownership",
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
                        "tags": tags,
                    },
                    ownership_list_params.OwnershipListParams,
                ),
                post_parser=DataWrapper[Optional[OwnershipListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OwnershipListResponse]], DataWrapper[OwnershipListResponse]),
        )


class AsyncOwnershipResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOwnershipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOwnershipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOwnershipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOwnershipResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal[
            "name",
            "short_name",
            "first_buy",
            "units",
            "units_change",
            "units_changed",
            "value",
            "avg_price",
            "perc_outstanding",
            "perc_units_changed",
            "activity",
            "perc_inst_value",
            "perc_share_value",
        ]
        | NotGiven = NOT_GIVEN,
        order_direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OwnershipListResponse]:
        """
        Returns the institutional ownership of a given ticker.

        Args:
          date: A trading date in the format of YYYY-MM-DD. Defaults to the last trading date if
              not provided.

          limit: How many items to return. Default 500. Max 500. Min 1.

          order: Optional columns to order the result by.

          order_direction: Whether to sort descending or ascending. Default is descending.

          page: Page number (use with limit). Starts on page 0.

          tags: An array of institution tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/institution/{ticker}/ownership",
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
                        "tags": tags,
                    },
                    ownership_list_params.OwnershipListParams,
                ),
                post_parser=DataWrapper[Optional[OwnershipListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OwnershipListResponse]], DataWrapper[OwnershipListResponse]),
        )


class OwnershipResourceWithRawResponse:
    def __init__(self, ownership: OwnershipResource) -> None:
        self._ownership = ownership

        self.list = to_raw_response_wrapper(
            ownership.list,
        )


class AsyncOwnershipResourceWithRawResponse:
    def __init__(self, ownership: AsyncOwnershipResource) -> None:
        self._ownership = ownership

        self.list = async_to_raw_response_wrapper(
            ownership.list,
        )


class OwnershipResourceWithStreamingResponse:
    def __init__(self, ownership: OwnershipResource) -> None:
        self._ownership = ownership

        self.list = to_streamed_response_wrapper(
            ownership.list,
        )


class AsyncOwnershipResourceWithStreamingResponse:
    def __init__(self, ownership: AsyncOwnershipResource) -> None:
        self._ownership = ownership

        self.list = async_to_streamed_response_wrapper(
            ownership.list,
        )
