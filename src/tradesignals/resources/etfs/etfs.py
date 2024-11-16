# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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

__all__ = ["EtfsResource", "AsyncEtfsResource"]


class EtfsResource(SyncAPIResource):
    @cached_property
    def holdings(self) -> HoldingsResource:
        return HoldingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EtfsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return EtfsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EtfsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return EtfsResourceWithStreamingResponse(self)


class AsyncEtfsResource(AsyncAPIResource):
    @cached_property
    def holdings(self) -> AsyncHoldingsResource:
        return AsyncHoldingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEtfsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEtfsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEtfsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncEtfsResourceWithStreamingResponse(self)


class EtfsResourceWithRawResponse:
    def __init__(self, etfs: EtfsResource) -> None:
        self._etfs = etfs

    @cached_property
    def holdings(self) -> HoldingsResourceWithRawResponse:
        return HoldingsResourceWithRawResponse(self._etfs.holdings)


class AsyncEtfsResourceWithRawResponse:
    def __init__(self, etfs: AsyncEtfsResource) -> None:
        self._etfs = etfs

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithRawResponse:
        return AsyncHoldingsResourceWithRawResponse(self._etfs.holdings)


class EtfsResourceWithStreamingResponse:
    def __init__(self, etfs: EtfsResource) -> None:
        self._etfs = etfs

    @cached_property
    def holdings(self) -> HoldingsResourceWithStreamingResponse:
        return HoldingsResourceWithStreamingResponse(self._etfs.holdings)


class AsyncEtfsResourceWithStreamingResponse:
    def __init__(self, etfs: AsyncEtfsResource) -> None:
        self._etfs = etfs

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithStreamingResponse:
        return AsyncHoldingsResourceWithStreamingResponse(self._etfs.holdings)
