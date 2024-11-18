# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .candle_data import (
    CandleDataResource,
    AsyncCandleDataResource,
    CandleDataResourceWithRawResponse,
    AsyncCandleDataResourceWithRawResponse,
    CandleDataResourceWithStreamingResponse,
    AsyncCandleDataResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OhlcResource", "AsyncOhlcResource"]


class OhlcResource(SyncAPIResource):
    @cached_property
    def candle_data(self) -> CandleDataResource:
        return CandleDataResource(self._client)

    @cached_property
    def with_raw_response(self) -> OhlcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OhlcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OhlcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OhlcResourceWithStreamingResponse(self)


class AsyncOhlcResource(AsyncAPIResource):
    @cached_property
    def candle_data(self) -> AsyncCandleDataResource:
        return AsyncCandleDataResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOhlcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOhlcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOhlcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOhlcResourceWithStreamingResponse(self)


class OhlcResourceWithRawResponse:
    def __init__(self, ohlc: OhlcResource) -> None:
        self._ohlc = ohlc

    @cached_property
    def candle_data(self) -> CandleDataResourceWithRawResponse:
        return CandleDataResourceWithRawResponse(self._ohlc.candle_data)


class AsyncOhlcResourceWithRawResponse:
    def __init__(self, ohlc: AsyncOhlcResource) -> None:
        self._ohlc = ohlc

    @cached_property
    def candle_data(self) -> AsyncCandleDataResourceWithRawResponse:
        return AsyncCandleDataResourceWithRawResponse(self._ohlc.candle_data)


class OhlcResourceWithStreamingResponse:
    def __init__(self, ohlc: OhlcResource) -> None:
        self._ohlc = ohlc

    @cached_property
    def candle_data(self) -> CandleDataResourceWithStreamingResponse:
        return CandleDataResourceWithStreamingResponse(self._ohlc.candle_data)


class AsyncOhlcResourceWithStreamingResponse:
    def __init__(self, ohlc: AsyncOhlcResource) -> None:
        self._ohlc = ohlc

    @cached_property
    def candle_data(self) -> AsyncCandleDataResourceWithStreamingResponse:
        return AsyncCandleDataResourceWithStreamingResponse(self._ohlc.candle_data)
