# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .atm_chains import (
    AtmChainsResource,
    AsyncAtmChainsResource,
    AtmChainsResourceWithRawResponse,
    AsyncAtmChainsResourceWithRawResponse,
    AtmChainsResourceWithStreamingResponse,
    AsyncAtmChainsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .option_alerts import (
    OptionAlertsResource,
    AsyncOptionAlertsResource,
    OptionAlertsResourceWithRawResponse,
    AsyncOptionAlertsResourceWithRawResponse,
    OptionAlertsResourceWithStreamingResponse,
    AsyncOptionAlertsResourceWithStreamingResponse,
)
from .sector_tickers import (
    SectorTickersResource,
    AsyncSectorTickersResource,
    SectorTickersResourceWithRawResponse,
    AsyncSectorTickersResourceWithRawResponse,
    SectorTickersResourceWithStreamingResponse,
    AsyncSectorTickersResourceWithStreamingResponse,
)
from .flow_per_expiry import (
    FlowPerExpiryResource,
    AsyncFlowPerExpiryResource,
    FlowPerExpiryResourceWithRawResponse,
    AsyncFlowPerExpiryResourceWithRawResponse,
    FlowPerExpiryResourceWithStreamingResponse,
    AsyncFlowPerExpiryResourceWithStreamingResponse,
)

__all__ = ["StockResource", "AsyncStockResource"]


class StockResource(SyncAPIResource):
    @cached_property
    def flow_per_expiry(self) -> FlowPerExpiryResource:
        return FlowPerExpiryResource(self._client)

    @cached_property
    def option_alerts(self) -> OptionAlertsResource:
        return OptionAlertsResource(self._client)

    @cached_property
    def sector_tickers(self) -> SectorTickersResource:
        return SectorTickersResource(self._client)

    @cached_property
    def atm_chains(self) -> AtmChainsResource:
        return AtmChainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> StockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return StockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return StockResourceWithStreamingResponse(self)


class AsyncStockResource(AsyncAPIResource):
    @cached_property
    def flow_per_expiry(self) -> AsyncFlowPerExpiryResource:
        return AsyncFlowPerExpiryResource(self._client)

    @cached_property
    def option_alerts(self) -> AsyncOptionAlertsResource:
        return AsyncOptionAlertsResource(self._client)

    @cached_property
    def sector_tickers(self) -> AsyncSectorTickersResource:
        return AsyncSectorTickersResource(self._client)

    @cached_property
    def atm_chains(self) -> AsyncAtmChainsResource:
        return AsyncAtmChainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncStockResourceWithStreamingResponse(self)


class StockResourceWithRawResponse:
    def __init__(self, stock: StockResource) -> None:
        self._stock = stock

    @cached_property
    def flow_per_expiry(self) -> FlowPerExpiryResourceWithRawResponse:
        return FlowPerExpiryResourceWithRawResponse(self._stock.flow_per_expiry)

    @cached_property
    def option_alerts(self) -> OptionAlertsResourceWithRawResponse:
        return OptionAlertsResourceWithRawResponse(self._stock.option_alerts)

    @cached_property
    def sector_tickers(self) -> SectorTickersResourceWithRawResponse:
        return SectorTickersResourceWithRawResponse(self._stock.sector_tickers)

    @cached_property
    def atm_chains(self) -> AtmChainsResourceWithRawResponse:
        return AtmChainsResourceWithRawResponse(self._stock.atm_chains)


class AsyncStockResourceWithRawResponse:
    def __init__(self, stock: AsyncStockResource) -> None:
        self._stock = stock

    @cached_property
    def flow_per_expiry(self) -> AsyncFlowPerExpiryResourceWithRawResponse:
        return AsyncFlowPerExpiryResourceWithRawResponse(self._stock.flow_per_expiry)

    @cached_property
    def option_alerts(self) -> AsyncOptionAlertsResourceWithRawResponse:
        return AsyncOptionAlertsResourceWithRawResponse(self._stock.option_alerts)

    @cached_property
    def sector_tickers(self) -> AsyncSectorTickersResourceWithRawResponse:
        return AsyncSectorTickersResourceWithRawResponse(self._stock.sector_tickers)

    @cached_property
    def atm_chains(self) -> AsyncAtmChainsResourceWithRawResponse:
        return AsyncAtmChainsResourceWithRawResponse(self._stock.atm_chains)


class StockResourceWithStreamingResponse:
    def __init__(self, stock: StockResource) -> None:
        self._stock = stock

    @cached_property
    def flow_per_expiry(self) -> FlowPerExpiryResourceWithStreamingResponse:
        return FlowPerExpiryResourceWithStreamingResponse(self._stock.flow_per_expiry)

    @cached_property
    def option_alerts(self) -> OptionAlertsResourceWithStreamingResponse:
        return OptionAlertsResourceWithStreamingResponse(self._stock.option_alerts)

    @cached_property
    def sector_tickers(self) -> SectorTickersResourceWithStreamingResponse:
        return SectorTickersResourceWithStreamingResponse(self._stock.sector_tickers)

    @cached_property
    def atm_chains(self) -> AtmChainsResourceWithStreamingResponse:
        return AtmChainsResourceWithStreamingResponse(self._stock.atm_chains)


class AsyncStockResourceWithStreamingResponse:
    def __init__(self, stock: AsyncStockResource) -> None:
        self._stock = stock

    @cached_property
    def flow_per_expiry(self) -> AsyncFlowPerExpiryResourceWithStreamingResponse:
        return AsyncFlowPerExpiryResourceWithStreamingResponse(self._stock.flow_per_expiry)

    @cached_property
    def option_alerts(self) -> AsyncOptionAlertsResourceWithStreamingResponse:
        return AsyncOptionAlertsResourceWithStreamingResponse(self._stock.option_alerts)

    @cached_property
    def sector_tickers(self) -> AsyncSectorTickersResourceWithStreamingResponse:
        return AsyncSectorTickersResourceWithStreamingResponse(self._stock.sector_tickers)

    @cached_property
    def atm_chains(self) -> AsyncAtmChainsResourceWithStreamingResponse:
        return AsyncAtmChainsResourceWithStreamingResponse(self._stock.atm_chains)
