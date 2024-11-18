# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.option_trades.flow_alert_list_response import FlowAlertListResponse

__all__ = ["FlowAlertsResource", "AsyncFlowAlertsResource"]


class FlowAlertsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FlowAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return FlowAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlowAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return FlowAlertsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FlowAlertListResponse]:
        """Returns the latest flow alerts."""
        return self._get(
            "/api/option-trades/flow-alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[FlowAlertListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FlowAlertListResponse]], DataWrapper[FlowAlertListResponse]),
        )


class AsyncFlowAlertsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFlowAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlowAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlowAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncFlowAlertsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FlowAlertListResponse]:
        """Returns the latest flow alerts."""
        return await self._get(
            "/api/option-trades/flow-alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Optional[FlowAlertListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FlowAlertListResponse]], DataWrapper[FlowAlertListResponse]),
        )


class FlowAlertsResourceWithRawResponse:
    def __init__(self, flow_alerts: FlowAlertsResource) -> None:
        self._flow_alerts = flow_alerts

        self.list = to_raw_response_wrapper(
            flow_alerts.list,
        )


class AsyncFlowAlertsResourceWithRawResponse:
    def __init__(self, flow_alerts: AsyncFlowAlertsResource) -> None:
        self._flow_alerts = flow_alerts

        self.list = async_to_raw_response_wrapper(
            flow_alerts.list,
        )


class FlowAlertsResourceWithStreamingResponse:
    def __init__(self, flow_alerts: FlowAlertsResource) -> None:
        self._flow_alerts = flow_alerts

        self.list = to_streamed_response_wrapper(
            flow_alerts.list,
        )


class AsyncFlowAlertsResourceWithStreamingResponse:
    def __init__(self, flow_alerts: AsyncFlowAlertsResource) -> None:
        self._flow_alerts = flow_alerts

        self.list = async_to_streamed_response_wrapper(
            flow_alerts.list,
        )
