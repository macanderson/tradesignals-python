# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import make_request_options
from ...types.options.contract_retrieve_response import ContractRetrieveResponse

__all__ = ["ContractResource", "AsyncContractResource"]


class ContractResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return ContractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return ContractResourceWithStreamingResponse(self)

    def retrieve(
        self,
        option_symbol: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractRetrieveResponse:
        """
        Retrieve detailed data for a specific option contract identified by its option
        symbol.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not option_symbol:
            raise ValueError(f"Expected a non-empty value for `option_symbol` but received {option_symbol!r}")
        return self._get(
            f"/api/options/contract/{option_symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveResponse,
        )


class AsyncContractResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncContractResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        option_symbol: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractRetrieveResponse:
        """
        Retrieve detailed data for a specific option contract identified by its option
        symbol.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not option_symbol:
            raise ValueError(f"Expected a non-empty value for `option_symbol` but received {option_symbol!r}")
        return await self._get(
            f"/api/options/contract/{option_symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveResponse,
        )


class ContractResourceWithRawResponse:
    def __init__(self, contract: ContractResource) -> None:
        self._contract = contract

        self.retrieve = to_raw_response_wrapper(
            contract.retrieve,
        )


class AsyncContractResourceWithRawResponse:
    def __init__(self, contract: AsyncContractResource) -> None:
        self._contract = contract

        self.retrieve = async_to_raw_response_wrapper(
            contract.retrieve,
        )


class ContractResourceWithStreamingResponse:
    def __init__(self, contract: ContractResource) -> None:
        self._contract = contract

        self.retrieve = to_streamed_response_wrapper(
            contract.retrieve,
        )


class AsyncContractResourceWithStreamingResponse:
    def __init__(self, contract: AsyncContractResource) -> None:
        self._contract = contract

        self.retrieve = async_to_streamed_response_wrapper(
            contract.retrieve,
        )
