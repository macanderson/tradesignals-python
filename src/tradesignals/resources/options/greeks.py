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
from ...types.options import greek_retrieve_params
from ...types.options.greek_retrieve_response import GreekRetrieveResponse

__all__ = ["GreeksResource", "AsyncGreeksResource"]


class GreeksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GreeksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return GreeksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GreeksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return GreeksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        option_type: Literal["CALL", "PUT"] | NotGiven = NOT_GIVEN,
        strike: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreekRetrieveResponse:
        """Retrieve option greeks data for a specific stock symbol.

        Filter by optional
        expiration date.

        Args:
          expiration: Option expiration date to filter the greeks data.

          option_type: Option type (CALL or PUT).

          strike: Option strike price to filter the greeks data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/api/options/greeks/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expiration": expiration,
                        "option_type": option_type,
                        "strike": strike,
                    },
                    greek_retrieve_params.GreekRetrieveParams,
                ),
            ),
            cast_to=GreekRetrieveResponse,
        )


class AsyncGreeksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGreeksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGreeksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGreeksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncGreeksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        option_type: Literal["CALL", "PUT"] | NotGiven = NOT_GIVEN,
        strike: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreekRetrieveResponse:
        """Retrieve option greeks data for a specific stock symbol.

        Filter by optional
        expiration date.

        Args:
          expiration: Option expiration date to filter the greeks data.

          option_type: Option type (CALL or PUT).

          strike: Option strike price to filter the greeks data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/api/options/greeks/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expiration": expiration,
                        "option_type": option_type,
                        "strike": strike,
                    },
                    greek_retrieve_params.GreekRetrieveParams,
                ),
            ),
            cast_to=GreekRetrieveResponse,
        )


class GreeksResourceWithRawResponse:
    def __init__(self, greeks: GreeksResource) -> None:
        self._greeks = greeks

        self.retrieve = to_raw_response_wrapper(
            greeks.retrieve,
        )


class AsyncGreeksResourceWithRawResponse:
    def __init__(self, greeks: AsyncGreeksResource) -> None:
        self._greeks = greeks

        self.retrieve = async_to_raw_response_wrapper(
            greeks.retrieve,
        )


class GreeksResourceWithStreamingResponse:
    def __init__(self, greeks: GreeksResource) -> None:
        self._greeks = greeks

        self.retrieve = to_streamed_response_wrapper(
            greeks.retrieve,
        )


class AsyncGreeksResourceWithStreamingResponse:
    def __init__(self, greeks: AsyncGreeksResource) -> None:
        self._greeks = greeks

        self.retrieve = async_to_streamed_response_wrapper(
            greeks.retrieve,
        )
