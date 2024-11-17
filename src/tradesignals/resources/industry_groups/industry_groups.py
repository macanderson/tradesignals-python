# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .greek_flows import (
    GreekFlowsResource,
    AsyncGreekFlowsResource,
    GreekFlowsResourceWithRawResponse,
    AsyncGreekFlowsResourceWithRawResponse,
    GreekFlowsResourceWithStreamingResponse,
    AsyncGreekFlowsResourceWithStreamingResponse,
)
from .greek_flows_by_expiry import (
    GreekFlowsByExpiryResource,
    AsyncGreekFlowsByExpiryResource,
    GreekFlowsByExpiryResourceWithRawResponse,
    AsyncGreekFlowsByExpiryResourceWithRawResponse,
    GreekFlowsByExpiryResourceWithStreamingResponse,
    AsyncGreekFlowsByExpiryResourceWithStreamingResponse,
)

__all__ = ["IndustryGroupsResource", "AsyncIndustryGroupsResource"]


class IndustryGroupsResource(SyncAPIResource):
    @cached_property
    def greek_flows(self) -> GreekFlowsResource:
        return GreekFlowsResource(self._client)

    @cached_property
    def greek_flows_by_expiry(self) -> GreekFlowsByExpiryResource:
        return GreekFlowsByExpiryResource(self._client)

    @cached_property
    def with_raw_response(self) -> IndustryGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return IndustryGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndustryGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return IndustryGroupsResourceWithStreamingResponse(self)


class AsyncIndustryGroupsResource(AsyncAPIResource):
    @cached_property
    def greek_flows(self) -> AsyncGreekFlowsResource:
        return AsyncGreekFlowsResource(self._client)

    @cached_property
    def greek_flows_by_expiry(self) -> AsyncGreekFlowsByExpiryResource:
        return AsyncGreekFlowsByExpiryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIndustryGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndustryGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndustryGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncIndustryGroupsResourceWithStreamingResponse(self)


class IndustryGroupsResourceWithRawResponse:
    def __init__(self, industry_groups: IndustryGroupsResource) -> None:
        self._industry_groups = industry_groups

    @cached_property
    def greek_flows(self) -> GreekFlowsResourceWithRawResponse:
        return GreekFlowsResourceWithRawResponse(self._industry_groups.greek_flows)

    @cached_property
    def greek_flows_by_expiry(self) -> GreekFlowsByExpiryResourceWithRawResponse:
        return GreekFlowsByExpiryResourceWithRawResponse(self._industry_groups.greek_flows_by_expiry)


class AsyncIndustryGroupsResourceWithRawResponse:
    def __init__(self, industry_groups: AsyncIndustryGroupsResource) -> None:
        self._industry_groups = industry_groups

    @cached_property
    def greek_flows(self) -> AsyncGreekFlowsResourceWithRawResponse:
        return AsyncGreekFlowsResourceWithRawResponse(self._industry_groups.greek_flows)

    @cached_property
    def greek_flows_by_expiry(self) -> AsyncGreekFlowsByExpiryResourceWithRawResponse:
        return AsyncGreekFlowsByExpiryResourceWithRawResponse(self._industry_groups.greek_flows_by_expiry)


class IndustryGroupsResourceWithStreamingResponse:
    def __init__(self, industry_groups: IndustryGroupsResource) -> None:
        self._industry_groups = industry_groups

    @cached_property
    def greek_flows(self) -> GreekFlowsResourceWithStreamingResponse:
        return GreekFlowsResourceWithStreamingResponse(self._industry_groups.greek_flows)

    @cached_property
    def greek_flows_by_expiry(self) -> GreekFlowsByExpiryResourceWithStreamingResponse:
        return GreekFlowsByExpiryResourceWithStreamingResponse(self._industry_groups.greek_flows_by_expiry)


class AsyncIndustryGroupsResourceWithStreamingResponse:
    def __init__(self, industry_groups: AsyncIndustryGroupsResource) -> None:
        self._industry_groups = industry_groups

    @cached_property
    def greek_flows(self) -> AsyncGreekFlowsResourceWithStreamingResponse:
        return AsyncGreekFlowsResourceWithStreamingResponse(self._industry_groups.greek_flows)

    @cached_property
    def greek_flows_by_expiry(self) -> AsyncGreekFlowsByExpiryResourceWithStreamingResponse:
        return AsyncGreekFlowsByExpiryResourceWithStreamingResponse(self._industry_groups.greek_flows_by_expiry)
