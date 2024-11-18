# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

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
from ...types.stock import atm_chain_list_params
from ..._base_client import make_request_options
from ...types.stock.atm_chain_list_response import AtmChainListResponse

__all__ = ["AtmChainsResource", "AsyncAtmChainsResource"]


class AtmChainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AtmChainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AtmChainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AtmChainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AtmChainsResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        expirations: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AtmChainListResponse]:
        """
        Returns the ATM chains for the given expirations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/stock/{ticker}/atm-chains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expirations": expirations}, atm_chain_list_params.AtmChainListParams),
                post_parser=DataWrapper[Optional[AtmChainListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AtmChainListResponse]], DataWrapper[AtmChainListResponse]),
        )


class AsyncAtmChainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAtmChainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAtmChainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAtmChainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncAtmChainsResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        expirations: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AtmChainListResponse]:
        """
        Returns the ATM chains for the given expirations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/stock/{ticker}/atm-chains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expirations": expirations}, atm_chain_list_params.AtmChainListParams
                ),
                post_parser=DataWrapper[Optional[AtmChainListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AtmChainListResponse]], DataWrapper[AtmChainListResponse]),
        )


class AtmChainsResourceWithRawResponse:
    def __init__(self, atm_chains: AtmChainsResource) -> None:
        self._atm_chains = atm_chains

        self.list = to_raw_response_wrapper(
            atm_chains.list,
        )


class AsyncAtmChainsResourceWithRawResponse:
    def __init__(self, atm_chains: AsyncAtmChainsResource) -> None:
        self._atm_chains = atm_chains

        self.list = async_to_raw_response_wrapper(
            atm_chains.list,
        )


class AtmChainsResourceWithStreamingResponse:
    def __init__(self, atm_chains: AtmChainsResource) -> None:
        self._atm_chains = atm_chains

        self.list = to_streamed_response_wrapper(
            atm_chains.list,
        )


class AsyncAtmChainsResourceWithStreamingResponse:
    def __init__(self, atm_chains: AsyncAtmChainsResource) -> None:
        self._atm_chains = atm_chains

        self.list = async_to_streamed_response_wrapper(
            atm_chains.list,
        )
