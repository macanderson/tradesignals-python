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
from ...types.option_contracts import option_expiration_data_list_params
from ...types.option_contracts.option_expiration_data_list_response import OptionExpirationDataListResponse

__all__ = ["OptionExpirationDataResource", "AsyncOptionExpirationDataResource"]


class OptionExpirationDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptionExpirationDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionExpirationDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionExpirationDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OptionExpirationDataResourceWithStreamingResponse(self)

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
    ) -> Optional[OptionExpirationDataListResponse]:
        """
        Returns all expirations for the given trading day for a ticker.

        Args:
          date: A trading date in the format YYYY-MM-DD. Defaults to the last trading date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/stock/{ticker}/expiry-breakdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"date": date}, option_expiration_data_list_params.OptionExpirationDataListParams
                ),
                post_parser=DataWrapper[Optional[OptionExpirationDataListResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OptionExpirationDataListResponse]], DataWrapper[OptionExpirationDataListResponse]
            ),
        )


class AsyncOptionExpirationDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptionExpirationDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionExpirationDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionExpirationDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOptionExpirationDataResourceWithStreamingResponse(self)

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
    ) -> Optional[OptionExpirationDataListResponse]:
        """
        Returns all expirations for the given trading day for a ticker.

        Args:
          date: A trading date in the format YYYY-MM-DD. Defaults to the last trading date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/stock/{ticker}/expiry-breakdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"date": date}, option_expiration_data_list_params.OptionExpirationDataListParams
                ),
                post_parser=DataWrapper[Optional[OptionExpirationDataListResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OptionExpirationDataListResponse]], DataWrapper[OptionExpirationDataListResponse]
            ),
        )


class OptionExpirationDataResourceWithRawResponse:
    def __init__(self, option_expiration_data: OptionExpirationDataResource) -> None:
        self._option_expiration_data = option_expiration_data

        self.list = to_raw_response_wrapper(
            option_expiration_data.list,
        )


class AsyncOptionExpirationDataResourceWithRawResponse:
    def __init__(self, option_expiration_data: AsyncOptionExpirationDataResource) -> None:
        self._option_expiration_data = option_expiration_data

        self.list = async_to_raw_response_wrapper(
            option_expiration_data.list,
        )


class OptionExpirationDataResourceWithStreamingResponse:
    def __init__(self, option_expiration_data: OptionExpirationDataResource) -> None:
        self._option_expiration_data = option_expiration_data

        self.list = to_streamed_response_wrapper(
            option_expiration_data.list,
        )


class AsyncOptionExpirationDataResourceWithStreamingResponse:
    def __init__(self, option_expiration_data: AsyncOptionExpirationDataResource) -> None:
        self._option_expiration_data = option_expiration_data

        self.list = async_to_streamed_response_wrapper(
            option_expiration_data.list,
        )
