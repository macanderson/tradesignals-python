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
from ...types.options import list_contract_list_params
from ...types.options.list_contract_list_response import ListContractListResponse

__all__ = ["ListContractsResource", "AsyncListContractsResource"]


class ListContractsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return ListContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return ListContractsResourceWithStreamingResponse(self)

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
    ) -> ListContractListResponse:
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
                    list_contract_list_params.ListContractListParams,
                ),
            ),
            cast_to=ListContractListResponse,
        )


class AsyncListContractsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncListContractsResourceWithStreamingResponse(self)

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
    ) -> ListContractListResponse:
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
                    list_contract_list_params.ListContractListParams,
                ),
            ),
            cast_to=ListContractListResponse,
        )


class ListContractsResourceWithRawResponse:
    def __init__(self, list_contracts: ListContractsResource) -> None:
        self._list_contracts = list_contracts

        self.list = to_raw_response_wrapper(
            list_contracts.list,
        )


class AsyncListContractsResourceWithRawResponse:
    def __init__(self, list_contracts: AsyncListContractsResource) -> None:
        self._list_contracts = list_contracts

        self.list = async_to_raw_response_wrapper(
            list_contracts.list,
        )


class ListContractsResourceWithStreamingResponse:
    def __init__(self, list_contracts: ListContractsResource) -> None:
        self._list_contracts = list_contracts

        self.list = to_streamed_response_wrapper(
            list_contracts.list,
        )


class AsyncListContractsResourceWithStreamingResponse:
    def __init__(self, list_contracts: AsyncListContractsResource) -> None:
        self._list_contracts = list_contracts

        self.list = async_to_streamed_response_wrapper(
            list_contracts.list,
        )
