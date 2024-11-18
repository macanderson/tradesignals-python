# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .order_flow import (
    OrderFlowResource,
    AsyncOrderFlowResource,
    OrderFlowResourceWithRawResponse,
    AsyncOrderFlowResourceWithRawResponse,
    OrderFlowResourceWithStreamingResponse,
    AsyncOrderFlowResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .historic_data import (
    HistoricDataResource,
    AsyncHistoricDataResource,
    HistoricDataResourceWithRawResponse,
    AsyncHistoricDataResourceWithRawResponse,
    HistoricDataResourceWithStreamingResponse,
    AsyncHistoricDataResourceWithStreamingResponse,
)
from .option_expiration_data import (
    OptionExpirationDataResource,
    AsyncOptionExpirationDataResource,
    OptionExpirationDataResourceWithRawResponse,
    AsyncOptionExpirationDataResourceWithRawResponse,
    OptionExpirationDataResourceWithStreamingResponse,
    AsyncOptionExpirationDataResourceWithStreamingResponse,
)
from .ticker_option_contracts import (
    TickerOptionContractsResource,
    AsyncTickerOptionContractsResource,
    TickerOptionContractsResourceWithRawResponse,
    AsyncTickerOptionContractsResourceWithRawResponse,
    TickerOptionContractsResourceWithStreamingResponse,
    AsyncTickerOptionContractsResourceWithStreamingResponse,
)

__all__ = ["OptionContractsResource", "AsyncOptionContractsResource"]


class OptionContractsResource(SyncAPIResource):
    @cached_property
    def ticker_option_contracts(self) -> TickerOptionContractsResource:
        return TickerOptionContractsResource(self._client)

    @cached_property
    def order_flow(self) -> OrderFlowResource:
        return OrderFlowResource(self._client)

    @cached_property
    def historic_data(self) -> HistoricDataResource:
        return HistoricDataResource(self._client)

    @cached_property
    def option_expiration_data(self) -> OptionExpirationDataResource:
        return OptionExpirationDataResource(self._client)

    @cached_property
    def with_raw_response(self) -> OptionContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OptionContractsResourceWithStreamingResponse(self)


class AsyncOptionContractsResource(AsyncAPIResource):
    @cached_property
    def ticker_option_contracts(self) -> AsyncTickerOptionContractsResource:
        return AsyncTickerOptionContractsResource(self._client)

    @cached_property
    def order_flow(self) -> AsyncOrderFlowResource:
        return AsyncOrderFlowResource(self._client)

    @cached_property
    def historic_data(self) -> AsyncHistoricDataResource:
        return AsyncHistoricDataResource(self._client)

    @cached_property
    def option_expiration_data(self) -> AsyncOptionExpirationDataResource:
        return AsyncOptionExpirationDataResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOptionContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOptionContractsResourceWithStreamingResponse(self)


class OptionContractsResourceWithRawResponse:
    def __init__(self, option_contracts: OptionContractsResource) -> None:
        self._option_contracts = option_contracts

    @cached_property
    def ticker_option_contracts(self) -> TickerOptionContractsResourceWithRawResponse:
        return TickerOptionContractsResourceWithRawResponse(self._option_contracts.ticker_option_contracts)

    @cached_property
    def order_flow(self) -> OrderFlowResourceWithRawResponse:
        return OrderFlowResourceWithRawResponse(self._option_contracts.order_flow)

    @cached_property
    def historic_data(self) -> HistoricDataResourceWithRawResponse:
        return HistoricDataResourceWithRawResponse(self._option_contracts.historic_data)

    @cached_property
    def option_expiration_data(self) -> OptionExpirationDataResourceWithRawResponse:
        return OptionExpirationDataResourceWithRawResponse(self._option_contracts.option_expiration_data)


class AsyncOptionContractsResourceWithRawResponse:
    def __init__(self, option_contracts: AsyncOptionContractsResource) -> None:
        self._option_contracts = option_contracts

    @cached_property
    def ticker_option_contracts(self) -> AsyncTickerOptionContractsResourceWithRawResponse:
        return AsyncTickerOptionContractsResourceWithRawResponse(self._option_contracts.ticker_option_contracts)

    @cached_property
    def order_flow(self) -> AsyncOrderFlowResourceWithRawResponse:
        return AsyncOrderFlowResourceWithRawResponse(self._option_contracts.order_flow)

    @cached_property
    def historic_data(self) -> AsyncHistoricDataResourceWithRawResponse:
        return AsyncHistoricDataResourceWithRawResponse(self._option_contracts.historic_data)

    @cached_property
    def option_expiration_data(self) -> AsyncOptionExpirationDataResourceWithRawResponse:
        return AsyncOptionExpirationDataResourceWithRawResponse(self._option_contracts.option_expiration_data)


class OptionContractsResourceWithStreamingResponse:
    def __init__(self, option_contracts: OptionContractsResource) -> None:
        self._option_contracts = option_contracts

    @cached_property
    def ticker_option_contracts(self) -> TickerOptionContractsResourceWithStreamingResponse:
        return TickerOptionContractsResourceWithStreamingResponse(self._option_contracts.ticker_option_contracts)

    @cached_property
    def order_flow(self) -> OrderFlowResourceWithStreamingResponse:
        return OrderFlowResourceWithStreamingResponse(self._option_contracts.order_flow)

    @cached_property
    def historic_data(self) -> HistoricDataResourceWithStreamingResponse:
        return HistoricDataResourceWithStreamingResponse(self._option_contracts.historic_data)

    @cached_property
    def option_expiration_data(self) -> OptionExpirationDataResourceWithStreamingResponse:
        return OptionExpirationDataResourceWithStreamingResponse(self._option_contracts.option_expiration_data)


class AsyncOptionContractsResourceWithStreamingResponse:
    def __init__(self, option_contracts: AsyncOptionContractsResource) -> None:
        self._option_contracts = option_contracts

    @cached_property
    def ticker_option_contracts(self) -> AsyncTickerOptionContractsResourceWithStreamingResponse:
        return AsyncTickerOptionContractsResourceWithStreamingResponse(self._option_contracts.ticker_option_contracts)

    @cached_property
    def order_flow(self) -> AsyncOrderFlowResourceWithStreamingResponse:
        return AsyncOrderFlowResourceWithStreamingResponse(self._option_contracts.order_flow)

    @cached_property
    def historic_data(self) -> AsyncHistoricDataResourceWithStreamingResponse:
        return AsyncHistoricDataResourceWithStreamingResponse(self._option_contracts.historic_data)

    @cached_property
    def option_expiration_data(self) -> AsyncOptionExpirationDataResourceWithStreamingResponse:
        return AsyncOptionExpirationDataResourceWithStreamingResponse(self._option_contracts.option_expiration_data)
