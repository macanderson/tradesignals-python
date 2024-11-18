# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .top_performers import (
    TopPerformersResource,
    AsyncTopPerformersResource,
    TopPerformersResourceWithRawResponse,
    AsyncTopPerformersResourceWithRawResponse,
    TopPerformersResourceWithStreamingResponse,
    AsyncTopPerformersResourceWithStreamingResponse,
)
from .market_seasonality import (
    MarketSeasonalityResource,
    AsyncMarketSeasonalityResource,
    MarketSeasonalityResourceWithRawResponse,
    AsyncMarketSeasonalityResourceWithRawResponse,
    MarketSeasonalityResourceWithStreamingResponse,
    AsyncMarketSeasonalityResourceWithStreamingResponse,
)
from .stock_price_changes import (
    StockPriceChangesResource,
    AsyncStockPriceChangesResource,
    StockPriceChangesResourceWithRawResponse,
    AsyncStockPriceChangesResourceWithRawResponse,
    StockPriceChangesResourceWithStreamingResponse,
    AsyncStockPriceChangesResourceWithStreamingResponse,
)
from .stock_average_returns import (
    StockAverageReturnsResource,
    AsyncStockAverageReturnsResource,
    StockAverageReturnsResourceWithRawResponse,
    AsyncStockAverageReturnsResourceWithRawResponse,
    StockAverageReturnsResourceWithStreamingResponse,
    AsyncStockAverageReturnsResourceWithStreamingResponse,
)

__all__ = ["SeasonalityResource", "AsyncSeasonalityResource"]


class SeasonalityResource(SyncAPIResource):
    @cached_property
    def stock_average_returns(self) -> StockAverageReturnsResource:
        return StockAverageReturnsResource(self._client)

    @cached_property
    def stock_price_changes(self) -> StockPriceChangesResource:
        return StockPriceChangesResource(self._client)

    @cached_property
    def market_seasonality(self) -> MarketSeasonalityResource:
        return MarketSeasonalityResource(self._client)

    @cached_property
    def top_performers(self) -> TopPerformersResource:
        return TopPerformersResource(self._client)

    @cached_property
    def with_raw_response(self) -> SeasonalityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return SeasonalityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeasonalityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return SeasonalityResourceWithStreamingResponse(self)


class AsyncSeasonalityResource(AsyncAPIResource):
    @cached_property
    def stock_average_returns(self) -> AsyncStockAverageReturnsResource:
        return AsyncStockAverageReturnsResource(self._client)

    @cached_property
    def stock_price_changes(self) -> AsyncStockPriceChangesResource:
        return AsyncStockPriceChangesResource(self._client)

    @cached_property
    def market_seasonality(self) -> AsyncMarketSeasonalityResource:
        return AsyncMarketSeasonalityResource(self._client)

    @cached_property
    def top_performers(self) -> AsyncTopPerformersResource:
        return AsyncTopPerformersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSeasonalityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSeasonalityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeasonalityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncSeasonalityResourceWithStreamingResponse(self)


class SeasonalityResourceWithRawResponse:
    def __init__(self, seasonality: SeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def stock_average_returns(self) -> StockAverageReturnsResourceWithRawResponse:
        return StockAverageReturnsResourceWithRawResponse(self._seasonality.stock_average_returns)

    @cached_property
    def stock_price_changes(self) -> StockPriceChangesResourceWithRawResponse:
        return StockPriceChangesResourceWithRawResponse(self._seasonality.stock_price_changes)

    @cached_property
    def market_seasonality(self) -> MarketSeasonalityResourceWithRawResponse:
        return MarketSeasonalityResourceWithRawResponse(self._seasonality.market_seasonality)

    @cached_property
    def top_performers(self) -> TopPerformersResourceWithRawResponse:
        return TopPerformersResourceWithRawResponse(self._seasonality.top_performers)


class AsyncSeasonalityResourceWithRawResponse:
    def __init__(self, seasonality: AsyncSeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def stock_average_returns(self) -> AsyncStockAverageReturnsResourceWithRawResponse:
        return AsyncStockAverageReturnsResourceWithRawResponse(self._seasonality.stock_average_returns)

    @cached_property
    def stock_price_changes(self) -> AsyncStockPriceChangesResourceWithRawResponse:
        return AsyncStockPriceChangesResourceWithRawResponse(self._seasonality.stock_price_changes)

    @cached_property
    def market_seasonality(self) -> AsyncMarketSeasonalityResourceWithRawResponse:
        return AsyncMarketSeasonalityResourceWithRawResponse(self._seasonality.market_seasonality)

    @cached_property
    def top_performers(self) -> AsyncTopPerformersResourceWithRawResponse:
        return AsyncTopPerformersResourceWithRawResponse(self._seasonality.top_performers)


class SeasonalityResourceWithStreamingResponse:
    def __init__(self, seasonality: SeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def stock_average_returns(self) -> StockAverageReturnsResourceWithStreamingResponse:
        return StockAverageReturnsResourceWithStreamingResponse(self._seasonality.stock_average_returns)

    @cached_property
    def stock_price_changes(self) -> StockPriceChangesResourceWithStreamingResponse:
        return StockPriceChangesResourceWithStreamingResponse(self._seasonality.stock_price_changes)

    @cached_property
    def market_seasonality(self) -> MarketSeasonalityResourceWithStreamingResponse:
        return MarketSeasonalityResourceWithStreamingResponse(self._seasonality.market_seasonality)

    @cached_property
    def top_performers(self) -> TopPerformersResourceWithStreamingResponse:
        return TopPerformersResourceWithStreamingResponse(self._seasonality.top_performers)


class AsyncSeasonalityResourceWithStreamingResponse:
    def __init__(self, seasonality: AsyncSeasonalityResource) -> None:
        self._seasonality = seasonality

    @cached_property
    def stock_average_returns(self) -> AsyncStockAverageReturnsResourceWithStreamingResponse:
        return AsyncStockAverageReturnsResourceWithStreamingResponse(self._seasonality.stock_average_returns)

    @cached_property
    def stock_price_changes(self) -> AsyncStockPriceChangesResourceWithStreamingResponse:
        return AsyncStockPriceChangesResourceWithStreamingResponse(self._seasonality.stock_price_changes)

    @cached_property
    def market_seasonality(self) -> AsyncMarketSeasonalityResourceWithStreamingResponse:
        return AsyncMarketSeasonalityResourceWithStreamingResponse(self._seasonality.market_seasonality)

    @cached_property
    def top_performers(self) -> AsyncTopPerformersResourceWithStreamingResponse:
        return AsyncTopPerformersResourceWithStreamingResponse(self._seasonality.top_performers)
