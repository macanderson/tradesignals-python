# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ..._base_client import make_request_options
from ...types.institutions import institutional_activity_list_params
from ...types.institutions.institutional_activity_list_response import InstitutionalActivityListResponse

__all__ = ["InstitutionalActivitiesResource", "AsyncInstitutionalActivitiesResource"]


class InstitutionalActivitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstitutionalActivitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return InstitutionalActivitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstitutionalActivitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return InstitutionalActivitiesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        institution: str | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstitutionalActivityListResponse:
        """Retrieve data on institutional trading activity.

        Filter by optional symbol,
        date, and institution name.

        Args:
          date: Date to filter institutional activity.

          institution: Name of the institution.

          symbol: Stock symbol to filter institutional activity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/institutional/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "institution": institution,
                        "symbol": symbol,
                    },
                    institutional_activity_list_params.InstitutionalActivityListParams,
                ),
            ),
            cast_to=InstitutionalActivityListResponse,
        )


class AsyncInstitutionalActivitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstitutionalActivitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstitutionalActivitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstitutionalActivitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncInstitutionalActivitiesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        institution: str | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstitutionalActivityListResponse:
        """Retrieve data on institutional trading activity.

        Filter by optional symbol,
        date, and institution name.

        Args:
          date: Date to filter institutional activity.

          institution: Name of the institution.

          symbol: Stock symbol to filter institutional activity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/institutional/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "institution": institution,
                        "symbol": symbol,
                    },
                    institutional_activity_list_params.InstitutionalActivityListParams,
                ),
            ),
            cast_to=InstitutionalActivityListResponse,
        )


class InstitutionalActivitiesResourceWithRawResponse:
    def __init__(self, institutional_activities: InstitutionalActivitiesResource) -> None:
        self._institutional_activities = institutional_activities

        self.list = to_raw_response_wrapper(
            institutional_activities.list,
        )


class AsyncInstitutionalActivitiesResourceWithRawResponse:
    def __init__(self, institutional_activities: AsyncInstitutionalActivitiesResource) -> None:
        self._institutional_activities = institutional_activities

        self.list = async_to_raw_response_wrapper(
            institutional_activities.list,
        )


class InstitutionalActivitiesResourceWithStreamingResponse:
    def __init__(self, institutional_activities: InstitutionalActivitiesResource) -> None:
        self._institutional_activities = institutional_activities

        self.list = to_streamed_response_wrapper(
            institutional_activities.list,
        )


class AsyncInstitutionalActivitiesResourceWithStreamingResponse:
    def __init__(self, institutional_activities: AsyncInstitutionalActivitiesResource) -> None:
        self._institutional_activities = institutional_activities

        self.list = async_to_streamed_response_wrapper(
            institutional_activities.list,
        )
