# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sectors import (
    SectorsResource,
    AsyncSectorsResource,
    SectorsResourceWithRawResponse,
    AsyncSectorsResourceWithRawResponse,
    SectorsResourceWithStreamingResponse,
    AsyncSectorsResourceWithStreamingResponse,
)
from .activity import (
    ActivityResource,
    AsyncActivityResource,
    ActivityResourceWithRawResponse,
    AsyncActivityResourceWithRawResponse,
    ActivityResourceWithStreamingResponse,
    AsyncActivityResourceWithStreamingResponse,
)
from .holdings import (
    HoldingsResource,
    AsyncHoldingsResource,
    HoldingsResourceWithRawResponse,
    AsyncHoldingsResourceWithRawResponse,
    HoldingsResourceWithStreamingResponse,
    AsyncHoldingsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InstitutionsResource", "AsyncInstitutionsResource"]


class InstitutionsResource(SyncAPIResource):
    @cached_property
    def activity(self) -> ActivityResource:
        return ActivityResource(self._client)

    @cached_property
    def holdings(self) -> HoldingsResource:
        return HoldingsResource(self._client)

    @cached_property
    def sectors(self) -> SectorsResource:
        return SectorsResource(self._client)

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


class AsyncInstitutionsResource(AsyncAPIResource):
    @cached_property
    def activity(self) -> AsyncActivityResource:
        return AsyncActivityResource(self._client)

    @cached_property
    def holdings(self) -> AsyncHoldingsResource:
        return AsyncHoldingsResource(self._client)

    @cached_property
    def sectors(self) -> AsyncSectorsResource:
        return AsyncSectorsResource(self._client)

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


class InstitutionsResourceWithRawResponse:
    def __init__(self, institutions: InstitutionsResource) -> None:
        self._institutions = institutions

    @cached_property
    def activity(self) -> ActivityResourceWithRawResponse:
        return ActivityResourceWithRawResponse(self._institutions.activity)

    @cached_property
    def holdings(self) -> HoldingsResourceWithRawResponse:
        return HoldingsResourceWithRawResponse(self._institutions.holdings)

    @cached_property
    def sectors(self) -> SectorsResourceWithRawResponse:
        return SectorsResourceWithRawResponse(self._institutions.sectors)


class AsyncInstitutionsResourceWithRawResponse:
    def __init__(self, institutions: AsyncInstitutionsResource) -> None:
        self._institutions = institutions

    @cached_property
    def activity(self) -> AsyncActivityResourceWithRawResponse:
        return AsyncActivityResourceWithRawResponse(self._institutions.activity)

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithRawResponse:
        return AsyncHoldingsResourceWithRawResponse(self._institutions.holdings)

    @cached_property
    def sectors(self) -> AsyncSectorsResourceWithRawResponse:
        return AsyncSectorsResourceWithRawResponse(self._institutions.sectors)


class InstitutionsResourceWithStreamingResponse:
    def __init__(self, institutions: InstitutionsResource) -> None:
        self._institutions = institutions

    @cached_property
    def activity(self) -> ActivityResourceWithStreamingResponse:
        return ActivityResourceWithStreamingResponse(self._institutions.activity)

    @cached_property
    def holdings(self) -> HoldingsResourceWithStreamingResponse:
        return HoldingsResourceWithStreamingResponse(self._institutions.holdings)

    @cached_property
    def sectors(self) -> SectorsResourceWithStreamingResponse:
        return SectorsResourceWithStreamingResponse(self._institutions.sectors)


class AsyncInstitutionsResourceWithStreamingResponse:
    def __init__(self, institutions: AsyncInstitutionsResource) -> None:
        self._institutions = institutions

    @cached_property
    def activity(self) -> AsyncActivityResourceWithStreamingResponse:
        return AsyncActivityResourceWithStreamingResponse(self._institutions.activity)

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithStreamingResponse:
        return AsyncHoldingsResourceWithStreamingResponse(self._institutions.holdings)

    @cached_property
    def sectors(self) -> AsyncSectorsResourceWithStreamingResponse:
        return AsyncSectorsResourceWithStreamingResponse(self._institutions.sectors)
