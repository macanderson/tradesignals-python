# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
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
from ...types.option_contracts import underlying_chain_list_params
from ...types.option_contracts.underlying_chain_list_response import UnderlyingChainListResponse

__all__ = ["UnderlyingChainsResource", "AsyncUnderlyingChainsResource"]


class UnderlyingChainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UnderlyingChainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return UnderlyingChainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnderlyingChainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return UnderlyingChainsResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        exclude_zero_dte: bool | NotGiven = NOT_GIVEN,
        exclude_zero_oi_chains: bool | NotGiven = NOT_GIVEN,
        exclude_zero_vol_chains: bool | NotGiven = NOT_GIVEN,
        expiry: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        maybe_otm_only: bool | NotGiven = NOT_GIVEN,
        option_type: Literal["call", "put"] | NotGiven = NOT_GIVEN,
        vol_greater_oi: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnderlyingChainListResponse]:
        """
        Returns all option contracts for the given ticker.

        Args:
          exclude_zero_dte: Exclude chains expiring the same day.

          exclude_zero_oi_chains: Exclude chains where open interest is zero.

          exclude_zero_vol_chains: Exclude chains where volume is zero.

          expiry: Filter by expiry date.

          limit: The number of items to return. Minimum is 1.

          maybe_otm_only: Include only out-of-the-money chains.

          option_type: Filter by option type (call/put).

          vol_greater_oi: Include only chains where volume > open interest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/stock/{ticker}/option-contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_zero_dte": exclude_zero_dte,
                        "exclude_zero_oi_chains": exclude_zero_oi_chains,
                        "exclude_zero_vol_chains": exclude_zero_vol_chains,
                        "expiry": expiry,
                        "limit": limit,
                        "maybe_otm_only": maybe_otm_only,
                        "option_type": option_type,
                        "vol_greater_oi": vol_greater_oi,
                    },
                    underlying_chain_list_params.UnderlyingChainListParams,
                ),
                post_parser=DataWrapper[Optional[UnderlyingChainListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UnderlyingChainListResponse]], DataWrapper[UnderlyingChainListResponse]),
        )


class AsyncUnderlyingChainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUnderlyingChainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUnderlyingChainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnderlyingChainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncUnderlyingChainsResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        exclude_zero_dte: bool | NotGiven = NOT_GIVEN,
        exclude_zero_oi_chains: bool | NotGiven = NOT_GIVEN,
        exclude_zero_vol_chains: bool | NotGiven = NOT_GIVEN,
        expiry: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        maybe_otm_only: bool | NotGiven = NOT_GIVEN,
        option_type: Literal["call", "put"] | NotGiven = NOT_GIVEN,
        vol_greater_oi: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UnderlyingChainListResponse]:
        """
        Returns all option contracts for the given ticker.

        Args:
          exclude_zero_dte: Exclude chains expiring the same day.

          exclude_zero_oi_chains: Exclude chains where open interest is zero.

          exclude_zero_vol_chains: Exclude chains where volume is zero.

          expiry: Filter by expiry date.

          limit: The number of items to return. Minimum is 1.

          maybe_otm_only: Include only out-of-the-money chains.

          option_type: Filter by option type (call/put).

          vol_greater_oi: Include only chains where volume > open interest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/stock/{ticker}/option-contracts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exclude_zero_dte": exclude_zero_dte,
                        "exclude_zero_oi_chains": exclude_zero_oi_chains,
                        "exclude_zero_vol_chains": exclude_zero_vol_chains,
                        "expiry": expiry,
                        "limit": limit,
                        "maybe_otm_only": maybe_otm_only,
                        "option_type": option_type,
                        "vol_greater_oi": vol_greater_oi,
                    },
                    underlying_chain_list_params.UnderlyingChainListParams,
                ),
                post_parser=DataWrapper[Optional[UnderlyingChainListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UnderlyingChainListResponse]], DataWrapper[UnderlyingChainListResponse]),
        )


class UnderlyingChainsResourceWithRawResponse:
    def __init__(self, underlying_chains: UnderlyingChainsResource) -> None:
        self._underlying_chains = underlying_chains

        self.list = to_raw_response_wrapper(
            underlying_chains.list,
        )


class AsyncUnderlyingChainsResourceWithRawResponse:
    def __init__(self, underlying_chains: AsyncUnderlyingChainsResource) -> None:
        self._underlying_chains = underlying_chains

        self.list = async_to_raw_response_wrapper(
            underlying_chains.list,
        )


class UnderlyingChainsResourceWithStreamingResponse:
    def __init__(self, underlying_chains: UnderlyingChainsResource) -> None:
        self._underlying_chains = underlying_chains

        self.list = to_streamed_response_wrapper(
            underlying_chains.list,
        )


class AsyncUnderlyingChainsResourceWithStreamingResponse:
    def __init__(self, underlying_chains: AsyncUnderlyingChainsResource) -> None:
        self._underlying_chains = underlying_chains

        self.list = async_to_streamed_response_wrapper(
            underlying_chains.list,
        )
