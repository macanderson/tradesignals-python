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
from .option_chains import (
    OptionChainsResource,
    AsyncOptionChainsResource,
    OptionChainsResourceWithRawResponse,
    AsyncOptionChainsResourceWithRawResponse,
    OptionChainsResourceWithStreamingResponse,
    AsyncOptionChainsResourceWithStreamingResponse,
)
from .expiry_breakdown import (
    ExpiryBreakdownResource,
    AsyncExpiryBreakdownResource,
    ExpiryBreakdownResourceWithRawResponse,
    AsyncExpiryBreakdownResourceWithRawResponse,
    ExpiryBreakdownResourceWithStreamingResponse,
    AsyncExpiryBreakdownResourceWithStreamingResponse,
)

__all__ = ["OptionContractResource", "AsyncOptionContractResource"]


class OptionContractResource(SyncAPIResource):
    @cached_property
    def option_chains(self) -> OptionChainsResource:
        return OptionChainsResource(self._client)

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
    def with_raw_response(self) -> OptionContractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionContractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionContractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OptionContractResourceWithStreamingResponse(self)


class AsyncOptionContractResource(AsyncAPIResource):
    @cached_property
    def option_chains(self) -> AsyncOptionChainsResource:
        return AsyncOptionChainsResource(self._client)

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
    def with_raw_response(self) -> AsyncOptionContractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionContractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionContractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOptionContractResourceWithStreamingResponse(self)


class OptionContractResourceWithRawResponse:
    def __init__(self, option_contract: OptionContractResource) -> None:
        self._option_contract = option_contract

    @cached_property
    def option_chains(self) -> OptionChainsResourceWithRawResponse:
        return OptionChainsResourceWithRawResponse(self._option_contract.option_chains)

    @cached_property
    def flow_data(self) -> FlowDataResourceWithRawResponse:
        return FlowDataResourceWithRawResponse(self._option_contract.flow_data)

    @cached_property
    def historic_data(self) -> HistoricDataResourceWithRawResponse:
        return HistoricDataResourceWithRawResponse(self._option_contract.historic_data)

    @cached_property
    def expiry_breakdown(self) -> ExpiryBreakdownResourceWithRawResponse:
        return ExpiryBreakdownResourceWithRawResponse(self._option_contract.expiry_breakdown)


class AsyncOptionContractResourceWithRawResponse:
    def __init__(self, option_contract: AsyncOptionContractResource) -> None:
        self._option_contract = option_contract

    @cached_property
    def option_chains(self) -> AsyncOptionChainsResourceWithRawResponse:
        return AsyncOptionChainsResourceWithRawResponse(self._option_contract.option_chains)

    @cached_property
    def flow_data(self) -> AsyncFlowDataResourceWithRawResponse:
        return AsyncFlowDataResourceWithRawResponse(self._option_contract.flow_data)

    @cached_property
    def historic_data(self) -> AsyncHistoricDataResourceWithRawResponse:
        return AsyncHistoricDataResourceWithRawResponse(self._option_contract.historic_data)

    @cached_property
    def expiry_breakdown(self) -> AsyncExpiryBreakdownResourceWithRawResponse:
        return AsyncExpiryBreakdownResourceWithRawResponse(self._option_contract.expiry_breakdown)


class OptionContractResourceWithStreamingResponse:
    def __init__(self, option_contract: OptionContractResource) -> None:
        self._option_contract = option_contract

    @cached_property
    def option_chains(self) -> OptionChainsResourceWithStreamingResponse:
        return OptionChainsResourceWithStreamingResponse(self._option_contract.option_chains)

    @cached_property
    def flow_data(self) -> FlowDataResourceWithStreamingResponse:
        return FlowDataResourceWithStreamingResponse(self._option_contract.flow_data)

    @cached_property
    def historic_data(self) -> HistoricDataResourceWithStreamingResponse:
        return HistoricDataResourceWithStreamingResponse(self._option_contract.historic_data)

    @cached_property
    def expiry_breakdown(self) -> ExpiryBreakdownResourceWithStreamingResponse:
        return ExpiryBreakdownResourceWithStreamingResponse(self._option_contract.expiry_breakdown)


class AsyncOptionContractResourceWithStreamingResponse:
    def __init__(self, option_contract: AsyncOptionContractResource) -> None:
        self._option_contract = option_contract

    @cached_property
    def option_chains(self) -> AsyncOptionChainsResourceWithStreamingResponse:
        return AsyncOptionChainsResourceWithStreamingResponse(self._option_contract.option_chains)

    @cached_property
    def flow_data(self) -> AsyncFlowDataResourceWithStreamingResponse:
        return AsyncFlowDataResourceWithStreamingResponse(self._option_contract.flow_data)

    @cached_property
    def historic_data(self) -> AsyncHistoricDataResourceWithStreamingResponse:
        return AsyncHistoricDataResourceWithStreamingResponse(self._option_contract.historic_data)

    @cached_property
    def expiry_breakdown(self) -> AsyncExpiryBreakdownResourceWithStreamingResponse:
        return AsyncExpiryBreakdownResourceWithStreamingResponse(self._option_contract.expiry_breakdown)
