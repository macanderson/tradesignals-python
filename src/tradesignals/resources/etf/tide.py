# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

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
from ...types.etf import tide_retrieve_params
from ..._base_client import make_request_options
from ...types.etf.tide_retrieve_response import TideRetrieveResponse

__all__ = ["TideResource", "AsyncTideResource"]


class TideResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TideResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return TideResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TideResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return TideResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        etf: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TideRetrieveResponse:
        """Retrieve data showing ETF inflows and outflows.

        Filter by optional date and ETF
        symbol.

        Args:
          date: Date to filter ETF tide data.

          etf: ETF symbol to filter data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/etf/tide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "etf": etf,
                    },
                    tide_retrieve_params.TideRetrieveParams,
                ),
            ),
            cast_to=TideRetrieveResponse,
        )


class AsyncTideResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTideResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTideResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTideResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncTideResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        etf: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TideRetrieveResponse:
        """Retrieve data showing ETF inflows and outflows.

        Filter by optional date and ETF
        symbol.

        Args:
          date: Date to filter ETF tide data.

          etf: ETF symbol to filter data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/etf/tide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "etf": etf,
                    },
                    tide_retrieve_params.TideRetrieveParams,
                ),
            ),
            cast_to=TideRetrieveResponse,
        )


class TideResourceWithRawResponse:
    def __init__(self, tide: TideResource) -> None:
        self._tide = tide

        self.retrieve = to_raw_response_wrapper(
            tide.retrieve,
        )


class AsyncTideResourceWithRawResponse:
    def __init__(self, tide: AsyncTideResource) -> None:
        self._tide = tide

        self.retrieve = async_to_raw_response_wrapper(
            tide.retrieve,
        )


class TideResourceWithStreamingResponse:
    def __init__(self, tide: TideResource) -> None:
        self._tide = tide

        self.retrieve = to_streamed_response_wrapper(
            tide.retrieve,
        )


class AsyncTideResourceWithStreamingResponse:
    def __init__(self, tide: AsyncTideResource) -> None:
        self._tide = tide

        self.retrieve = async_to_streamed_response_wrapper(
            tide.retrieve,
        )
