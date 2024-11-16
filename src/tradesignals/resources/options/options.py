# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .chain import (
    ChainResource,
    AsyncChainResource,
    ChainResourceWithRawResponse,
    AsyncChainResourceWithRawResponse,
    ChainResourceWithStreamingResponse,
    AsyncChainResourceWithStreamingResponse,
)
from .greeks import (
    GreeksResource,
    AsyncGreeksResource,
    GreeksResourceWithRawResponse,
    AsyncGreeksResourceWithRawResponse,
    GreeksResourceWithStreamingResponse,
    AsyncGreeksResourceWithStreamingResponse,
)
from .contract import (
    ContractResource,
    AsyncContractResource,
    ContractResourceWithRawResponse,
    AsyncContractResourceWithRawResponse,
    ContractResourceWithStreamingResponse,
    AsyncContractResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .contracts import (
    ContractsResource,
    AsyncContractsResource,
    ContractsResourceWithRawResponse,
    AsyncContractsResourceWithRawResponse,
    ContractsResourceWithStreamingResponse,
    AsyncContractsResourceWithStreamingResponse,
)
from .historical import (
    HistoricalResource,
    AsyncHistoricalResource,
    HistoricalResourceWithRawResponse,
    AsyncHistoricalResourceWithRawResponse,
    HistoricalResourceWithStreamingResponse,
    AsyncHistoricalResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .expirations import (
    ExpirationsResource,
    AsyncExpirationsResource,
    ExpirationsResourceWithRawResponse,
    AsyncExpirationsResourceWithRawResponse,
    ExpirationsResourceWithStreamingResponse,
    AsyncExpirationsResourceWithStreamingResponse,
)

__all__ = ["OptionsResource", "AsyncOptionsResource"]


class OptionsResource(SyncAPIResource):
    @cached_property
    def chain(self) -> ChainResource:
        return ChainResource(self._client)

    @cached_property
    def expirations(self) -> ExpirationsResource:
        return ExpirationsResource(self._client)

    @cached_property
    def greeks(self) -> GreeksResource:
        return GreeksResource(self._client)

    @cached_property
    def historical(self) -> HistoricalResource:
        return HistoricalResource(self._client)

    @cached_property
    def contract(self) -> ContractResource:
        return ContractResource(self._client)

    @cached_property
    def contracts(self) -> ContractsResource:
        return ContractsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#with_streaming_response
        """
        return OptionsResourceWithStreamingResponse(self)


class AsyncOptionsResource(AsyncAPIResource):
    @cached_property
    def chain(self) -> AsyncChainResource:
        return AsyncChainResource(self._client)

    @cached_property
    def expirations(self) -> AsyncExpirationsResource:
        return AsyncExpirationsResource(self._client)

    @cached_property
    def greeks(self) -> AsyncGreeksResource:
        return AsyncGreeksResource(self._client)

    @cached_property
    def historical(self) -> AsyncHistoricalResource:
        return AsyncHistoricalResource(self._client)

    @cached_property
    def contract(self) -> AsyncContractResource:
        return AsyncContractResource(self._client)

    @cached_property
    def contracts(self) -> AsyncContractsResource:
        return AsyncContractsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#with_streaming_response
        """
        return AsyncOptionsResourceWithStreamingResponse(self)


class OptionsResourceWithRawResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

    @cached_property
    def chain(self) -> ChainResourceWithRawResponse:
        return ChainResourceWithRawResponse(self._options.chain)

    @cached_property
    def expirations(self) -> ExpirationsResourceWithRawResponse:
        return ExpirationsResourceWithRawResponse(self._options.expirations)

    @cached_property
    def greeks(self) -> GreeksResourceWithRawResponse:
        return GreeksResourceWithRawResponse(self._options.greeks)

    @cached_property
    def historical(self) -> HistoricalResourceWithRawResponse:
        return HistoricalResourceWithRawResponse(self._options.historical)

    @cached_property
    def contract(self) -> ContractResourceWithRawResponse:
        return ContractResourceWithRawResponse(self._options.contract)

    @cached_property
    def contracts(self) -> ContractsResourceWithRawResponse:
        return ContractsResourceWithRawResponse(self._options.contracts)


class AsyncOptionsResourceWithRawResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

    @cached_property
    def chain(self) -> AsyncChainResourceWithRawResponse:
        return AsyncChainResourceWithRawResponse(self._options.chain)

    @cached_property
    def expirations(self) -> AsyncExpirationsResourceWithRawResponse:
        return AsyncExpirationsResourceWithRawResponse(self._options.expirations)

    @cached_property
    def greeks(self) -> AsyncGreeksResourceWithRawResponse:
        return AsyncGreeksResourceWithRawResponse(self._options.greeks)

    @cached_property
    def historical(self) -> AsyncHistoricalResourceWithRawResponse:
        return AsyncHistoricalResourceWithRawResponse(self._options.historical)

    @cached_property
    def contract(self) -> AsyncContractResourceWithRawResponse:
        return AsyncContractResourceWithRawResponse(self._options.contract)

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithRawResponse:
        return AsyncContractsResourceWithRawResponse(self._options.contracts)


class OptionsResourceWithStreamingResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

    @cached_property
    def chain(self) -> ChainResourceWithStreamingResponse:
        return ChainResourceWithStreamingResponse(self._options.chain)

    @cached_property
    def expirations(self) -> ExpirationsResourceWithStreamingResponse:
        return ExpirationsResourceWithStreamingResponse(self._options.expirations)

    @cached_property
    def greeks(self) -> GreeksResourceWithStreamingResponse:
        return GreeksResourceWithStreamingResponse(self._options.greeks)

    @cached_property
    def historical(self) -> HistoricalResourceWithStreamingResponse:
        return HistoricalResourceWithStreamingResponse(self._options.historical)

    @cached_property
    def contract(self) -> ContractResourceWithStreamingResponse:
        return ContractResourceWithStreamingResponse(self._options.contract)

    @cached_property
    def contracts(self) -> ContractsResourceWithStreamingResponse:
        return ContractsResourceWithStreamingResponse(self._options.contracts)


class AsyncOptionsResourceWithStreamingResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

    @cached_property
    def chain(self) -> AsyncChainResourceWithStreamingResponse:
        return AsyncChainResourceWithStreamingResponse(self._options.chain)

    @cached_property
    def expirations(self) -> AsyncExpirationsResourceWithStreamingResponse:
        return AsyncExpirationsResourceWithStreamingResponse(self._options.expirations)

    @cached_property
    def greeks(self) -> AsyncGreeksResourceWithStreamingResponse:
        return AsyncGreeksResourceWithStreamingResponse(self._options.greeks)

    @cached_property
    def historical(self) -> AsyncHistoricalResourceWithStreamingResponse:
        return AsyncHistoricalResourceWithStreamingResponse(self._options.historical)

    @cached_property
    def contract(self) -> AsyncContractResourceWithStreamingResponse:
        return AsyncContractResourceWithStreamingResponse(self._options.contract)

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithStreamingResponse:
        return AsyncContractsResourceWithStreamingResponse(self._options.contracts)
