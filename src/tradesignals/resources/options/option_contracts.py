# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ..._base_client import make_request_options
from ...types.options import option_contract_list_params
from ...types.options.option_contract_list_response import OptionContractListResponse

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
        symbol: str,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        option_type: Literal["CALL", "PUT"] | NotGiven = NOT_GIVEN,
        strike: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptionContractListResponse:
        """Retrieve a list of option contracts based on specified filters.

        Filter by
        optional symbol and expiration date.

        Args:
          symbol: Stock symbol to filter option contracts.

          expiration: Option expiration date to filter contracts.

          option_type: Option type (CALL or PUT) to filter contracts.

          strike: Option strike price to filter contracts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/options/contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbol": symbol,
                        "expiration": expiration,
                        "option_type": option_type,
                        "strike": strike,
                    },
                    option_contract_list_params.OptionContractListParams,
                ),
            ),
            cast_to=OptionContractListResponse,
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
        symbol: str,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        option_type: Literal["CALL", "PUT"] | NotGiven = NOT_GIVEN,
        strike: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptionContractListResponse:
        """Retrieve a list of option contracts based on specified filters.

        Filter by
        optional symbol and expiration date.

        Args:
          symbol: Stock symbol to filter option contracts.

          expiration: Option expiration date to filter contracts.

          option_type: Option type (CALL or PUT) to filter contracts.

          strike: Option strike price to filter contracts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/options/contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbol": symbol,
                        "expiration": expiration,
                        "option_type": option_type,
                        "strike": strike,
                    },
                    option_contract_list_params.OptionContractListParams,
                ),
            ),
            cast_to=OptionContractListResponse,
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
