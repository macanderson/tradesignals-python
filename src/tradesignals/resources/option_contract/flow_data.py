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
from ...types.option_contract import flow_data_retrieve_params
from ...types.option_contract.flow_data_retrieve_response import FlowDataRetrieveResponse

__all__ = ["FlowDataResource", "AsyncFlowDataResource"]


class FlowDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlowDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return FlowDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlowDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return FlowDataResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        min_premium: int | NotGiven = NOT_GIVEN,
        side: Literal["ALL", "ASK", "BID", "MID"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FlowDataRetrieveResponse]:
        """
        Returns the latest flows for the given option chain, with optional filtering by
        min premium or side.

        Args:
          date: A trading date in the format YYYY-MM-DD. Defaults to the last trading date.

          limit: The number of items to return. Minimum is 1.

          min_premium: The minimum premium requested trades should have. Defaults to 0.

          side: The side of a stock trade. Defaults to ALL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/option-contract/{id}/flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "min_premium": min_premium,
                        "side": side,
                    },
                    flow_data_retrieve_params.FlowDataRetrieveParams,
                ),
                post_parser=DataWrapper[Optional[FlowDataRetrieveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FlowDataRetrieveResponse]], DataWrapper[FlowDataRetrieveResponse]),
        )


class AsyncFlowDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlowDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlowDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlowDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncFlowDataResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        min_premium: int | NotGiven = NOT_GIVEN,
        side: Literal["ALL", "ASK", "BID", "MID"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FlowDataRetrieveResponse]:
        """
        Returns the latest flows for the given option chain, with optional filtering by
        min premium or side.

        Args:
          date: A trading date in the format YYYY-MM-DD. Defaults to the last trading date.

          limit: The number of items to return. Minimum is 1.

          min_premium: The minimum premium requested trades should have. Defaults to 0.

          side: The side of a stock trade. Defaults to ALL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/option-contract/{id}/flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "min_premium": min_premium,
                        "side": side,
                    },
                    flow_data_retrieve_params.FlowDataRetrieveParams,
                ),
                post_parser=DataWrapper[Optional[FlowDataRetrieveResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FlowDataRetrieveResponse]], DataWrapper[FlowDataRetrieveResponse]),
        )


class FlowDataResourceWithRawResponse:
    def __init__(self, flow_data: FlowDataResource) -> None:
        self._flow_data = flow_data

        self.retrieve = to_raw_response_wrapper(
            flow_data.retrieve,
        )


class AsyncFlowDataResourceWithRawResponse:
    def __init__(self, flow_data: AsyncFlowDataResource) -> None:
        self._flow_data = flow_data

        self.retrieve = async_to_raw_response_wrapper(
            flow_data.retrieve,
        )


class FlowDataResourceWithStreamingResponse:
    def __init__(self, flow_data: FlowDataResource) -> None:
        self._flow_data = flow_data

        self.retrieve = to_streamed_response_wrapper(
            flow_data.retrieve,
        )


class AsyncFlowDataResourceWithStreamingResponse:
    def __init__(self, flow_data: AsyncFlowDataResource) -> None:
        self._flow_data = flow_data

        self.retrieve = async_to_streamed_response_wrapper(
            flow_data.retrieve,
        )
