# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .trades import (
    TradesResource,
    AsyncTradesResource,
    TradesResourceWithRawResponse,
    AsyncTradesResourceWithRawResponse,
    TradesResourceWithStreamingResponse,
    AsyncTradesResourceWithStreamingResponse,
)
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CongressResource", "AsyncCongressResource"]


class CongressResource(SyncAPIResource):
    @cached_property
    def trades(self) -> TradesResource:
        return TradesResource(self._client)

    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> CongressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return CongressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CongressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return CongressResourceWithStreamingResponse(self)


class AsyncCongressResource(AsyncAPIResource):
    @cached_property
    def trades(self) -> AsyncTradesResource:
        return AsyncTradesResource(self._client)

    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCongressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCongressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCongressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncCongressResourceWithStreamingResponse(self)


class CongressResourceWithRawResponse:
    def __init__(self, congress: CongressResource) -> None:
        self._congress = congress

    @cached_property
    def trades(self) -> TradesResourceWithRawResponse:
        return TradesResourceWithRawResponse(self._congress.trades)

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._congress.members)


class AsyncCongressResourceWithRawResponse:
    def __init__(self, congress: AsyncCongressResource) -> None:
        self._congress = congress

    @cached_property
    def trades(self) -> AsyncTradesResourceWithRawResponse:
        return AsyncTradesResourceWithRawResponse(self._congress.trades)

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._congress.members)


class CongressResourceWithStreamingResponse:
    def __init__(self, congress: CongressResource) -> None:
        self._congress = congress

    @cached_property
    def trades(self) -> TradesResourceWithStreamingResponse:
        return TradesResourceWithStreamingResponse(self._congress.trades)

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._congress.members)


class AsyncCongressResourceWithStreamingResponse:
    def __init__(self, congress: AsyncCongressResource) -> None:
        self._congress = congress

    @cached_property
    def trades(self) -> AsyncTradesResourceWithStreamingResponse:
        return AsyncTradesResourceWithStreamingResponse(self._congress.trades)

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._congress.members)
