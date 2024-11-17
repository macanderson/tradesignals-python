# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .flow_alerts import (
    FlowAlertsResource,
    AsyncFlowAlertsResource,
    FlowAlertsResourceWithRawResponse,
    AsyncFlowAlertsResourceWithRawResponse,
    FlowAlertsResourceWithStreamingResponse,
    AsyncFlowAlertsResourceWithStreamingResponse,
)

__all__ = ["OptionTradesResource", "AsyncOptionTradesResource"]


class OptionTradesResource(SyncAPIResource):
    @cached_property
    def flow_alerts(self) -> FlowAlertsResource:
        return FlowAlertsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OptionTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OptionTradesResourceWithStreamingResponse(self)


class AsyncOptionTradesResource(AsyncAPIResource):
    @cached_property
    def flow_alerts(self) -> AsyncFlowAlertsResource:
        return AsyncFlowAlertsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOptionTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOptionTradesResourceWithStreamingResponse(self)


class OptionTradesResourceWithRawResponse:
    def __init__(self, option_trades: OptionTradesResource) -> None:
        self._option_trades = option_trades

    @cached_property
    def flow_alerts(self) -> FlowAlertsResourceWithRawResponse:
        return FlowAlertsResourceWithRawResponse(self._option_trades.flow_alerts)


class AsyncOptionTradesResourceWithRawResponse:
    def __init__(self, option_trades: AsyncOptionTradesResource) -> None:
        self._option_trades = option_trades

    @cached_property
    def flow_alerts(self) -> AsyncFlowAlertsResourceWithRawResponse:
        return AsyncFlowAlertsResourceWithRawResponse(self._option_trades.flow_alerts)


class OptionTradesResourceWithStreamingResponse:
    def __init__(self, option_trades: OptionTradesResource) -> None:
        self._option_trades = option_trades

    @cached_property
    def flow_alerts(self) -> FlowAlertsResourceWithStreamingResponse:
        return FlowAlertsResourceWithStreamingResponse(self._option_trades.flow_alerts)


class AsyncOptionTradesResourceWithStreamingResponse:
    def __init__(self, option_trades: AsyncOptionTradesResource) -> None:
        self._option_trades = option_trades

    @cached_property
    def flow_alerts(self) -> AsyncFlowAlertsResourceWithStreamingResponse:
        return AsyncFlowAlertsResourceWithStreamingResponse(self._option_trades.flow_alerts)
