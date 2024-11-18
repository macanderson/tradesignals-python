# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .greek_flow import (
    GreekFlowResource,
    AsyncGreekFlowResource,
    GreekFlowResourceWithRawResponse,
    AsyncGreekFlowResourceWithRawResponse,
    GreekFlowResourceWithStreamingResponse,
    AsyncGreekFlowResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .greek_flow_by_expiry import (
    GreekFlowByExpiryResource,
    AsyncGreekFlowByExpiryResource,
    GreekFlowByExpiryResourceWithRawResponse,
    AsyncGreekFlowByExpiryResourceWithRawResponse,
    GreekFlowByExpiryResourceWithStreamingResponse,
    AsyncGreekFlowByExpiryResourceWithStreamingResponse,
)

__all__ = ["IndustryGroupResource", "AsyncIndustryGroupResource"]


class IndustryGroupResource(SyncAPIResource):
    @cached_property
    def greek_flow(self) -> GreekFlowResource:
        return GreekFlowResource(self._client)

    @cached_property
    def greek_flow_by_expiry(self) -> GreekFlowByExpiryResource:
        return GreekFlowByExpiryResource(self._client)

    @cached_property
    def with_raw_response(self) -> IndustryGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return IndustryGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndustryGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return IndustryGroupResourceWithStreamingResponse(self)


class AsyncIndustryGroupResource(AsyncAPIResource):
    @cached_property
    def greek_flow(self) -> AsyncGreekFlowResource:
        return AsyncGreekFlowResource(self._client)

    @cached_property
    def greek_flow_by_expiry(self) -> AsyncGreekFlowByExpiryResource:
        return AsyncGreekFlowByExpiryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIndustryGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndustryGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndustryGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncIndustryGroupResourceWithStreamingResponse(self)


class IndustryGroupResourceWithRawResponse:
    def __init__(self, industry_group: IndustryGroupResource) -> None:
        self._industry_group = industry_group

    @cached_property
    def greek_flow(self) -> GreekFlowResourceWithRawResponse:
        return GreekFlowResourceWithRawResponse(self._industry_group.greek_flow)

    @cached_property
    def greek_flow_by_expiry(self) -> GreekFlowByExpiryResourceWithRawResponse:
        return GreekFlowByExpiryResourceWithRawResponse(self._industry_group.greek_flow_by_expiry)


class AsyncIndustryGroupResourceWithRawResponse:
    def __init__(self, industry_group: AsyncIndustryGroupResource) -> None:
        self._industry_group = industry_group

    @cached_property
    def greek_flow(self) -> AsyncGreekFlowResourceWithRawResponse:
        return AsyncGreekFlowResourceWithRawResponse(self._industry_group.greek_flow)

    @cached_property
    def greek_flow_by_expiry(self) -> AsyncGreekFlowByExpiryResourceWithRawResponse:
        return AsyncGreekFlowByExpiryResourceWithRawResponse(self._industry_group.greek_flow_by_expiry)


class IndustryGroupResourceWithStreamingResponse:
    def __init__(self, industry_group: IndustryGroupResource) -> None:
        self._industry_group = industry_group

    @cached_property
    def greek_flow(self) -> GreekFlowResourceWithStreamingResponse:
        return GreekFlowResourceWithStreamingResponse(self._industry_group.greek_flow)

    @cached_property
    def greek_flow_by_expiry(self) -> GreekFlowByExpiryResourceWithStreamingResponse:
        return GreekFlowByExpiryResourceWithStreamingResponse(self._industry_group.greek_flow_by_expiry)


class AsyncIndustryGroupResourceWithStreamingResponse:
    def __init__(self, industry_group: AsyncIndustryGroupResource) -> None:
        self._industry_group = industry_group

    @cached_property
    def greek_flow(self) -> AsyncGreekFlowResourceWithStreamingResponse:
        return AsyncGreekFlowResourceWithStreamingResponse(self._industry_group.greek_flow)

    @cached_property
    def greek_flow_by_expiry(self) -> AsyncGreekFlowByExpiryResourceWithStreamingResponse:
        return AsyncGreekFlowByExpiryResourceWithStreamingResponse(self._industry_group.greek_flow_by_expiry)
