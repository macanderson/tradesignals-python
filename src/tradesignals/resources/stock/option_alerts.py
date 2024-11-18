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
from ..._wrappers import DataWrapper
from ...types.stock import option_alert_list_params
from ..._base_client import make_request_options
from ...types.stock.option_alert_list_response import OptionAlertListResponse

__all__ = ["OptionAlertsResource", "AsyncOptionAlertsResource"]


class OptionAlertsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OptionAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return OptionAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return OptionAlertsResourceWithStreamingResponse(self)

    def list(
        self,
        ticker: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OptionAlertListResponse]:
        """
        Returns the latest option alerts for the given ticker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return self._get(
            f"/api/stock/{ticker}/flow-alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, option_alert_list_params.OptionAlertListParams),
                post_parser=DataWrapper[Optional[OptionAlertListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OptionAlertListResponse]], DataWrapper[OptionAlertListResponse]),
        )


class AsyncOptionAlertsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOptionAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncOptionAlertsResourceWithStreamingResponse(self)

    async def list(
        self,
        ticker: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OptionAlertListResponse]:
        """
        Returns the latest option alerts for the given ticker.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ticker:
            raise ValueError(f"Expected a non-empty value for `ticker` but received {ticker!r}")
        return await self._get(
            f"/api/stock/{ticker}/flow-alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, option_alert_list_params.OptionAlertListParams),
                post_parser=DataWrapper[Optional[OptionAlertListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OptionAlertListResponse]], DataWrapper[OptionAlertListResponse]),
        )


class OptionAlertsResourceWithRawResponse:
    def __init__(self, option_alerts: OptionAlertsResource) -> None:
        self._option_alerts = option_alerts

        self.list = to_raw_response_wrapper(
            option_alerts.list,
        )


class AsyncOptionAlertsResourceWithRawResponse:
    def __init__(self, option_alerts: AsyncOptionAlertsResource) -> None:
        self._option_alerts = option_alerts

        self.list = async_to_raw_response_wrapper(
            option_alerts.list,
        )


class OptionAlertsResourceWithStreamingResponse:
    def __init__(self, option_alerts: OptionAlertsResource) -> None:
        self._option_alerts = option_alerts

        self.list = to_streamed_response_wrapper(
            option_alerts.list,
        )


class AsyncOptionAlertsResourceWithStreamingResponse:
    def __init__(self, option_alerts: AsyncOptionAlertsResource) -> None:
        self._option_alerts = option_alerts

        self.list = async_to_streamed_response_wrapper(
            option_alerts.list,
        )
