# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.insider_trades.congress_member_list_response import CongressMemberListResponse

__all__ = ["CongressMembersResource", "AsyncCongressMembersResource"]


class CongressMembersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CongressMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return CongressMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CongressMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return CongressMembersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CongressMemberListResponse:
        """Retrieve a list of Congress members who have reported trades."""
        return self._get(
            "/api/congress/members",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CongressMemberListResponse,
        )


class AsyncCongressMembersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCongressMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCongressMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCongressMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncCongressMembersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CongressMemberListResponse:
        """Retrieve a list of Congress members who have reported trades."""
        return await self._get(
            "/api/congress/members",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CongressMemberListResponse,
        )


class CongressMembersResourceWithRawResponse:
    def __init__(self, congress_members: CongressMembersResource) -> None:
        self._congress_members = congress_members

        self.list = to_raw_response_wrapper(
            congress_members.list,
        )


class AsyncCongressMembersResourceWithRawResponse:
    def __init__(self, congress_members: AsyncCongressMembersResource) -> None:
        self._congress_members = congress_members

        self.list = async_to_raw_response_wrapper(
            congress_members.list,
        )


class CongressMembersResourceWithStreamingResponse:
    def __init__(self, congress_members: CongressMembersResource) -> None:
        self._congress_members = congress_members

        self.list = to_streamed_response_wrapper(
            congress_members.list,
        )


class AsyncCongressMembersResourceWithStreamingResponse:
    def __init__(self, congress_members: AsyncCongressMembersResource) -> None:
        self._congress_members = congress_members

        self.list = async_to_streamed_response_wrapper(
            congress_members.list,
        )
