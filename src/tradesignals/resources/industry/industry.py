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
from .industry_expiry_greek_flow import (
    IndustryExpiryGreekFlowResource,
    AsyncIndustryExpiryGreekFlowResource,
    IndustryExpiryGreekFlowResourceWithRawResponse,
    AsyncIndustryExpiryGreekFlowResourceWithRawResponse,
    IndustryExpiryGreekFlowResourceWithStreamingResponse,
    AsyncIndustryExpiryGreekFlowResourceWithStreamingResponse,
)

__all__ = ["IndustryResource", "AsyncIndustryResource"]


class IndustryResource(SyncAPIResource):
    @cached_property
    def greek_flow(self) -> GreekFlowResource:
        return GreekFlowResource(self._client)

    @cached_property
    def industry_expiry_greek_flow(self) -> IndustryExpiryGreekFlowResource:
        return IndustryExpiryGreekFlowResource(self._client)

    @cached_property
    def with_raw_response(self) -> IndustryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return IndustryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndustryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return IndustryResourceWithStreamingResponse(self)


class AsyncIndustryResource(AsyncAPIResource):
    @cached_property
    def greek_flow(self) -> AsyncGreekFlowResource:
        return AsyncGreekFlowResource(self._client)

    @cached_property
    def industry_expiry_greek_flow(self) -> AsyncIndustryExpiryGreekFlowResource:
        return AsyncIndustryExpiryGreekFlowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIndustryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndustryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndustryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncIndustryResourceWithStreamingResponse(self)


class IndustryResourceWithRawResponse:
    def __init__(self, industry: IndustryResource) -> None:
        self._industry = industry

    @cached_property
    def greek_flow(self) -> GreekFlowResourceWithRawResponse:
        return GreekFlowResourceWithRawResponse(self._industry.greek_flow)

    @cached_property
    def industry_expiry_greek_flow(self) -> IndustryExpiryGreekFlowResourceWithRawResponse:
        return IndustryExpiryGreekFlowResourceWithRawResponse(self._industry.industry_expiry_greek_flow)


class AsyncIndustryResourceWithRawResponse:
    def __init__(self, industry: AsyncIndustryResource) -> None:
        self._industry = industry

    @cached_property
    def greek_flow(self) -> AsyncGreekFlowResourceWithRawResponse:
        return AsyncGreekFlowResourceWithRawResponse(self._industry.greek_flow)

    @cached_property
    def industry_expiry_greek_flow(self) -> AsyncIndustryExpiryGreekFlowResourceWithRawResponse:
        return AsyncIndustryExpiryGreekFlowResourceWithRawResponse(self._industry.industry_expiry_greek_flow)


class IndustryResourceWithStreamingResponse:
    def __init__(self, industry: IndustryResource) -> None:
        self._industry = industry

    @cached_property
    def greek_flow(self) -> GreekFlowResourceWithStreamingResponse:
        return GreekFlowResourceWithStreamingResponse(self._industry.greek_flow)

    @cached_property
    def industry_expiry_greek_flow(self) -> IndustryExpiryGreekFlowResourceWithStreamingResponse:
        return IndustryExpiryGreekFlowResourceWithStreamingResponse(self._industry.industry_expiry_greek_flow)


class AsyncIndustryResourceWithStreamingResponse:
    def __init__(self, industry: AsyncIndustryResource) -> None:
        self._industry = industry

    @cached_property
    def greek_flow(self) -> AsyncGreekFlowResourceWithStreamingResponse:
        return AsyncGreekFlowResourceWithStreamingResponse(self._industry.greek_flow)

    @cached_property
    def industry_expiry_greek_flow(self) -> AsyncIndustryExpiryGreekFlowResourceWithStreamingResponse:
        return AsyncIndustryExpiryGreekFlowResourceWithStreamingResponse(self._industry.industry_expiry_greek_flow)
