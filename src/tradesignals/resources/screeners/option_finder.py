# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast
from datetime import date
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
from ...types.screeners import option_finder_list_params
from ...types.screeners.option_finder_list_response import OptionFinderListResponse

__all__ = ["OptionFinderResource", "AsyncOptionFinderResource"]


class OptionFinderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptionFinderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionFinderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionFinderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OptionFinderResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        expiry_dates: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        is_otm: bool | NotGiven = NOT_GIVEN,
        issue_types: List[Literal["Common Stock", "ETF", "Index", "ADR"]] | NotGiven = NOT_GIVEN,
        max_daily_perc_change: float | NotGiven = NOT_GIVEN,
        min_volume: int | NotGiven = NOT_GIVEN,
        order: Literal["bid_ask_vol", "bull_bear_vol", "contract_pricing", "daily_perc_change", "volume"]
        | NotGiven = NOT_GIVEN,
        order_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OptionFinderListResponse]:
        """
        A contract screener endpoint to screen the market for contracts by a variety of
        filter options. Contracts with a volume of less than 200 are not returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/screener/option-contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expiry_dates": expiry_dates,
                        "is_otm": is_otm,
                        "issue_types": issue_types,
                        "max_daily_perc_change": max_daily_perc_change,
                        "min_volume": min_volume,
                        "order": order,
                        "order_direction": order_direction,
                    },
                    option_finder_list_params.OptionFinderListParams,
                ),
                post_parser=DataWrapper[Optional[OptionFinderListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OptionFinderListResponse]], DataWrapper[OptionFinderListResponse]),
        )


class AsyncOptionFinderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptionFinderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionFinderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionFinderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOptionFinderResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        expiry_dates: List[Union[str, date]] | NotGiven = NOT_GIVEN,
        is_otm: bool | NotGiven = NOT_GIVEN,
        issue_types: List[Literal["Common Stock", "ETF", "Index", "ADR"]] | NotGiven = NOT_GIVEN,
        max_daily_perc_change: float | NotGiven = NOT_GIVEN,
        min_volume: int | NotGiven = NOT_GIVEN,
        order: Literal["bid_ask_vol", "bull_bear_vol", "contract_pricing", "daily_perc_change", "volume"]
        | NotGiven = NOT_GIVEN,
        order_direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OptionFinderListResponse]:
        """
        A contract screener endpoint to screen the market for contracts by a variety of
        filter options. Contracts with a volume of less than 200 are not returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/screener/option-contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expiry_dates": expiry_dates,
                        "is_otm": is_otm,
                        "issue_types": issue_types,
                        "max_daily_perc_change": max_daily_perc_change,
                        "min_volume": min_volume,
                        "order": order,
                        "order_direction": order_direction,
                    },
                    option_finder_list_params.OptionFinderListParams,
                ),
                post_parser=DataWrapper[Optional[OptionFinderListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OptionFinderListResponse]], DataWrapper[OptionFinderListResponse]),
        )


class OptionFinderResourceWithRawResponse:
    def __init__(self, option_finder: OptionFinderResource) -> None:
        self._option_finder = option_finder

        self.list = to_raw_response_wrapper(
            option_finder.list,
        )


class AsyncOptionFinderResourceWithRawResponse:
    def __init__(self, option_finder: AsyncOptionFinderResource) -> None:
        self._option_finder = option_finder

        self.list = async_to_raw_response_wrapper(
            option_finder.list,
        )


class OptionFinderResourceWithStreamingResponse:
    def __init__(self, option_finder: OptionFinderResource) -> None:
        self._option_finder = option_finder

        self.list = to_streamed_response_wrapper(
            option_finder.list,
        )


class AsyncOptionFinderResourceWithStreamingResponse:
    def __init__(self, option_finder: AsyncOptionFinderResource) -> None:
        self._option_finder = option_finder

        self.list = async_to_streamed_response_wrapper(
            option_finder.list,
        )
