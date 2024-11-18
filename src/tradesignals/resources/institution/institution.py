# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .institutions import (
    InstitutionsResource,
    AsyncInstitutionsResource,
    InstitutionsResourceWithRawResponse,
    AsyncInstitutionsResourceWithRawResponse,
    InstitutionsResourceWithStreamingResponse,
    AsyncInstitutionsResourceWithStreamingResponse,
)
from .sector_exposure import (
    SectorExposureResource,
    AsyncSectorExposureResource,
    SectorExposureResourceWithRawResponse,
    AsyncSectorExposureResourceWithRawResponse,
    SectorExposureResourceWithStreamingResponse,
    AsyncSectorExposureResourceWithStreamingResponse,
)
from .equity_ownership import (
    EquityOwnershipResource,
    AsyncEquityOwnershipResource,
    EquityOwnershipResourceWithRawResponse,
    AsyncEquityOwnershipResourceWithRawResponse,
    EquityOwnershipResourceWithStreamingResponse,
    AsyncEquityOwnershipResourceWithStreamingResponse,
)
from .trading_activity import (
    TradingActivityResource,
    AsyncTradingActivityResource,
    TradingActivityResourceWithRawResponse,
    AsyncTradingActivityResourceWithRawResponse,
    TradingActivityResourceWithStreamingResponse,
    AsyncTradingActivityResourceWithStreamingResponse,
)

__all__ = ["InstitutionResource", "AsyncInstitutionResource"]


class InstitutionResource(SyncAPIResource):
    """
    -> Institution endpoints provide data and insights into the activities, holdings, and sector exposure of hedge funds.
    """

    @cached_property
    def institutions(self) -> InstitutionsResource:
        return InstitutionsResource(self._client)

    @cached_property
    def trading_activity(self) -> TradingActivityResource:
        return TradingActivityResource(self._client)

    @cached_property
    def holdings(self) -> HoldingsResource:
        return HoldingsResource(self._client)

    @cached_property
    def sector_exposure(self) -> SectorExposureResource:
        return SectorExposureResource(self._client)

    @cached_property
    def equity_ownership(self) -> EquityOwnershipResource:
        return EquityOwnershipResource(self._client)

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
    """
    -> Institution endpoints provide data and insights into the activities, holdings, and sector exposure of hedge funds.
    """

    @cached_property
    def institutions(self) -> AsyncInstitutionsResource:
        return AsyncInstitutionsResource(self._client)

    @cached_property
    def trading_activity(self) -> AsyncTradingActivityResource:
        return AsyncTradingActivityResource(self._client)

    @cached_property
    def holdings(self) -> AsyncHoldingsResource:
        return AsyncHoldingsResource(self._client)

    @cached_property
    def sector_exposure(self) -> AsyncSectorExposureResource:
        return AsyncSectorExposureResource(self._client)

    @cached_property
    def equity_ownership(self) -> AsyncEquityOwnershipResource:
        return AsyncEquityOwnershipResource(self._client)

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
    def institutions(self) -> InstitutionsResourceWithRawResponse:
        return InstitutionsResourceWithRawResponse(self._institution.institutions)

    @cached_property
    def trading_activity(self) -> TradingActivityResourceWithRawResponse:
        return TradingActivityResourceWithRawResponse(self._institution.trading_activity)

    @cached_property
    def holdings(self) -> HoldingsResourceWithRawResponse:
        return HoldingsResourceWithRawResponse(self._institution.holdings)

    @cached_property
    def sector_exposure(self) -> SectorExposureResourceWithRawResponse:
        return SectorExposureResourceWithRawResponse(self._institution.sector_exposure)

    @cached_property
    def equity_ownership(self) -> EquityOwnershipResourceWithRawResponse:
        return EquityOwnershipResourceWithRawResponse(self._institution.equity_ownership)


class AsyncInstitutionResourceWithRawResponse:
    def __init__(self, institution: AsyncInstitutionResource) -> None:
        self._institution = institution

    @cached_property
    def institutions(self) -> AsyncInstitutionsResourceWithRawResponse:
        return AsyncInstitutionsResourceWithRawResponse(self._institution.institutions)

    @cached_property
    def trading_activity(self) -> AsyncTradingActivityResourceWithRawResponse:
        return AsyncTradingActivityResourceWithRawResponse(self._institution.trading_activity)

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithRawResponse:
        return AsyncHoldingsResourceWithRawResponse(self._institution.holdings)

    @cached_property
    def sector_exposure(self) -> AsyncSectorExposureResourceWithRawResponse:
        return AsyncSectorExposureResourceWithRawResponse(self._institution.sector_exposure)

    @cached_property
    def equity_ownership(self) -> AsyncEquityOwnershipResourceWithRawResponse:
        return AsyncEquityOwnershipResourceWithRawResponse(self._institution.equity_ownership)


class InstitutionResourceWithStreamingResponse:
    def __init__(self, institution: InstitutionResource) -> None:
        self._institution = institution

    @cached_property
    def institutions(self) -> InstitutionsResourceWithStreamingResponse:
        return InstitutionsResourceWithStreamingResponse(self._institution.institutions)

    @cached_property
    def trading_activity(self) -> TradingActivityResourceWithStreamingResponse:
        return TradingActivityResourceWithStreamingResponse(self._institution.trading_activity)

    @cached_property
    def holdings(self) -> HoldingsResourceWithStreamingResponse:
        return HoldingsResourceWithStreamingResponse(self._institution.holdings)

    @cached_property
    def sector_exposure(self) -> SectorExposureResourceWithStreamingResponse:
        return SectorExposureResourceWithStreamingResponse(self._institution.sector_exposure)

    @cached_property
    def equity_ownership(self) -> EquityOwnershipResourceWithStreamingResponse:
        return EquityOwnershipResourceWithStreamingResponse(self._institution.equity_ownership)


class AsyncInstitutionResourceWithStreamingResponse:
    def __init__(self, institution: AsyncInstitutionResource) -> None:
        self._institution = institution

    @cached_property
    def institutions(self) -> AsyncInstitutionsResourceWithStreamingResponse:
        return AsyncInstitutionsResourceWithStreamingResponse(self._institution.institutions)

    @cached_property
    def trading_activity(self) -> AsyncTradingActivityResourceWithStreamingResponse:
        return AsyncTradingActivityResourceWithStreamingResponse(self._institution.trading_activity)

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithStreamingResponse:
        return AsyncHoldingsResourceWithStreamingResponse(self._institution.holdings)

    @cached_property
    def sector_exposure(self) -> AsyncSectorExposureResourceWithStreamingResponse:
        return AsyncSectorExposureResourceWithStreamingResponse(self._institution.sector_exposure)

    @cached_property
    def equity_ownership(self) -> AsyncEquityOwnershipResourceWithStreamingResponse:
        return AsyncEquityOwnershipResourceWithStreamingResponse(self._institution.equity_ownership)
