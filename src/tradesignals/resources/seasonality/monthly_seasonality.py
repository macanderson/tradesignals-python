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
from ...types.seasonality.monthly_seasonality_list_response import MonthlySeasonalityListResponse

__all__ = ["MonthlySeasonalityResource", "AsyncMonthlySeasonalityResource"]


class MonthlySeasonalityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MonthlySeasonalityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return MonthlySeasonalityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonthlySeasonalityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return MonthlySeasonalityResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MonthlySeasonalityListResponse]:
        """
        Returns the average return by month for the given ticker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/seasonality/{ticker}/monthly",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[MonthlySeasonalityListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MonthlySeasonalityListResponse]], DataWrapper[MonthlySeasonalityListResponse]),
        )


class AsyncMonthlySeasonalityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMonthlySeasonalityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMonthlySeasonalityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonthlySeasonalityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncMonthlySeasonalityResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MonthlySeasonalityListResponse]:
        """
        Returns the average return by month for the given ticker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/seasonality/{ticker}/monthly",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[MonthlySeasonalityListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MonthlySeasonalityListResponse]], DataWrapper[MonthlySeasonalityListResponse]),
        )


class MonthlySeasonalityResourceWithRawResponse:
    def __init__(self, monthly_seasonality: MonthlySeasonalityResource) -> None:
        self._monthly_seasonality = monthly_seasonality

        self.list = to_raw_response_wrapper(
            monthly_seasonality.list,
        )


class AsyncMonthlySeasonalityResourceWithRawResponse:
    def __init__(self, monthly_seasonality: AsyncMonthlySeasonalityResource) -> None:
        self._monthly_seasonality = monthly_seasonality

        self.list = async_to_raw_response_wrapper(
            monthly_seasonality.list,
        )


class MonthlySeasonalityResourceWithStreamingResponse:
    def __init__(self, monthly_seasonality: MonthlySeasonalityResource) -> None:
        self._monthly_seasonality = monthly_seasonality

        self.list = to_streamed_response_wrapper(
            monthly_seasonality.list,
        )


class AsyncMonthlySeasonalityResourceWithStreamingResponse:
    def __init__(self, monthly_seasonality: AsyncMonthlySeasonalityResource) -> None:
        self._monthly_seasonality = monthly_seasonality

        self.list = async_to_streamed_response_wrapper(
            monthly_seasonality.list,
        )
