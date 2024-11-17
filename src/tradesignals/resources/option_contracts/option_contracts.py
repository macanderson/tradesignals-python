# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .flow_data import (
    FlowDataResource,
    AsyncFlowDataResource,
    FlowDataResourceWithRawResponse,
    AsyncFlowDataResourceWithRawResponse,
    FlowDataResourceWithStreamingResponse,
    AsyncFlowDataResourceWithStreamingResponse,
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
from .expiry_breakdown import (
    ExpiryBreakdownResource,
    AsyncExpiryBreakdownResource,
    ExpiryBreakdownResourceWithRawResponse,
    AsyncExpiryBreakdownResourceWithRawResponse,
    ExpiryBreakdownResourceWithStreamingResponse,
    AsyncExpiryBreakdownResourceWithStreamingResponse,
)
from .underlying_chains import (
    UnderlyingChainsResource,
    AsyncUnderlyingChainsResource,
    UnderlyingChainsResourceWithRawResponse,
    AsyncUnderlyingChainsResourceWithRawResponse,
    UnderlyingChainsResourceWithStreamingResponse,
    AsyncUnderlyingChainsResourceWithStreamingResponse,
)

__all__ = ["OptionContractsResource", "AsyncOptionContractsResource"]


class OptionContractsResource(SyncAPIResource):
    @cached_property
    def underlying_chains(self) -> UnderlyingChainsResource:
        return UnderlyingChainsResource(self._client)

    @cached_property
    def flow_data(self) -> FlowDataResource:
        return FlowDataResource(self._client)

    @cached_property
    def historic_data(self) -> HistoricDataResource:
        return HistoricDataResource(self._client)

    @cached_property
    def expiry_breakdown(self) -> ExpiryBreakdownResource:
        return ExpiryBreakdownResource(self._client)

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
    def underlying_chains(self) -> AsyncUnderlyingChainsResource:
        return AsyncUnderlyingChainsResource(self._client)

    @cached_property
    def flow_data(self) -> AsyncFlowDataResource:
        return AsyncFlowDataResource(self._client)

    @cached_property
    def historic_data(self) -> AsyncHistoricDataResource:
        return AsyncHistoricDataResource(self._client)

    @cached_property
    def expiry_breakdown(self) -> AsyncExpiryBreakdownResource:
        return AsyncExpiryBreakdownResource(self._client)

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
    def underlying_chains(self) -> UnderlyingChainsResourceWithRawResponse:
        return UnderlyingChainsResourceWithRawResponse(self._option_contracts.underlying_chains)

    @cached_property
    def flow_data(self) -> FlowDataResourceWithRawResponse:
        return FlowDataResourceWithRawResponse(self._option_contracts.flow_data)

    @cached_property
    def historic_data(self) -> HistoricDataResourceWithRawResponse:
        return HistoricDataResourceWithRawResponse(self._option_contracts.historic_data)

    @cached_property
    def expiry_breakdown(self) -> ExpiryBreakdownResourceWithRawResponse:
        return ExpiryBreakdownResourceWithRawResponse(self._option_contracts.expiry_breakdown)


class AsyncOptionContractsResourceWithRawResponse:
    def __init__(self, option_contracts: AsyncOptionContractsResource) -> None:
        self._option_contracts = option_contracts

    @cached_property
    def underlying_chains(self) -> AsyncUnderlyingChainsResourceWithRawResponse:
        return AsyncUnderlyingChainsResourceWithRawResponse(self._option_contracts.underlying_chains)

    @cached_property
    def flow_data(self) -> AsyncFlowDataResourceWithRawResponse:
        return AsyncFlowDataResourceWithRawResponse(self._option_contracts.flow_data)

    @cached_property
    def historic_data(self) -> AsyncHistoricDataResourceWithRawResponse:
        return AsyncHistoricDataResourceWithRawResponse(self._option_contracts.historic_data)

    @cached_property
    def expiry_breakdown(self) -> AsyncExpiryBreakdownResourceWithRawResponse:
        return AsyncExpiryBreakdownResourceWithRawResponse(self._option_contracts.expiry_breakdown)


class OptionContractsResourceWithStreamingResponse:
    def __init__(self, option_contracts: OptionContractsResource) -> None:
        self._option_contracts = option_contracts

    @cached_property
    def underlying_chains(self) -> UnderlyingChainsResourceWithStreamingResponse:
        return UnderlyingChainsResourceWithStreamingResponse(self._option_contracts.underlying_chains)

    @cached_property
    def flow_data(self) -> FlowDataResourceWithStreamingResponse:
        return FlowDataResourceWithStreamingResponse(self._option_contracts.flow_data)

    @cached_property
    def historic_data(self) -> HistoricDataResourceWithStreamingResponse:
        return HistoricDataResourceWithStreamingResponse(self._option_contracts.historic_data)

    @cached_property
    def expiry_breakdown(self) -> ExpiryBreakdownResourceWithStreamingResponse:
        return ExpiryBreakdownResourceWithStreamingResponse(self._option_contracts.expiry_breakdown)


class AsyncOptionContractsResourceWithStreamingResponse:
    def __init__(self, option_contracts: AsyncOptionContractsResource) -> None:
        self._option_contracts = option_contracts

    @cached_property
    def underlying_chains(self) -> AsyncUnderlyingChainsResourceWithStreamingResponse:
        return AsyncUnderlyingChainsResourceWithStreamingResponse(self._option_contracts.underlying_chains)

    @cached_property
    def flow_data(self) -> AsyncFlowDataResourceWithStreamingResponse:
        return AsyncFlowDataResourceWithStreamingResponse(self._option_contracts.flow_data)

    @cached_property
    def historic_data(self) -> AsyncHistoricDataResourceWithStreamingResponse:
        return AsyncHistoricDataResourceWithStreamingResponse(self._option_contracts.historic_data)

    @cached_property
    def expiry_breakdown(self) -> AsyncExpiryBreakdownResourceWithStreamingResponse:
        return AsyncExpiryBreakdownResourceWithStreamingResponse(self._option_contracts.expiry_breakdown)
