# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ..._wrappers import ChainsWrapper
from ..._base_client import make_request_options
from ...types.option_contracts import historic_data_retrieve_params
from ...types.option_contracts.historic_data_retrieve_response import HistoricDataRetrieveResponse

__all__ = ["HistoricDataResource", "AsyncHistoricDataResource"]


class HistoricDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoricDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return HistoricDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoricDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return HistoricDataResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HistoricDataRetrieveResponse]:
        """
        Returns historic data for the given option contract for each trading day.

        Args:
          limit: The number of items to return. Minimum is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/option-contract/{id}/historic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, historic_data_retrieve_params.HistoricDataRetrieveParams),
                post_parser=ChainsWrapper[Optional[HistoricDataRetrieveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HistoricDataRetrieveResponse]], ChainsWrapper[HistoricDataRetrieveResponse]),
        )


class AsyncHistoricDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoricDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHistoricDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoricDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncHistoricDataResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HistoricDataRetrieveResponse]:
        """
        Returns historic data for the given option contract for each trading day.

        Args:
          limit: The number of items to return. Minimum is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/option-contract/{id}/historic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, historic_data_retrieve_params.HistoricDataRetrieveParams
                ),
                post_parser=ChainsWrapper[Optional[HistoricDataRetrieveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HistoricDataRetrieveResponse]], ChainsWrapper[HistoricDataRetrieveResponse]),
        )


class HistoricDataResourceWithRawResponse:
    def __init__(self, historic_data: HistoricDataResource) -> None:
        self._historic_data = historic_data

        self.retrieve = to_raw_response_wrapper(
            historic_data.retrieve,
        )


class AsyncHistoricDataResourceWithRawResponse:
    def __init__(self, historic_data: AsyncHistoricDataResource) -> None:
        self._historic_data = historic_data

        self.retrieve = async_to_raw_response_wrapper(
            historic_data.retrieve,
        )


class HistoricDataResourceWithStreamingResponse:
    def __init__(self, historic_data: HistoricDataResource) -> None:
        self._historic_data = historic_data

        self.retrieve = to_streamed_response_wrapper(
            historic_data.retrieve,
        )


class AsyncHistoricDataResourceWithStreamingResponse:
    def __init__(self, historic_data: AsyncHistoricDataResource) -> None:
        self._historic_data = historic_data

        self.retrieve = async_to_streamed_response_wrapper(
            historic_data.retrieve,
        )
