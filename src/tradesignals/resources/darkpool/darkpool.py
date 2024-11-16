# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .transactions import (
    TransactionsResource,
    AsyncTransactionsResource,
    TransactionsResourceWithRawResponse,
    AsyncTransactionsResourceWithRawResponse,
    TransactionsResourceWithStreamingResponse,
    AsyncTransactionsResourceWithStreamingResponse,
)

__all__ = ["DarkpoolResource", "AsyncDarkpoolResource"]


class DarkpoolResource(SyncAPIResource):
    @cached_property
    def transactions(self) -> TransactionsResource:
        return TransactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DarkpoolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return DarkpoolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DarkpoolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#with_streaming_response
        """
        return DarkpoolResourceWithStreamingResponse(self)


class AsyncDarkpoolResource(AsyncAPIResource):
    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        return AsyncTransactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDarkpoolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDarkpoolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDarkpoolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#with_streaming_response
        """
        return AsyncDarkpoolResourceWithStreamingResponse(self)


class DarkpoolResourceWithRawResponse:
    def __init__(self, darkpool: DarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self._darkpool.transactions)


class AsyncDarkpoolResourceWithRawResponse:
    def __init__(self, darkpool: AsyncDarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        return AsyncTransactionsResourceWithRawResponse(self._darkpool.transactions)


class DarkpoolResourceWithStreamingResponse:
    def __init__(self, darkpool: DarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self._darkpool.transactions)


class AsyncDarkpoolResourceWithStreamingResponse:
    def __init__(self, darkpool: AsyncDarkpoolResource) -> None:
        self._darkpool = darkpool

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self._darkpool.transactions)
