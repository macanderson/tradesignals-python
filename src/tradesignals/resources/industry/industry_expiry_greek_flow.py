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
from ...types.industry import industry_expiry_greek_flow_list_params
from ...types.industry.industry_expiry_greek_flow_list_response import IndustryExpiryGreekFlowListResponse

__all__ = ["IndustryExpiryGreekFlowResource", "AsyncIndustryExpiryGreekFlowResource"]


class IndustryExpiryGreekFlowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndustryExpiryGreekFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return IndustryExpiryGreekFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndustryExpiryGreekFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return IndustryExpiryGreekFlowResourceWithStreamingResponse(self)

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
    ) -> Optional[IndustryExpiryGreekFlowListResponse]:
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
                query=maybe_transform(
                    {"date": date}, industry_expiry_greek_flow_list_params.IndustryExpiryGreekFlowListParams
                ),
                post_parser=DataWrapper[Optional[IndustryExpiryGreekFlowListResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IndustryExpiryGreekFlowListResponse]], DataWrapper[IndustryExpiryGreekFlowListResponse]
            ),
        )


class AsyncIndustryExpiryGreekFlowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndustryExpiryGreekFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndustryExpiryGreekFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndustryExpiryGreekFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncIndustryExpiryGreekFlowResourceWithStreamingResponse(self)

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
    ) -> Optional[IndustryExpiryGreekFlowListResponse]:
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
                    {"date": date}, industry_expiry_greek_flow_list_params.IndustryExpiryGreekFlowListParams
                ),
                post_parser=DataWrapper[Optional[IndustryExpiryGreekFlowListResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IndustryExpiryGreekFlowListResponse]], DataWrapper[IndustryExpiryGreekFlowListResponse]
            ),
        )


class IndustryExpiryGreekFlowResourceWithRawResponse:
    def __init__(self, industry_expiry_greek_flow: IndustryExpiryGreekFlowResource) -> None:
        self._industry_expiry_greek_flow = industry_expiry_greek_flow

        self.list = to_raw_response_wrapper(
            industry_expiry_greek_flow.list,
        )


class AsyncIndustryExpiryGreekFlowResourceWithRawResponse:
    def __init__(self, industry_expiry_greek_flow: AsyncIndustryExpiryGreekFlowResource) -> None:
        self._industry_expiry_greek_flow = industry_expiry_greek_flow

        self.list = async_to_raw_response_wrapper(
            industry_expiry_greek_flow.list,
        )


class IndustryExpiryGreekFlowResourceWithStreamingResponse:
    def __init__(self, industry_expiry_greek_flow: IndustryExpiryGreekFlowResource) -> None:
        self._industry_expiry_greek_flow = industry_expiry_greek_flow

        self.list = to_streamed_response_wrapper(
            industry_expiry_greek_flow.list,
        )


class AsyncIndustryExpiryGreekFlowResourceWithStreamingResponse:
    def __init__(self, industry_expiry_greek_flow: AsyncIndustryExpiryGreekFlowResource) -> None:
        self._industry_expiry_greek_flow = industry_expiry_greek_flow

        self.list = async_to_streamed_response_wrapper(
            industry_expiry_greek_flow.list,
        )
