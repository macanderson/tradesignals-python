# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .weights import (
    WeightsResource,
    AsyncWeightsResource,
    WeightsResourceWithRawResponse,
    AsyncWeightsResourceWithRawResponse,
    WeightsResourceWithStreamingResponse,
    AsyncWeightsResourceWithStreamingResponse,
)
from .exposure import (
    ExposureResource,
    AsyncExposureResource,
    ExposureResourceWithRawResponse,
    AsyncExposureResourceWithRawResponse,
    ExposureResourceWithStreamingResponse,
    AsyncExposureResourceWithStreamingResponse,
)
from .holdings import (
    HoldingsResource,
    AsyncHoldingsResource,
    HoldingsResourceWithRawResponse,
    AsyncHoldingsResourceWithRawResponse,
    HoldingsResourceWithStreamingResponse,
    AsyncHoldingsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .information import (
    InformationResource,
    AsyncInformationResource,
    InformationResourceWithRawResponse,
    AsyncInformationResourceWithRawResponse,
    InformationResourceWithStreamingResponse,
    AsyncInformationResourceWithStreamingResponse,
)
from .inflows_outflows import (
    InflowsOutflowsResource,
    AsyncInflowsOutflowsResource,
    InflowsOutflowsResourceWithRawResponse,
    AsyncInflowsOutflowsResourceWithRawResponse,
    InflowsOutflowsResourceWithStreamingResponse,
    AsyncInflowsOutflowsResourceWithStreamingResponse,
)

__all__ = ["EtfResource", "AsyncEtfResource"]


class EtfResource(SyncAPIResource):
    @cached_property
    def holdings(self) -> HoldingsResource:
        return HoldingsResource(self._client)

    @cached_property
    def inflows_outflows(self) -> InflowsOutflowsResource:
        return InflowsOutflowsResource(self._client)

    @cached_property
    def information(self) -> InformationResource:
        return InformationResource(self._client)

    @cached_property
    def exposure(self) -> ExposureResource:
        return ExposureResource(self._client)

    @cached_property
    def weights(self) -> WeightsResource:
        return WeightsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EtfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return EtfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EtfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return EtfResourceWithStreamingResponse(self)


class AsyncEtfResource(AsyncAPIResource):
    @cached_property
    def holdings(self) -> AsyncHoldingsResource:
        return AsyncHoldingsResource(self._client)

    @cached_property
    def inflows_outflows(self) -> AsyncInflowsOutflowsResource:
        return AsyncInflowsOutflowsResource(self._client)

    @cached_property
    def information(self) -> AsyncInformationResource:
        return AsyncInformationResource(self._client)

    @cached_property
    def exposure(self) -> AsyncExposureResource:
        return AsyncExposureResource(self._client)

    @cached_property
    def weights(self) -> AsyncWeightsResource:
        return AsyncWeightsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEtfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEtfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEtfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncEtfResourceWithStreamingResponse(self)


class EtfResourceWithRawResponse:
    def __init__(self, etf: EtfResource) -> None:
        self._etf = etf

    @cached_property
    def holdings(self) -> HoldingsResourceWithRawResponse:
        return HoldingsResourceWithRawResponse(self._etf.holdings)

    @cached_property
    def inflows_outflows(self) -> InflowsOutflowsResourceWithRawResponse:
        return InflowsOutflowsResourceWithRawResponse(self._etf.inflows_outflows)

    @cached_property
    def information(self) -> InformationResourceWithRawResponse:
        return InformationResourceWithRawResponse(self._etf.information)

    @cached_property
    def exposure(self) -> ExposureResourceWithRawResponse:
        return ExposureResourceWithRawResponse(self._etf.exposure)

    @cached_property
    def weights(self) -> WeightsResourceWithRawResponse:
        return WeightsResourceWithRawResponse(self._etf.weights)


class AsyncEtfResourceWithRawResponse:
    def __init__(self, etf: AsyncEtfResource) -> None:
        self._etf = etf

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithRawResponse:
        return AsyncHoldingsResourceWithRawResponse(self._etf.holdings)

    @cached_property
    def inflows_outflows(self) -> AsyncInflowsOutflowsResourceWithRawResponse:
        return AsyncInflowsOutflowsResourceWithRawResponse(self._etf.inflows_outflows)

    @cached_property
    def information(self) -> AsyncInformationResourceWithRawResponse:
        return AsyncInformationResourceWithRawResponse(self._etf.information)

    @cached_property
    def exposure(self) -> AsyncExposureResourceWithRawResponse:
        return AsyncExposureResourceWithRawResponse(self._etf.exposure)

    @cached_property
    def weights(self) -> AsyncWeightsResourceWithRawResponse:
        return AsyncWeightsResourceWithRawResponse(self._etf.weights)


class EtfResourceWithStreamingResponse:
    def __init__(self, etf: EtfResource) -> None:
        self._etf = etf

    @cached_property
    def holdings(self) -> HoldingsResourceWithStreamingResponse:
        return HoldingsResourceWithStreamingResponse(self._etf.holdings)

    @cached_property
    def inflows_outflows(self) -> InflowsOutflowsResourceWithStreamingResponse:
        return InflowsOutflowsResourceWithStreamingResponse(self._etf.inflows_outflows)

    @cached_property
    def information(self) -> InformationResourceWithStreamingResponse:
        return InformationResourceWithStreamingResponse(self._etf.information)

    @cached_property
    def exposure(self) -> ExposureResourceWithStreamingResponse:
        return ExposureResourceWithStreamingResponse(self._etf.exposure)

    @cached_property
    def weights(self) -> WeightsResourceWithStreamingResponse:
        return WeightsResourceWithStreamingResponse(self._etf.weights)


class AsyncEtfResourceWithStreamingResponse:
    def __init__(self, etf: AsyncEtfResource) -> None:
        self._etf = etf

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithStreamingResponse:
        return AsyncHoldingsResourceWithStreamingResponse(self._etf.holdings)

    @cached_property
    def inflows_outflows(self) -> AsyncInflowsOutflowsResourceWithStreamingResponse:
        return AsyncInflowsOutflowsResourceWithStreamingResponse(self._etf.inflows_outflows)

    @cached_property
    def information(self) -> AsyncInformationResourceWithStreamingResponse:
        return AsyncInformationResourceWithStreamingResponse(self._etf.information)

    @cached_property
    def exposure(self) -> AsyncExposureResourceWithStreamingResponse:
        return AsyncExposureResourceWithStreamingResponse(self._etf.exposure)

    @cached_property
    def weights(self) -> AsyncWeightsResourceWithStreamingResponse:
        return AsyncWeightsResourceWithStreamingResponse(self._etf.weights)
