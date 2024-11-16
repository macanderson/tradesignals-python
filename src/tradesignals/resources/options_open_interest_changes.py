# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import options_open_interest_change_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.options_open_interest_change_retrieve_response import OptionsOpenInterestChangeRetrieveResponse

__all__ = ["OptionsOpenInterestChangesResource", "AsyncOptionsOpenInterestChangesResource"]


class OptionsOpenInterestChangesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptionsOpenInterestChangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionsOpenInterestChangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsOpenInterestChangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OptionsOpenInterestChangesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptionsOpenInterestChangeRetrieveResponse:
        """
        Option open interest change data for a specific underlying symbol.

        Args:
          date: Date to filter the OI change data. ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/api/options/oi_change/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"date": date}, options_open_interest_change_retrieve_params.OptionsOpenInterestChangeRetrieveParams
                ),
            ),
            cast_to=OptionsOpenInterestChangeRetrieveResponse,
        )


class AsyncOptionsOpenInterestChangesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptionsOpenInterestChangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsOpenInterestChangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsOpenInterestChangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOptionsOpenInterestChangesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptionsOpenInterestChangeRetrieveResponse:
        """
        Option open interest change data for a specific underlying symbol.

        Args:
          date: Date to filter the OI change data. ISO 8601 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/api/options/oi_change/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"date": date}, options_open_interest_change_retrieve_params.OptionsOpenInterestChangeRetrieveParams
                ),
            ),
            cast_to=OptionsOpenInterestChangeRetrieveResponse,
        )


class OptionsOpenInterestChangesResourceWithRawResponse:
    def __init__(self, options_open_interest_changes: OptionsOpenInterestChangesResource) -> None:
        self._options_open_interest_changes = options_open_interest_changes

        self.retrieve = to_raw_response_wrapper(
            options_open_interest_changes.retrieve,
        )


class AsyncOptionsOpenInterestChangesResourceWithRawResponse:
    def __init__(self, options_open_interest_changes: AsyncOptionsOpenInterestChangesResource) -> None:
        self._options_open_interest_changes = options_open_interest_changes

        self.retrieve = async_to_raw_response_wrapper(
            options_open_interest_changes.retrieve,
        )


class OptionsOpenInterestChangesResourceWithStreamingResponse:
    def __init__(self, options_open_interest_changes: OptionsOpenInterestChangesResource) -> None:
        self._options_open_interest_changes = options_open_interest_changes

        self.retrieve = to_streamed_response_wrapper(
            options_open_interest_changes.retrieve,
        )


class AsyncOptionsOpenInterestChangesResourceWithStreamingResponse:
    def __init__(self, options_open_interest_changes: AsyncOptionsOpenInterestChangesResource) -> None:
        self._options_open_interest_changes = options_open_interest_changes

        self.retrieve = async_to_streamed_response_wrapper(
            options_open_interest_changes.retrieve,
        )
