# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .premarket_earnings import (
    PremarketEarningsResource,
    AsyncPremarketEarningsResource,
    PremarketEarningsResourceWithRawResponse,
    AsyncPremarketEarningsResourceWithRawResponse,
    PremarketEarningsResourceWithStreamingResponse,
    AsyncPremarketEarningsResourceWithStreamingResponse,
)
from .afterhours_earnings import (
    AfterhoursEarningsResource,
    AsyncAfterhoursEarningsResource,
    AfterhoursEarningsResourceWithRawResponse,
    AsyncAfterhoursEarningsResourceWithRawResponse,
    AfterhoursEarningsResourceWithStreamingResponse,
    AsyncAfterhoursEarningsResourceWithStreamingResponse,
)
from .historical_earnings import (
    HistoricalEarningsResource,
    AsyncHistoricalEarningsResource,
    HistoricalEarningsResourceWithRawResponse,
    AsyncHistoricalEarningsResourceWithRawResponse,
    HistoricalEarningsResourceWithStreamingResponse,
    AsyncHistoricalEarningsResourceWithStreamingResponse,
)

__all__ = ["EarningsResource", "AsyncEarningsResource"]


class EarningsResource(SyncAPIResource):
    """
    -> Earnings endpoints provides historical data for equity earnings, as well as upcoming earnings for both afterhours and premarket earnings reports.
    """

    @cached_property
    def afterhours_earnings(self) -> AfterhoursEarningsResource:
        return AfterhoursEarningsResource(self._client)

    @cached_property
    def premarket_earnings(self) -> PremarketEarningsResource:
        return PremarketEarningsResource(self._client)

    @cached_property
    def historical_earnings(self) -> HistoricalEarningsResource:
        return HistoricalEarningsResource(self._client)

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
    """
    -> Earnings endpoints provides historical data for equity earnings, as well as upcoming earnings for both afterhours and premarket earnings reports.
    """

    @cached_property
    def afterhours_earnings(self) -> AsyncAfterhoursEarningsResource:
        return AsyncAfterhoursEarningsResource(self._client)

    @cached_property
    def premarket_earnings(self) -> AsyncPremarketEarningsResource:
        return AsyncPremarketEarningsResource(self._client)

    @cached_property
    def historical_earnings(self) -> AsyncHistoricalEarningsResource:
        return AsyncHistoricalEarningsResource(self._client)

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
    def afterhours_earnings(self) -> AfterhoursEarningsResourceWithRawResponse:
        return AfterhoursEarningsResourceWithRawResponse(self._earnings.afterhours_earnings)

    @cached_property
    def premarket_earnings(self) -> PremarketEarningsResourceWithRawResponse:
        return PremarketEarningsResourceWithRawResponse(self._earnings.premarket_earnings)

    @cached_property
    def historical_earnings(self) -> HistoricalEarningsResourceWithRawResponse:
        return HistoricalEarningsResourceWithRawResponse(self._earnings.historical_earnings)


class AsyncEarningsResourceWithRawResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

    @cached_property
    def afterhours_earnings(self) -> AsyncAfterhoursEarningsResourceWithRawResponse:
        return AsyncAfterhoursEarningsResourceWithRawResponse(self._earnings.afterhours_earnings)

    @cached_property
    def premarket_earnings(self) -> AsyncPremarketEarningsResourceWithRawResponse:
        return AsyncPremarketEarningsResourceWithRawResponse(self._earnings.premarket_earnings)

    @cached_property
    def historical_earnings(self) -> AsyncHistoricalEarningsResourceWithRawResponse:
        return AsyncHistoricalEarningsResourceWithRawResponse(self._earnings.historical_earnings)


class EarningsResourceWithStreamingResponse:
    def __init__(self, earnings: EarningsResource) -> None:
        self._earnings = earnings

    @cached_property
    def afterhours_earnings(self) -> AfterhoursEarningsResourceWithStreamingResponse:
        return AfterhoursEarningsResourceWithStreamingResponse(self._earnings.afterhours_earnings)

    @cached_property
    def premarket_earnings(self) -> PremarketEarningsResourceWithStreamingResponse:
        return PremarketEarningsResourceWithStreamingResponse(self._earnings.premarket_earnings)

    @cached_property
    def historical_earnings(self) -> HistoricalEarningsResourceWithStreamingResponse:
        return HistoricalEarningsResourceWithStreamingResponse(self._earnings.historical_earnings)


class AsyncEarningsResourceWithStreamingResponse:
    def __init__(self, earnings: AsyncEarningsResource) -> None:
        self._earnings = earnings

    @cached_property
    def afterhours_earnings(self) -> AsyncAfterhoursEarningsResourceWithStreamingResponse:
        return AsyncAfterhoursEarningsResourceWithStreamingResponse(self._earnings.afterhours_earnings)

    @cached_property
    def premarket_earnings(self) -> AsyncPremarketEarningsResourceWithStreamingResponse:
        return AsyncPremarketEarningsResourceWithStreamingResponse(self._earnings.premarket_earnings)

    @cached_property
    def historical_earnings(self) -> AsyncHistoricalEarningsResourceWithStreamingResponse:
        return AsyncHistoricalEarningsResourceWithStreamingResponse(self._earnings.historical_earnings)
