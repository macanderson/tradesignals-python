# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import date

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ...types.institution import sector_exposure_list_params
from ...types.institution.sector_exposure_list_response import SectorExposureListResponse

__all__ = ["SectorExposureResource", "AsyncSectorExposureResource"]


class SectorExposureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SectorExposureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return SectorExposureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SectorExposureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return SectorExposureResourceWithStreamingResponse(self)

    def list(
        self,
        name: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SectorExposureListResponse]:
        """
        Returns the sector exposure for a given institution.

        Args:
          date: A date in the format of YYYY-MM-DD.

          limit: How many items to return. Default 500. Max 500. Min 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/api/institution/{name}/sectors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                    },
                    sector_exposure_list_params.SectorExposureListParams,
                ),
                post_parser=DataWrapper[Optional[SectorExposureListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SectorExposureListResponse]], DataWrapper[SectorExposureListResponse]),
        )


class AsyncSectorExposureResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSectorExposureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSectorExposureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSectorExposureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncSectorExposureResourceWithStreamingResponse(self)

    async def list(
        self,
        name: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SectorExposureListResponse]:
        """
        Returns the sector exposure for a given institution.

        Args:
          date: A date in the format of YYYY-MM-DD.

          limit: How many items to return. Default 500. Max 500. Min 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/api/institution/{name}/sectors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                    },
                    sector_exposure_list_params.SectorExposureListParams,
                ),
                post_parser=DataWrapper[Optional[SectorExposureListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SectorExposureListResponse]], DataWrapper[SectorExposureListResponse]),
        )


class SectorExposureResourceWithRawResponse:
    def __init__(self, sector_exposure: SectorExposureResource) -> None:
        self._sector_exposure = sector_exposure

        self.list = to_raw_response_wrapper(
            sector_exposure.list,
        )


class AsyncSectorExposureResourceWithRawResponse:
    def __init__(self, sector_exposure: AsyncSectorExposureResource) -> None:
        self._sector_exposure = sector_exposure

        self.list = async_to_raw_response_wrapper(
            sector_exposure.list,
        )


class SectorExposureResourceWithStreamingResponse:
    def __init__(self, sector_exposure: SectorExposureResource) -> None:
        self._sector_exposure = sector_exposure

        self.list = to_streamed_response_wrapper(
            sector_exposure.list,
        )


class AsyncSectorExposureResourceWithStreamingResponse:
    def __init__(self, sector_exposure: AsyncSectorExposureResource) -> None:
        self._sector_exposure = sector_exposure

        self.list = async_to_streamed_response_wrapper(
            sector_exposure.list,
        )
