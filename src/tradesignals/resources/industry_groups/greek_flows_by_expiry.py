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
from ...types.industry_groups import greek_flows_by_expiry_list_params
from ...types.industry_groups.greek_flows_by_expiry_list_response import GreekFlowsByExpiryListResponse

__all__ = ["GreekFlowsByExpiryResource", "AsyncGreekFlowsByExpiryResource"]


class GreekFlowsByExpiryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GreekFlowsByExpiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return GreekFlowsByExpiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GreekFlowsByExpiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return GreekFlowsByExpiryResourceWithStreamingResponse(self)

    def list(
        self,
        expiry: Union[str, date],
        *,
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
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GreekFlowsByExpiryListResponse]:
        """
        Returns the group flow's Greek flow (delta & vega flow) for the given market day
        broken down per minute & expiry.

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
        if not expiry:
            raise ValueError(f"Expected a non-empty value for `expiry` but received {expiry!r}")
        return self._get(
            f"/api/group-flow/{flow_group}/greek-flow/{expiry}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, greek_flows_by_expiry_list_params.GreekFlowsByExpiryListParams),
                post_parser=DataWrapper[Optional[GreekFlowsByExpiryListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GreekFlowsByExpiryListResponse]], DataWrapper[GreekFlowsByExpiryListResponse]),
        )


class AsyncGreekFlowsByExpiryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGreekFlowsByExpiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGreekFlowsByExpiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGreekFlowsByExpiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncGreekFlowsByExpiryResourceWithStreamingResponse(self)

    async def list(
        self,
        expiry: Union[str, date],
        *,
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
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GreekFlowsByExpiryListResponse]:
        """
        Returns the group flow's Greek flow (delta & vega flow) for the given market day
        broken down per minute & expiry.

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
        if not expiry:
            raise ValueError(f"Expected a non-empty value for `expiry` but received {expiry!r}")
        return await self._get(
            f"/api/group-flow/{flow_group}/greek-flow/{expiry}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"date": date}, greek_flows_by_expiry_list_params.GreekFlowsByExpiryListParams
                ),
                post_parser=DataWrapper[Optional[GreekFlowsByExpiryListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GreekFlowsByExpiryListResponse]], DataWrapper[GreekFlowsByExpiryListResponse]),
        )


class GreekFlowsByExpiryResourceWithRawResponse:
    def __init__(self, greek_flows_by_expiry: GreekFlowsByExpiryResource) -> None:
        self._greek_flows_by_expiry = greek_flows_by_expiry

        self.list = to_raw_response_wrapper(
            greek_flows_by_expiry.list,
        )


class AsyncGreekFlowsByExpiryResourceWithRawResponse:
    def __init__(self, greek_flows_by_expiry: AsyncGreekFlowsByExpiryResource) -> None:
        self._greek_flows_by_expiry = greek_flows_by_expiry

        self.list = async_to_raw_response_wrapper(
            greek_flows_by_expiry.list,
        )


class GreekFlowsByExpiryResourceWithStreamingResponse:
    def __init__(self, greek_flows_by_expiry: GreekFlowsByExpiryResource) -> None:
        self._greek_flows_by_expiry = greek_flows_by_expiry

        self.list = to_streamed_response_wrapper(
            greek_flows_by_expiry.list,
        )


class AsyncGreekFlowsByExpiryResourceWithStreamingResponse:
    def __init__(self, greek_flows_by_expiry: AsyncGreekFlowsByExpiryResource) -> None:
        self._greek_flows_by_expiry = greek_flows_by_expiry

        self.list = async_to_streamed_response_wrapper(
            greek_flows_by_expiry.list,
        )
