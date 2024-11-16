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
from ...types.options import contract_list_params

__all__ = ["ContractsResource", "AsyncContractsResource"]


class ContractsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return ContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#with_streaming_response
        """
        return ContractsResourceWithStreamingResponse(self)

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
    ) -> object:
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
                    contract_list_params.ContractListParams,
                ),
            ),
            cast_to=object,
        )


class AsyncContractsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tradesignals-python#with_streaming_response
        """
        return AsyncContractsResourceWithStreamingResponse(self)

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
    ) -> object:
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
                    contract_list_params.ContractListParams,
                ),
            ),
            cast_to=object,
        )


class ContractsResourceWithRawResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.list = to_raw_response_wrapper(
            contracts.list,
        )


class AsyncContractsResourceWithRawResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.list = async_to_raw_response_wrapper(
            contracts.list,
        )


class ContractsResourceWithStreamingResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.list = to_streamed_response_wrapper(
            contracts.list,
        )


class AsyncContractsResourceWithStreamingResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.list = async_to_streamed_response_wrapper(
            contracts.list,
        )
