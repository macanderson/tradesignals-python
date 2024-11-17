# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .premarket import (
    PremarketResource,
    AsyncPremarketResource,
    PremarketResourceWithRawResponse,
    AsyncPremarketResourceWithRawResponse,
    PremarketResourceWithStreamingResponse,
    AsyncPremarketResourceWithStreamingResponse,
)
from .afterhours import (
    AfterhoursResource,
    AsyncAfterhoursResource,
    AfterhoursResourceWithRawResponse,
    AsyncAfterhoursResourceWithRawResponse,
    AfterhoursResourceWithStreamingResponse,
    AsyncAfterhoursResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .past_ticker import (
    PastTickerResource,
    AsyncPastTickerResource,
    PastTickerResourceWithRawResponse,
    AsyncPastTickerResourceWithRawResponse,
    PastTickerResourceWithStreamingResponse,
    AsyncPastTickerResourceWithStreamingResponse,
)

__all__ = ["EarningsResource", "AsyncEarningsResource"]


class EarningsResource(SyncAPIResource):
    @cached_property
    def afterhours(self) -> AfterhoursResource:
        return AfterhoursResource(self._client)

    @cached_property
    def premarket(self) -> PremarketResource:
        return PremarketResource(self._client)

    @cached_property
    def past_ticker(self) -> PastTickerResource:
        return PastTickerResource(self._client)

    @cached_property
    def with_raw_response(self) -> EarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return EarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return EarningsResourceWithStreamingResponse(self)


class AsyncEarningsResource(AsyncAPIResource):
    @cached_property
    def afterhours(self) -> AsyncAfterhoursResource:
        return AsyncAfterhoursResource(self._client)

    @cached_property
    def premarket(self) -> AsyncPremarketResource:
        return AsyncPremarketResource(self._client)

    @cached_property
    def past_ticker(self) -> AsyncPastTickerResource:
        return AsyncPastTickerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEarningsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEarningsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEarningsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncEarningsResourceWithStreamingResponse(self)


class EarningsResourceWithRawResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

    @cached_property
    def afterhours(self) -> AfterhoursResourceWithRawResponse:
        return AfterhoursResourceWithRawResponse(self._earnings.afterhours)

    @cached_property
    def premarket(self) -> PremarketResourceWithRawResponse:
        return PremarketResourceWithRawResponse(self._earnings.premarket)

    @cached_property
    def past_ticker(self) -> PastTickerResourceWithRawResponse:
        return PastTickerResourceWithRawResponse(self._earnings.past_ticker)


class AsyncEarningsResourceWithRawResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

    @cached_property
    def afterhours(self) -> AsyncAfterhoursResourceWithRawResponse:
        return AsyncAfterhoursResourceWithRawResponse(self._earnings.afterhours)

    @cached_property
    def premarket(self) -> AsyncPremarketResourceWithRawResponse:
        return AsyncPremarketResourceWithRawResponse(self._earnings.premarket)

    @cached_property
    def past_ticker(self) -> AsyncPastTickerResourceWithRawResponse:
        return AsyncPastTickerResourceWithRawResponse(self._earnings.past_ticker)


class EarningsResourceWithStreamingResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

    @cached_property
    def afterhours(self) -> AfterhoursResourceWithStreamingResponse:
        return AfterhoursResourceWithStreamingResponse(self._earnings.afterhours)

    @cached_property
    def premarket(self) -> PremarketResourceWithStreamingResponse:
        return PremarketResourceWithStreamingResponse(self._earnings.premarket)

    @cached_property
    def past_ticker(self) -> PastTickerResourceWithStreamingResponse:
        return PastTickerResourceWithStreamingResponse(self._earnings.past_ticker)


class AsyncEarningsResourceWithStreamingResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

    @cached_property
    def afterhours(self) -> AsyncAfterhoursResourceWithStreamingResponse:
        return AsyncAfterhoursResourceWithStreamingResponse(self._earnings.afterhours)

    @cached_property
    def premarket(self) -> AsyncPremarketResourceWithStreamingResponse:
        return AsyncPremarketResourceWithStreamingResponse(self._earnings.premarket)

    @cached_property
    def past_ticker(self) -> AsyncPastTickerResourceWithStreamingResponse:
        return AsyncPastTickerResourceWithStreamingResponse(self._earnings.past_ticker)
