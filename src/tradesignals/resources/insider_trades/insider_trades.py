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
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InsiderTradesResource", "AsyncInsiderTradesResource"]


class InsiderTradesResource(SyncAPIResource):
    @cached_property
    def trades(self) -> TradesResource:
        return TradesResource(self._client)

    @cached_property
    def with_raw_response(self) -> InsiderTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return InsiderTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsiderTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return InsiderTradesResourceWithStreamingResponse(self)


class AsyncInsiderTradesResource(AsyncAPIResource):
    @cached_property
    def trades(self) -> AsyncTradesResource:
        return AsyncTradesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInsiderTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsiderTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsiderTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncInsiderTradesResourceWithStreamingResponse(self)


class InsiderTradesResourceWithRawResponse:
    def __init__(self, insider_trades: InsiderTradesResource) -> None:
        self._insider_trades = insider_trades

    @cached_property
    def trades(self) -> TradesResourceWithRawResponse:
        return TradesResourceWithRawResponse(self._insider_trades.trades)


class AsyncInsiderTradesResourceWithRawResponse:
    def __init__(self, insider_trades: AsyncInsiderTradesResource) -> None:
        self._insider_trades = insider_trades

    @cached_property
    def trades(self) -> AsyncTradesResourceWithRawResponse:
        return AsyncTradesResourceWithRawResponse(self._insider_trades.trades)


class InsiderTradesResourceWithStreamingResponse:
    def __init__(self, insider_trades: InsiderTradesResource) -> None:
        self._insider_trades = insider_trades

    @cached_property
    def trades(self) -> TradesResourceWithStreamingResponse:
        return TradesResourceWithStreamingResponse(self._insider_trades.trades)


class AsyncInsiderTradesResourceWithStreamingResponse:
    def __init__(self, insider_trades: AsyncInsiderTradesResource) -> None:
        self._insider_trades = insider_trades

    @cached_property
    def trades(self) -> AsyncTradesResourceWithStreamingResponse:
        return AsyncTradesResourceWithStreamingResponse(self._insider_trades.trades)
