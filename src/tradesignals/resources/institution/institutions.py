# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
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
from ...types.institution import institution_list_params
from ...types.institution.institution_list_response import InstitutionListResponse

__all__ = ["InstitutionsResource", "AsyncInstitutionsResource"]


class InstitutionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstitutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return InstitutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstitutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return InstitutionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        max_share_value: str | NotGiven = NOT_GIVEN,
        max_total_value: str | NotGiven = NOT_GIVEN,
        min_share_value: str | NotGiven = NOT_GIVEN,
        min_total_value: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal[
            "name",
            "call_value",
            "put_value",
            "share_value",
            "call_holdings",
            "put_holdings",
            "share_holdings",
            "total_value",
            "warrant_value",
            "fund_value",
            "pfd_value",
            "debt_value",
            "total_holdings",
            "warrant_holdings",
            "fund_holdings",
            "pfd_holdings",
            "debt_holdings",
            "percent_of_total",
            "date",
            "buy_value",
            "sell_value",
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
    ) -> Optional[InstitutionListResponse]:
        """Returns a list of institutions.

        Args:
          limit: How many items to return.

        Default 500. Max 500. Min 1.

          max_share_value: The maximum share value for the query.

          max_total_value: The maximum total value for the query.

          min_share_value: The minimum share value for the query.

          min_total_value: The minimum total value for the query.

          name: A large entity that manages funds and investments for others. Queryable by name
              or CIK.

          order: Optional columns to order the result by.

          order_direction: Whether to sort descending or ascending. Default is descending.

          page: Page number (use with limit). Starts on page 0.

          tags: An array of institution tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/institutions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "max_share_value": max_share_value,
                        "max_total_value": max_total_value,
                        "min_share_value": min_share_value,
                        "min_total_value": min_total_value,
                        "name": name,
                        "order": order,
                        "order_direction": order_direction,
                        "page": page,
                        "tags": tags,
                    },
                    institution_list_params.InstitutionListParams,
                ),
                post_parser=DataWrapper[Optional[InstitutionListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstitutionListResponse]], DataWrapper[InstitutionListResponse]),
        )


class AsyncInstitutionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstitutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstitutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstitutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncInstitutionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        max_share_value: str | NotGiven = NOT_GIVEN,
        max_total_value: str | NotGiven = NOT_GIVEN,
        min_share_value: str | NotGiven = NOT_GIVEN,
        min_total_value: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal[
            "name",
            "call_value",
            "put_value",
            "share_value",
            "call_holdings",
            "put_holdings",
            "share_holdings",
            "total_value",
            "warrant_value",
            "fund_value",
            "pfd_value",
            "debt_value",
            "total_holdings",
            "warrant_holdings",
            "fund_holdings",
            "pfd_holdings",
            "debt_holdings",
            "percent_of_total",
            "date",
            "buy_value",
            "sell_value",
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
    ) -> Optional[InstitutionListResponse]:
        """Returns a list of institutions.

        Args:
          limit: How many items to return.

        Default 500. Max 500. Min 1.

          max_share_value: The maximum share value for the query.

          max_total_value: The maximum total value for the query.

          min_share_value: The minimum share value for the query.

          min_total_value: The minimum total value for the query.

          name: A large entity that manages funds and investments for others. Queryable by name
              or CIK.

          order: Optional columns to order the result by.

          order_direction: Whether to sort descending or ascending. Default is descending.

          page: Page number (use with limit). Starts on page 0.

          tags: An array of institution tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/institutions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "max_share_value": max_share_value,
                        "max_total_value": max_total_value,
                        "min_share_value": min_share_value,
                        "min_total_value": min_total_value,
                        "name": name,
                        "order": order,
                        "order_direction": order_direction,
                        "page": page,
                        "tags": tags,
                    },
                    institution_list_params.InstitutionListParams,
                ),
                post_parser=DataWrapper[Optional[InstitutionListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[InstitutionListResponse]], DataWrapper[InstitutionListResponse]),
        )


class InstitutionsResourceWithRawResponse:
    def __init__(self, institutions: InstitutionsResource) -> None:
        self._institutions = institutions

        self.list = to_raw_response_wrapper(
            institutions.list,
        )


class AsyncInstitutionsResourceWithRawResponse:
    def __init__(self, institutions: AsyncInstitutionsResource) -> None:
        self._institutions = institutions

        self.list = async_to_raw_response_wrapper(
            institutions.list,
        )


class InstitutionsResourceWithStreamingResponse:
    def __init__(self, institutions: InstitutionsResource) -> None:
        self._institutions = institutions

        self.list = to_streamed_response_wrapper(
            institutions.list,
        )


class AsyncInstitutionsResourceWithStreamingResponse:
    def __init__(self, institutions: AsyncInstitutionsResource) -> None:
        self._institutions = institutions

        self.list = async_to_streamed_response_wrapper(
            institutions.list,
        )
