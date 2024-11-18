# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.market_data.sector_etf_list_response import SectorEtfListResponse

__all__ = ["SectorEtfsResource", "AsyncSectorEtfsResource"]


class SectorEtfsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SectorEtfsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return SectorEtfsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SectorEtfsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return SectorEtfsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SectorEtfListResponse]:
        """Returns the current trading day's statistics for SPDR sector ETFs."""
        return self._get(
            "/api/market/sector-etfs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[SectorEtfListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SectorEtfListResponse]], DataWrapper[SectorEtfListResponse]),
        )


class AsyncSectorEtfsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSectorEtfsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSectorEtfsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSectorEtfsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncSectorEtfsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SectorEtfListResponse]:
        """Returns the current trading day's statistics for SPDR sector ETFs."""
        return await self._get(
            "/api/market/sector-etfs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[SectorEtfListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SectorEtfListResponse]], DataWrapper[SectorEtfListResponse]),
        )


class SectorEtfsResourceWithRawResponse:
    def __init__(self, sector_etfs: SectorEtfsResource) -> None:
        self._sector_etfs = sector_etfs

        self.list = to_raw_response_wrapper(
            sector_etfs.list,
        )


class AsyncSectorEtfsResourceWithRawResponse:
    def __init__(self, sector_etfs: AsyncSectorEtfsResource) -> None:
        self._sector_etfs = sector_etfs

        self.list = async_to_raw_response_wrapper(
            sector_etfs.list,
        )


class SectorEtfsResourceWithStreamingResponse:
    def __init__(self, sector_etfs: SectorEtfsResource) -> None:
        self._sector_etfs = sector_etfs

        self.list = to_streamed_response_wrapper(
            sector_etfs.list,
        )


class AsyncSectorEtfsResourceWithStreamingResponse:
    def __init__(self, sector_etfs: AsyncSectorEtfsResource) -> None:
        self._sector_etfs = sector_etfs

        self.list = async_to_streamed_response_wrapper(
            sector_etfs.list,
        )
