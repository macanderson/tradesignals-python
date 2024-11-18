# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .activity import (
    ActivityResource,
    AsyncActivityResource,
    ActivityResourceWithRawResponse,
    AsyncActivityResourceWithRawResponse,
    ActivityResourceWithStreamingResponse,
    AsyncActivityResourceWithStreamingResponse,
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
from .sector_exposure import (
    SectorExposureResource,
    AsyncSectorExposureResource,
    SectorExposureResourceWithRawResponse,
    AsyncSectorExposureResourceWithRawResponse,
    SectorExposureResourceWithStreamingResponse,
    AsyncSectorExposureResourceWithStreamingResponse,
)
from .stock_ownership import (
    StockOwnershipResource,
    AsyncStockOwnershipResource,
    StockOwnershipResourceWithRawResponse,
    AsyncStockOwnershipResourceWithRawResponse,
    StockOwnershipResourceWithStreamingResponse,
    AsyncStockOwnershipResourceWithStreamingResponse,
)
from .institution_list import (
    InstitutionListResource,
    AsyncInstitutionListResource,
    InstitutionListResourceWithRawResponse,
    AsyncInstitutionListResourceWithRawResponse,
    InstitutionListResourceWithStreamingResponse,
    AsyncInstitutionListResourceWithStreamingResponse,
)

__all__ = ["InstitutionResource", "AsyncInstitutionResource"]


class InstitutionResource(SyncAPIResource):
    @cached_property
    def institution_list(self) -> InstitutionListResource:
        return InstitutionListResource(self._client)

    @cached_property
    def activity(self) -> ActivityResource:
        return ActivityResource(self._client)

    @cached_property
    def holdings(self) -> HoldingsResource:
        return HoldingsResource(self._client)

    @cached_property
    def sector_exposure(self) -> SectorExposureResource:
        return SectorExposureResource(self._client)

    @cached_property
    def stock_ownership(self) -> StockOwnershipResource:
        return StockOwnershipResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstitutionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return InstitutionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstitutionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return InstitutionResourceWithStreamingResponse(self)


class AsyncInstitutionResource(AsyncAPIResource):
    @cached_property
    def institution_list(self) -> AsyncInstitutionListResource:
        return AsyncInstitutionListResource(self._client)

    @cached_property
    def activity(self) -> AsyncActivityResource:
        return AsyncActivityResource(self._client)

    @cached_property
    def holdings(self) -> AsyncHoldingsResource:
        return AsyncHoldingsResource(self._client)

    @cached_property
    def sector_exposure(self) -> AsyncSectorExposureResource:
        return AsyncSectorExposureResource(self._client)

    @cached_property
    def stock_ownership(self) -> AsyncStockOwnershipResource:
        return AsyncStockOwnershipResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstitutionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstitutionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstitutionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncInstitutionResourceWithStreamingResponse(self)


class InstitutionResourceWithRawResponse:
    def __init__(self, institution: InstitutionResource) -> None:
        self._institution = institution

    @cached_property
    def institution_list(self) -> InstitutionListResourceWithRawResponse:
        return InstitutionListResourceWithRawResponse(self._institution.institution_list)

    @cached_property
    def activity(self) -> ActivityResourceWithRawResponse:
        return ActivityResourceWithRawResponse(self._institution.activity)

    @cached_property
    def holdings(self) -> HoldingsResourceWithRawResponse:
        return HoldingsResourceWithRawResponse(self._institution.holdings)

    @cached_property
    def sector_exposure(self) -> SectorExposureResourceWithRawResponse:
        return SectorExposureResourceWithRawResponse(self._institution.sector_exposure)

    @cached_property
    def stock_ownership(self) -> StockOwnershipResourceWithRawResponse:
        return StockOwnershipResourceWithRawResponse(self._institution.stock_ownership)


class AsyncInstitutionResourceWithRawResponse:
    def __init__(self, institution: AsyncInstitutionResource) -> None:
        self._institution = institution

    @cached_property
    def institution_list(self) -> AsyncInstitutionListResourceWithRawResponse:
        return AsyncInstitutionListResourceWithRawResponse(self._institution.institution_list)

    @cached_property
    def activity(self) -> AsyncActivityResourceWithRawResponse:
        return AsyncActivityResourceWithRawResponse(self._institution.activity)

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithRawResponse:
        return AsyncHoldingsResourceWithRawResponse(self._institution.holdings)

    @cached_property
    def sector_exposure(self) -> AsyncSectorExposureResourceWithRawResponse:
        return AsyncSectorExposureResourceWithRawResponse(self._institution.sector_exposure)

    @cached_property
    def stock_ownership(self) -> AsyncStockOwnershipResourceWithRawResponse:
        return AsyncStockOwnershipResourceWithRawResponse(self._institution.stock_ownership)


class InstitutionResourceWithStreamingResponse:
    def __init__(self, institution: InstitutionResource) -> None:
        self._institution = institution

    @cached_property
    def institution_list(self) -> InstitutionListResourceWithStreamingResponse:
        return InstitutionListResourceWithStreamingResponse(self._institution.institution_list)

    @cached_property
    def activity(self) -> ActivityResourceWithStreamingResponse:
        return ActivityResourceWithStreamingResponse(self._institution.activity)

    @cached_property
    def holdings(self) -> HoldingsResourceWithStreamingResponse:
        return HoldingsResourceWithStreamingResponse(self._institution.holdings)

    @cached_property
    def sector_exposure(self) -> SectorExposureResourceWithStreamingResponse:
        return SectorExposureResourceWithStreamingResponse(self._institution.sector_exposure)

    @cached_property
    def stock_ownership(self) -> StockOwnershipResourceWithStreamingResponse:
        return StockOwnershipResourceWithStreamingResponse(self._institution.stock_ownership)


class AsyncInstitutionResourceWithStreamingResponse:
    def __init__(self, institution: AsyncInstitutionResource) -> None:
        self._institution = institution

    @cached_property
    def institution_list(self) -> AsyncInstitutionListResourceWithStreamingResponse:
        return AsyncInstitutionListResourceWithStreamingResponse(self._institution.institution_list)

    @cached_property
    def activity(self) -> AsyncActivityResourceWithStreamingResponse:
        return AsyncActivityResourceWithStreamingResponse(self._institution.activity)

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithStreamingResponse:
        return AsyncHoldingsResourceWithStreamingResponse(self._institution.holdings)

    @cached_property
    def sector_exposure(self) -> AsyncSectorExposureResourceWithStreamingResponse:
        return AsyncSectorExposureResourceWithStreamingResponse(self._institution.sector_exposure)

    @cached_property
    def stock_ownership(self) -> AsyncStockOwnershipResourceWithStreamingResponse:
        return AsyncStockOwnershipResourceWithStreamingResponse(self._institution.stock_ownership)
