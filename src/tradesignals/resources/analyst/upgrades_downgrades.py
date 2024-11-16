# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ..._base_client import make_request_options
from ...types.analyst import upgrades_downgrade_list_params
from ...types.analyst.upgrades_downgrade_list_response import UpgradesDowngradeListResponse

__all__ = ["UpgradesDowngradesResource", "AsyncUpgradesDowngradesResource"]


class UpgradesDowngradesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UpgradesDowngradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return UpgradesDowngradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UpgradesDowngradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return UpgradesDowngradesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpgradesDowngradeListResponse:
        """Retrieve recent analyst upgrades and downgrades across all stocks.

        Filter by
        optional date.

        Args:
          date: Date to filter upgrades and downgrades.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/analyst/upgrades_downgrades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, upgrades_downgrade_list_params.UpgradesDowngradeListParams),
            ),
            cast_to=UpgradesDowngradeListResponse,
        )


class AsyncUpgradesDowngradesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUpgradesDowngradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUpgradesDowngradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUpgradesDowngradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncUpgradesDowngradesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpgradesDowngradeListResponse:
        """Retrieve recent analyst upgrades and downgrades across all stocks.

        Filter by
        optional date.

        Args:
          date: Date to filter upgrades and downgrades.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/analyst/upgrades_downgrades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"date": date}, upgrades_downgrade_list_params.UpgradesDowngradeListParams
                ),
            ),
            cast_to=UpgradesDowngradeListResponse,
        )


class UpgradesDowngradesResourceWithRawResponse:
    def __init__(self, upgrades_downgrades: UpgradesDowngradesResource) -> None:
        self._upgrades_downgrades = upgrades_downgrades

        self.list = to_raw_response_wrapper(
            upgrades_downgrades.list,
        )


class AsyncUpgradesDowngradesResourceWithRawResponse:
    def __init__(self, upgrades_downgrades: AsyncUpgradesDowngradesResource) -> None:
        self._upgrades_downgrades = upgrades_downgrades

        self.list = async_to_raw_response_wrapper(
            upgrades_downgrades.list,
        )


class UpgradesDowngradesResourceWithStreamingResponse:
    def __init__(self, upgrades_downgrades: UpgradesDowngradesResource) -> None:
        self._upgrades_downgrades = upgrades_downgrades

        self.list = to_streamed_response_wrapper(
            upgrades_downgrades.list,
        )


class AsyncUpgradesDowngradesResourceWithStreamingResponse:
    def __init__(self, upgrades_downgrades: AsyncUpgradesDowngradesResource) -> None:
        self._upgrades_downgrades = upgrades_downgrades

        self.list = async_to_streamed_response_wrapper(
            upgrades_downgrades.list,
        )
