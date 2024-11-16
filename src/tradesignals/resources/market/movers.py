# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.market import mover_list_params
from ...types.market.mover_list_response import MoverListResponse

__all__ = ["MoversResource", "AsyncMoversResource"]


class MoversResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MoversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return MoversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MoversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return MoversResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        type: Literal["gainers", "losers"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MoverListResponse:
        """Retrieve top gainers and losers in the market.

        Filter by optional type.

        Args:
          limit: Number of records to retrieve.

          type: Type of movers to retrieve ('gainers' or 'losers').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/market/movers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "type": type,
                    },
                    mover_list_params.MoverListParams,
                ),
            ),
            cast_to=MoverListResponse,
        )


class AsyncMoversResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMoversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMoversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMoversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncMoversResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        type: Literal["gainers", "losers"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MoverListResponse:
        """Retrieve top gainers and losers in the market.

        Filter by optional type.

        Args:
          limit: Number of records to retrieve.

          type: Type of movers to retrieve ('gainers' or 'losers').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/market/movers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "type": type,
                    },
                    mover_list_params.MoverListParams,
                ),
            ),
            cast_to=MoverListResponse,
        )


class MoversResourceWithRawResponse:
    def __init__(self, movers: MoversResource) -> None:
        self._movers = movers

        self.list = to_raw_response_wrapper(
            movers.list,
        )


class AsyncMoversResourceWithRawResponse:
    def __init__(self, movers: AsyncMoversResource) -> None:
        self._movers = movers

        self.list = async_to_raw_response_wrapper(
            movers.list,
        )


class MoversResourceWithStreamingResponse:
    def __init__(self, movers: MoversResource) -> None:
        self._movers = movers

        self.list = to_streamed_response_wrapper(
            movers.list,
        )


class AsyncMoversResourceWithStreamingResponse:
    def __init__(self, movers: AsyncMoversResource) -> None:
        self._movers = movers

        self.list = async_to_streamed_response_wrapper(
            movers.list,
        )
