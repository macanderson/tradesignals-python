# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

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
from ...types.seasonality import performer_list_params
from ...types.seasonality.performer_list_response import PerformerListResponse

__all__ = ["PerformersResource", "AsyncPerformersResource"]


class PerformersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PerformersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return PerformersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PerformersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return PerformersResourceWithStreamingResponse(self)

    def list(
        self,
        month: int,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        min_oi: int | NotGiven = NOT_GIVEN,
        min_years: int | NotGiven = NOT_GIVEN,
        order: Literal[
            "ticker",
            "month",
            "positive_closes",
            "years",
            "positive_months_perc",
            "median_change",
            "avg_change",
            "max_change",
            "min_change",
        ]
        | NotGiven = NOT_GIVEN,
        order_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        s_p_500_nasdaq_only: bool | NotGiven = NOT_GIVEN,
        ticker_for_sector: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PerformerListResponse]:
        """
        Returns the tickers with the highest performance in terms of price change in the
        given month.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/api/seasonality/{month}/performers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "min_oi": min_oi,
                        "min_years": min_years,
                        "order": order,
                        "order_direction": order_direction,
                        "s_p_500_nasdaq_only": s_p_500_nasdaq_only,
                        "ticker_for_sector": ticker_for_sector,
                    },
                    performer_list_params.PerformerListParams,
                ),
                post_parser=DataWrapper[Optional[PerformerListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PerformerListResponse]], DataWrapper[PerformerListResponse]),
        )


class AsyncPerformersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPerformersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPerformersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPerformersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncPerformersResourceWithStreamingResponse(self)

    async def list(
        self,
        month: int,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        min_oi: int | NotGiven = NOT_GIVEN,
        min_years: int | NotGiven = NOT_GIVEN,
        order: Literal[
            "ticker",
            "month",
            "positive_closes",
            "years",
            "positive_months_perc",
            "median_change",
            "avg_change",
            "max_change",
            "min_change",
        ]
        | NotGiven = NOT_GIVEN,
        order_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        s_p_500_nasdaq_only: bool | NotGiven = NOT_GIVEN,
        ticker_for_sector: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PerformerListResponse]:
        """
        Returns the tickers with the highest performance in terms of price change in the
        given month.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/api/seasonality/{month}/performers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "min_oi": min_oi,
                        "min_years": min_years,
                        "order": order,
                        "order_direction": order_direction,
                        "s_p_500_nasdaq_only": s_p_500_nasdaq_only,
                        "ticker_for_sector": ticker_for_sector,
                    },
                    performer_list_params.PerformerListParams,
                ),
                post_parser=DataWrapper[Optional[PerformerListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PerformerListResponse]], DataWrapper[PerformerListResponse]),
        )


class PerformersResourceWithRawResponse:
    def __init__(self, performers: PerformersResource) -> None:
        self._performers = performers

        self.list = to_raw_response_wrapper(
            performers.list,
        )


class AsyncPerformersResourceWithRawResponse:
    def __init__(self, performers: AsyncPerformersResource) -> None:
        self._performers = performers

        self.list = async_to_raw_response_wrapper(
            performers.list,
        )


class PerformersResourceWithStreamingResponse:
    def __init__(self, performers: PerformersResource) -> None:
        self._performers = performers

        self.list = to_streamed_response_wrapper(
            performers.list,
        )


class AsyncPerformersResourceWithStreamingResponse:
    def __init__(self, performers: AsyncPerformersResource) -> None:
        self._performers = performers

        self.list = async_to_streamed_response_wrapper(
            performers.list,
        )
