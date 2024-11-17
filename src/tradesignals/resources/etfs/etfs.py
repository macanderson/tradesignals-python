# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .sector_country_weights import (
    SectorCountryWeightsResource,
    AsyncSectorCountryWeightsResource,
    SectorCountryWeightsResourceWithRawResponse,
    AsyncSectorCountryWeightsResourceWithRawResponse,
    SectorCountryWeightsResourceWithStreamingResponse,
    AsyncSectorCountryWeightsResourceWithStreamingResponse,
)

__all__ = ["EtfsResource", "AsyncEtfsResource"]


class EtfsResource(SyncAPIResource):
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
    def sector_country_weights(self) -> SectorCountryWeightsResource:
        return SectorCountryWeightsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EtfsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return EtfsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EtfsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return EtfsResourceWithStreamingResponse(self)


class AsyncEtfsResource(AsyncAPIResource):
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
    def sector_country_weights(self) -> AsyncSectorCountryWeightsResource:
        return AsyncSectorCountryWeightsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEtfsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEtfsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEtfsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncEtfsResourceWithStreamingResponse(self)


class EtfsResourceWithRawResponse:
    def __init__(self, etfs: EtfsResource) -> None:
        self._etfs = etfs

    @cached_property
    def holdings(self) -> HoldingsResourceWithRawResponse:
        return HoldingsResourceWithRawResponse(self._etfs.holdings)

    @cached_property
    def inflows_outflows(self) -> InflowsOutflowsResourceWithRawResponse:
        return InflowsOutflowsResourceWithRawResponse(self._etfs.inflows_outflows)

    @cached_property
    def information(self) -> InformationResourceWithRawResponse:
        return InformationResourceWithRawResponse(self._etfs.information)

    @cached_property
    def exposure(self) -> ExposureResourceWithRawResponse:
        return ExposureResourceWithRawResponse(self._etfs.exposure)

    @cached_property
    def sector_country_weights(self) -> SectorCountryWeightsResourceWithRawResponse:
        return SectorCountryWeightsResourceWithRawResponse(self._etfs.sector_country_weights)


class AsyncEtfsResourceWithRawResponse:
    def __init__(self, etfs: AsyncEtfsResource) -> None:
        self._etfs = etfs

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithRawResponse:
        return AsyncHoldingsResourceWithRawResponse(self._etfs.holdings)

    @cached_property
    def inflows_outflows(self) -> AsyncInflowsOutflowsResourceWithRawResponse:
        return AsyncInflowsOutflowsResourceWithRawResponse(self._etfs.inflows_outflows)

    @cached_property
    def information(self) -> AsyncInformationResourceWithRawResponse:
        return AsyncInformationResourceWithRawResponse(self._etfs.information)

    @cached_property
    def exposure(self) -> AsyncExposureResourceWithRawResponse:
        return AsyncExposureResourceWithRawResponse(self._etfs.exposure)

    @cached_property
    def sector_country_weights(self) -> AsyncSectorCountryWeightsResourceWithRawResponse:
        return AsyncSectorCountryWeightsResourceWithRawResponse(self._etfs.sector_country_weights)


class EtfsResourceWithStreamingResponse:
    def __init__(self, etfs: EtfsResource) -> None:
        self._etfs = etfs

    @cached_property
    def holdings(self) -> HoldingsResourceWithStreamingResponse:
        return HoldingsResourceWithStreamingResponse(self._etfs.holdings)

    @cached_property
    def inflows_outflows(self) -> InflowsOutflowsResourceWithStreamingResponse:
        return InflowsOutflowsResourceWithStreamingResponse(self._etfs.inflows_outflows)

    @cached_property
    def information(self) -> InformationResourceWithStreamingResponse:
        return InformationResourceWithStreamingResponse(self._etfs.information)

    @cached_property
    def exposure(self) -> ExposureResourceWithStreamingResponse:
        return ExposureResourceWithStreamingResponse(self._etfs.exposure)

    @cached_property
    def sector_country_weights(self) -> SectorCountryWeightsResourceWithStreamingResponse:
        return SectorCountryWeightsResourceWithStreamingResponse(self._etfs.sector_country_weights)


class AsyncEtfsResourceWithStreamingResponse:
    def __init__(self, etfs: AsyncEtfsResource) -> None:
        self._etfs = etfs

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithStreamingResponse:
        return AsyncHoldingsResourceWithStreamingResponse(self._etfs.holdings)

    @cached_property
    def inflows_outflows(self) -> AsyncInflowsOutflowsResourceWithStreamingResponse:
        return AsyncInflowsOutflowsResourceWithStreamingResponse(self._etfs.inflows_outflows)

    @cached_property
    def information(self) -> AsyncInformationResourceWithStreamingResponse:
        return AsyncInformationResourceWithStreamingResponse(self._etfs.information)

    @cached_property
    def exposure(self) -> AsyncExposureResourceWithStreamingResponse:
        return AsyncExposureResourceWithStreamingResponse(self._etfs.exposure)

    @cached_property
    def sector_country_weights(self) -> AsyncSectorCountryWeightsResourceWithStreamingResponse:
        return AsyncSectorCountryWeightsResourceWithStreamingResponse(self._etfs.sector_country_weights)
