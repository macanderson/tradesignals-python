# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .info import (
    InfoResource,
    AsyncInfoResource,
    InfoResourceWithRawResponse,
    AsyncInfoResourceWithRawResponse,
    InfoResourceWithStreamingResponse,
    AsyncInfoResourceWithStreamingResponse,
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
from .inflow_outflow import (
    InflowOutflowResource,
    AsyncInflowOutflowResource,
    InflowOutflowResourceWithRawResponse,
    AsyncInflowOutflowResourceWithRawResponse,
    InflowOutflowResourceWithStreamingResponse,
    AsyncInflowOutflowResourceWithStreamingResponse,
)

__all__ = ["EtfResource", "AsyncEtfResource"]


class EtfResource(SyncAPIResource):
    @cached_property
    def holdings(self) -> HoldingsResource:
        return HoldingsResource(self._client)

    @cached_property
    def inflow_outflow(self) -> InflowOutflowResource:
        return InflowOutflowResource(self._client)

    @cached_property
    def info(self) -> InfoResource:
        return InfoResource(self._client)

    @cached_property
    def exposure(self) -> ExposureResource:
        return ExposureResource(self._client)

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
    def inflow_outflow(self) -> AsyncInflowOutflowResource:
        return AsyncInflowOutflowResource(self._client)

    @cached_property
    def info(self) -> AsyncInfoResource:
        return AsyncInfoResource(self._client)

    @cached_property
    def exposure(self) -> AsyncExposureResource:
        return AsyncExposureResource(self._client)

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
    def inflow_outflow(self) -> InflowOutflowResourceWithRawResponse:
        return InflowOutflowResourceWithRawResponse(self._etf.inflow_outflow)

    @cached_property
    def info(self) -> InfoResourceWithRawResponse:
        return InfoResourceWithRawResponse(self._etf.info)

    @cached_property
    def exposure(self) -> ExposureResourceWithRawResponse:
        return ExposureResourceWithRawResponse(self._etf.exposure)


class AsyncEtfResourceWithRawResponse:
    def __init__(self, etf: AsyncEtfResource) -> None:
        self._etf = etf

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithRawResponse:
        return AsyncHoldingsResourceWithRawResponse(self._etf.holdings)

    @cached_property
    def inflow_outflow(self) -> AsyncInflowOutflowResourceWithRawResponse:
        return AsyncInflowOutflowResourceWithRawResponse(self._etf.inflow_outflow)

    @cached_property
    def info(self) -> AsyncInfoResourceWithRawResponse:
        return AsyncInfoResourceWithRawResponse(self._etf.info)

    @cached_property
    def exposure(self) -> AsyncExposureResourceWithRawResponse:
        return AsyncExposureResourceWithRawResponse(self._etf.exposure)


class EtfResourceWithStreamingResponse:
    def __init__(self, etf: EtfResource) -> None:
        self._etf = etf

    @cached_property
    def holdings(self) -> HoldingsResourceWithStreamingResponse:
        return HoldingsResourceWithStreamingResponse(self._etf.holdings)

    @cached_property
    def inflow_outflow(self) -> InflowOutflowResourceWithStreamingResponse:
        return InflowOutflowResourceWithStreamingResponse(self._etf.inflow_outflow)

    @cached_property
    def info(self) -> InfoResourceWithStreamingResponse:
        return InfoResourceWithStreamingResponse(self._etf.info)

    @cached_property
    def exposure(self) -> ExposureResourceWithStreamingResponse:
        return ExposureResourceWithStreamingResponse(self._etf.exposure)


class AsyncEtfResourceWithStreamingResponse:
    def __init__(self, etf: AsyncEtfResource) -> None:
        self._etf = etf

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithStreamingResponse:
        return AsyncHoldingsResourceWithStreamingResponse(self._etf.holdings)

    @cached_property
    def inflow_outflow(self) -> AsyncInflowOutflowResourceWithStreamingResponse:
        return AsyncInflowOutflowResourceWithStreamingResponse(self._etf.inflow_outflow)

    @cached_property
    def info(self) -> AsyncInfoResourceWithStreamingResponse:
        return AsyncInfoResourceWithStreamingResponse(self._etf.info)

    @cached_property
    def exposure(self) -> AsyncExposureResourceWithStreamingResponse:
        return AsyncExposureResourceWithStreamingResponse(self._etf.exposure)
