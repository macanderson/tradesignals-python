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
from ...types.industry import greek_flow_list_params
from ...types.industry.greek_flow_list_response import GreekFlowListResponse

__all__ = ["GreekFlowResource", "AsyncGreekFlowResource"]


class GreekFlowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GreekFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return GreekFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GreekFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return GreekFlowResourceWithStreamingResponse(self)

    def list(
        self,
        flow_group: Literal[
            "airline",
            "bank",
            "basic materials",
            "china",
            "communication services",
            "consumer cyclical",
            "consumer defensive",
            "crypto",
            "cyber",
            "energy",
            "financial services",
            "gas",
            "gold",
            "healthcare",
            "industrials",
            "mag7",
            "oil",
            "real estate",
            "refiners",
            "reit",
            "semi",
            "silver",
            "technology",
            "uranium",
            "utilities",
        ],
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GreekFlowListResponse]:
        """
        Returns the group flow's greek flow (delta & vega flow) for the given market day
        broken down per minute.

        Args:
          date: A trading date in the format of YYYY-MM-DD. This is optional and by default the
              last trading date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_group:
            raise ValueError(f"Expected a non-empty value for `flow_group` but received {flow_group!r}")
        return self._get(
            f"/api/group-flow/{flow_group}/greek-flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, greek_flow_list_params.GreekFlowListParams),
                post_parser=DataWrapper[Optional[GreekFlowListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GreekFlowListResponse]], DataWrapper[GreekFlowListResponse]),
        )


class AsyncGreekFlowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGreekFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGreekFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGreekFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncGreekFlowResourceWithStreamingResponse(self)

    async def list(
        self,
        flow_group: Literal[
            "airline",
            "bank",
            "basic materials",
            "china",
            "communication services",
            "consumer cyclical",
            "consumer defensive",
            "crypto",
            "cyber",
            "energy",
            "financial services",
            "gas",
            "gold",
            "healthcare",
            "industrials",
            "mag7",
            "oil",
            "real estate",
            "refiners",
            "reit",
            "semi",
            "silver",
            "technology",
            "uranium",
            "utilities",
        ],
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GreekFlowListResponse]:
        """
        Returns the group flow's greek flow (delta & vega flow) for the given market day
        broken down per minute.

        Args:
          date: A trading date in the format of YYYY-MM-DD. This is optional and by default the
              last trading date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not flow_group:
            raise ValueError(f"Expected a non-empty value for `flow_group` but received {flow_group!r}")
        return await self._get(
            f"/api/group-flow/{flow_group}/greek-flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"date": date}, greek_flow_list_params.GreekFlowListParams),
                post_parser=DataWrapper[Optional[GreekFlowListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GreekFlowListResponse]], DataWrapper[GreekFlowListResponse]),
        )


class GreekFlowResourceWithRawResponse:
    def __init__(self, greek_flow: GreekFlowResource) -> None:
        self._greek_flow = greek_flow

        self.list = to_raw_response_wrapper(
            greek_flow.list,
        )


class AsyncGreekFlowResourceWithRawResponse:
    def __init__(self, greek_flow: AsyncGreekFlowResource) -> None:
        self._greek_flow = greek_flow

        self.list = async_to_raw_response_wrapper(
            greek_flow.list,
        )


class GreekFlowResourceWithStreamingResponse:
    def __init__(self, greek_flow: GreekFlowResource) -> None:
        self._greek_flow = greek_flow

        self.list = to_streamed_response_wrapper(
            greek_flow.list,
        )


class AsyncGreekFlowResourceWithStreamingResponse:
    def __init__(self, greek_flow: AsyncGreekFlowResource) -> None:
        self._greek_flow = greek_flow

        self.list = async_to_streamed_response_wrapper(
            greek_flow.list,
        )
