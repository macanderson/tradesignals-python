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
from ...types.screener import option_contract_list_params
from ...types.screener.option_contract_list_response import OptionContractListResponse

__all__ = ["OptionContractsResource", "AsyncOptionContractsResource"]


class OptionContractsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptionContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OptionContractsResourceWithStreamingResponse(self)

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
    ) -> Optional[OptionContractListResponse]:
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
                    option_contract_list_params.OptionContractListParams,
                ),
                post_parser=DataWrapper[Optional[OptionContractListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OptionContractListResponse]], DataWrapper[OptionContractListResponse]),
        )


class AsyncOptionContractsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptionContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOptionContractsResourceWithStreamingResponse(self)

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
    ) -> Optional[OptionContractListResponse]:
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
                    option_contract_list_params.OptionContractListParams,
                ),
                post_parser=DataWrapper[Optional[OptionContractListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OptionContractListResponse]], DataWrapper[OptionContractListResponse]),
        )


class OptionContractsResourceWithRawResponse:
    def __init__(self, option_contracts: OptionContractsResource) -> None:
        self._option_contracts = option_contracts

        self.list = to_raw_response_wrapper(
            option_contracts.list,
        )


class AsyncOptionContractsResourceWithRawResponse:
    def __init__(self, option_contracts: AsyncOptionContractsResource) -> None:
        self._option_contracts = option_contracts

        self.list = async_to_raw_response_wrapper(
            option_contracts.list,
        )


class OptionContractsResourceWithStreamingResponse:
    def __init__(self, option_contracts: OptionContractsResource) -> None:
        self._option_contracts = option_contracts

        self.list = to_streamed_response_wrapper(
            option_contracts.list,
        )


class AsyncOptionContractsResourceWithStreamingResponse:
    def __init__(self, option_contracts: AsyncOptionContractsResource) -> None:
        self._option_contracts = option_contracts

        self.list = async_to_streamed_response_wrapper(
            option_contracts.list,
        )
