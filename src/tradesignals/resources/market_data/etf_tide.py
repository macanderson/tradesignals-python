# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
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
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.market_data import etf_tide_list_params
from ...types.market_data.etf_tide_list_response import EtfTideListResponse

__all__ = ["EtfTideResource", "AsyncEtfTideResource"]


class EtfTideResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EtfTideResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return EtfTideResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EtfTideResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return EtfTideResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EtfTideListResponse]:
        """
        Returns ETF tide data for the given ETF ticker.

        Args:
          date: A trading date in the format of YYYY-MM-DD. Defaults to the last trading date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/market/{ticker}/etf-tide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, etf_tide_list_params.EtfTideListParams),
                post_parser=DataWrapper[Optional[EtfTideListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EtfTideListResponse]], DataWrapper[EtfTideListResponse]),
        )


class AsyncEtfTideResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEtfTideResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEtfTideResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEtfTideResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncEtfTideResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EtfTideListResponse]:
        """
        Returns ETF tide data for the given ETF ticker.

        Args:
          date: A trading date in the format of YYYY-MM-DD. Defaults to the last trading date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/market/{ticker}/etf-tide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"date": date}, etf_tide_list_params.EtfTideListParams),
                post_parser=DataWrapper[Optional[EtfTideListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[EtfTideListResponse]], DataWrapper[EtfTideListResponse]),
        )


class EtfTideResourceWithRawResponse:
    def __init__(self, etf_tide: EtfTideResource) -> None:
        self._etf_tide = etf_tide

        self.list = to_raw_response_wrapper(
            etf_tide.list,
        )


class AsyncEtfTideResourceWithRawResponse:
    def __init__(self, etf_tide: AsyncEtfTideResource) -> None:
        self._etf_tide = etf_tide

        self.list = async_to_raw_response_wrapper(
            etf_tide.list,
        )


class EtfTideResourceWithStreamingResponse:
    def __init__(self, etf_tide: EtfTideResource) -> None:
        self._etf_tide = etf_tide

        self.list = to_streamed_response_wrapper(
            etf_tide.list,
        )


class AsyncEtfTideResourceWithStreamingResponse:
    def __init__(self, etf_tide: AsyncEtfTideResource) -> None:
        self._etf_tide = etf_tide

        self.list = async_to_streamed_response_wrapper(
            etf_tide.list,
        )
