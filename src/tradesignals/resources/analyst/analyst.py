# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .ratings import (
    RatingsResource,
    AsyncRatingsResource,
    RatingsResourceWithRawResponse,
    AsyncRatingsResourceWithRawResponse,
    RatingsResourceWithStreamingResponse,
    AsyncRatingsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AnalystResource", "AsyncAnalystResource"]


class AnalystResource(SyncAPIResource):
    @cached_property
    def ratings(self) -> RatingsResource:
        return RatingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnalystResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AnalystResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalystResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AnalystResourceWithStreamingResponse(self)


class AsyncAnalystResource(AsyncAPIResource):
    @cached_property
    def ratings(self) -> AsyncRatingsResource:
        return AsyncRatingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalystResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalystResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalystResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncAnalystResourceWithStreamingResponse(self)


class AnalystResourceWithRawResponse:
    def __init__(self, analyst: AnalystResource) -> None:
        self._analyst = analyst

    @cached_property
    def ratings(self) -> RatingsResourceWithRawResponse:
        return RatingsResourceWithRawResponse(self._analyst.ratings)


class AsyncAnalystResourceWithRawResponse:
    def __init__(self, analyst: AsyncAnalystResource) -> None:
        self._analyst = analyst

    @cached_property
    def ratings(self) -> AsyncRatingsResourceWithRawResponse:
        return AsyncRatingsResourceWithRawResponse(self._analyst.ratings)


class AnalystResourceWithStreamingResponse:
    def __init__(self, analyst: AnalystResource) -> None:
        self._analyst = analyst

    @cached_property
    def ratings(self) -> RatingsResourceWithStreamingResponse:
        return RatingsResourceWithStreamingResponse(self._analyst.ratings)


class AsyncAnalystResourceWithStreamingResponse:
    def __init__(self, analyst: AsyncAnalystResource) -> None:
        self._analyst = analyst

    @cached_property
    def ratings(self) -> AsyncRatingsResourceWithStreamingResponse:
        return AsyncRatingsResourceWithStreamingResponse(self._analyst.ratings)
