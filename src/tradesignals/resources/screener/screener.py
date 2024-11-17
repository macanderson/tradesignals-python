# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .analysts import (
    AnalystsResource,
    AsyncAnalystsResource,
    AnalystsResourceWithRawResponse,
    AsyncAnalystsResourceWithRawResponse,
    AnalystsResourceWithStreamingResponse,
    AsyncAnalystsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .option_contracts import (
    OptionContractsResource,
    AsyncOptionContractsResource,
    OptionContractsResourceWithRawResponse,
    AsyncOptionContractsResourceWithRawResponse,
    OptionContractsResourceWithStreamingResponse,
    AsyncOptionContractsResourceWithStreamingResponse,
)

__all__ = ["ScreenerResource", "AsyncScreenerResource"]


class ScreenerResource(SyncAPIResource):
    @cached_property
    def analysts(self) -> AnalystsResource:
        return AnalystsResource(self._client)

    @cached_property
    def option_contracts(self) -> OptionContractsResource:
        return OptionContractsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return ScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return ScreenerResourceWithStreamingResponse(self)


class AsyncScreenerResource(AsyncAPIResource):
    @cached_property
    def analysts(self) -> AsyncAnalystsResource:
        return AsyncAnalystsResource(self._client)

    @cached_property
    def option_contracts(self) -> AsyncOptionContractsResource:
        return AsyncOptionContractsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScreenerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScreenerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncScreenerResourceWithStreamingResponse(self)


class ScreenerResourceWithRawResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

    @cached_property
    def analysts(self) -> AnalystsResourceWithRawResponse:
        return AnalystsResourceWithRawResponse(self._screener.analysts)

    @cached_property
    def option_contracts(self) -> OptionContractsResourceWithRawResponse:
        return OptionContractsResourceWithRawResponse(self._screener.option_contracts)


class AsyncScreenerResourceWithRawResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

    @cached_property
    def analysts(self) -> AsyncAnalystsResourceWithRawResponse:
        return AsyncAnalystsResourceWithRawResponse(self._screener.analysts)

    @cached_property
    def option_contracts(self) -> AsyncOptionContractsResourceWithRawResponse:
        return AsyncOptionContractsResourceWithRawResponse(self._screener.option_contracts)


class ScreenerResourceWithStreamingResponse:
    def __init__(self, screener: ScreenerResource) -> None:
        self._screener = screener

    @cached_property
    def analysts(self) -> AnalystsResourceWithStreamingResponse:
        return AnalystsResourceWithStreamingResponse(self._screener.analysts)

    @cached_property
    def option_contracts(self) -> OptionContractsResourceWithStreamingResponse:
        return OptionContractsResourceWithStreamingResponse(self._screener.option_contracts)


class AsyncScreenerResourceWithStreamingResponse:
    def __init__(self, screener: AsyncScreenerResource) -> None:
        self._screener = screener

    @cached_property
    def analysts(self) -> AsyncAnalystsResourceWithStreamingResponse:
        return AsyncAnalystsResourceWithStreamingResponse(self._screener.analysts)

    @cached_property
    def option_contracts(self) -> AsyncOptionContractsResourceWithStreamingResponse:
        return AsyncOptionContractsResourceWithStreamingResponse(self._screener.option_contracts)
