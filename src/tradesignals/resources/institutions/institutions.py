# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .trades import (
    TradesResource,
    AsyncTradesResource,
    TradesResourceWithRawResponse,
    AsyncTradesResourceWithRawResponse,
    TradesResourceWithStreamingResponse,
    AsyncTradesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .institutional_activities import (
    InstitutionalActivitiesResource,
    AsyncInstitutionalActivitiesResource,
    InstitutionalActivitiesResourceWithRawResponse,
    AsyncInstitutionalActivitiesResourceWithRawResponse,
    InstitutionalActivitiesResourceWithStreamingResponse,
    AsyncInstitutionalActivitiesResourceWithStreamingResponse,
)
from ...types.institution_list_response import InstitutionListResponse

__all__ = ["InstitutionsResource", "AsyncInstitutionsResource"]


class InstitutionsResource(SyncAPIResource):
    @cached_property
    def trades(self) -> TradesResource:
        return TradesResource(self._client)

    @cached_property
    def institutional_activities(self) -> InstitutionalActivitiesResource:
        return InstitutionalActivitiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstitutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return InstitutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstitutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return InstitutionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstitutionListResponse:
        """Retrieve a list of institutions that have reported trades."""
        return self._get(
            "/api/institutions/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstitutionListResponse,
        )


class AsyncInstitutionsResource(AsyncAPIResource):
    @cached_property
    def trades(self) -> AsyncTradesResource:
        return AsyncTradesResource(self._client)

    @cached_property
    def institutional_activities(self) -> AsyncInstitutionalActivitiesResource:
        return AsyncInstitutionalActivitiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstitutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstitutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstitutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncInstitutionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstitutionListResponse:
        """Retrieve a list of institutions that have reported trades."""
        return await self._get(
            "/api/institutions/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstitutionListResponse,
        )


class InstitutionsResourceWithRawResponse:
    def __init__(self, institutions: InstitutionsResource) -> None:
        self._institutions = institutions

        self.list = to_raw_response_wrapper(
            institutions.list,
        )

    @cached_property
    def trades(self) -> TradesResourceWithRawResponse:
        return TradesResourceWithRawResponse(self._institutions.trades)

    @cached_property
    def institutional_activities(self) -> InstitutionalActivitiesResourceWithRawResponse:
        return InstitutionalActivitiesResourceWithRawResponse(self._institutions.institutional_activities)


class AsyncInstitutionsResourceWithRawResponse:
    def __init__(self, institutions: AsyncInstitutionsResource) -> None:
        self._institutions = institutions

        self.list = async_to_raw_response_wrapper(
            institutions.list,
        )

    @cached_property
    def trades(self) -> AsyncTradesResourceWithRawResponse:
        return AsyncTradesResourceWithRawResponse(self._institutions.trades)

    @cached_property
    def institutional_activities(self) -> AsyncInstitutionalActivitiesResourceWithRawResponse:
        return AsyncInstitutionalActivitiesResourceWithRawResponse(self._institutions.institutional_activities)


class InstitutionsResourceWithStreamingResponse:
    def __init__(self, institutions: InstitutionsResource) -> None:
        self._institutions = institutions

        self.list = to_streamed_response_wrapper(
            institutions.list,
        )

    @cached_property
    def trades(self) -> TradesResourceWithStreamingResponse:
        return TradesResourceWithStreamingResponse(self._institutions.trades)

    @cached_property
    def institutional_activities(self) -> InstitutionalActivitiesResourceWithStreamingResponse:
        return InstitutionalActivitiesResourceWithStreamingResponse(self._institutions.institutional_activities)


class AsyncInstitutionsResourceWithStreamingResponse:
    def __init__(self, institutions: AsyncInstitutionsResource) -> None:
        self._institutions = institutions

        self.list = async_to_streamed_response_wrapper(
            institutions.list,
        )

    @cached_property
    def trades(self) -> AsyncTradesResourceWithStreamingResponse:
        return AsyncTradesResourceWithStreamingResponse(self._institutions.trades)

    @cached_property
    def institutional_activities(self) -> AsyncInstitutionalActivitiesResourceWithStreamingResponse:
        return AsyncInstitutionalActivitiesResourceWithStreamingResponse(self._institutions.institutional_activities)
