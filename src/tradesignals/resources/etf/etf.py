# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .tide import (
    TideResource,
    AsyncTideResource,
    TideResourceWithRawResponse,
    AsyncTideResourceWithRawResponse,
    TideResourceWithStreamingResponse,
    AsyncTideResourceWithStreamingResponse,
)
from .sectors import (
    SectorsResource,
    AsyncSectorsResource,
    SectorsResourceWithRawResponse,
    AsyncSectorsResourceWithRawResponse,
    SectorsResourceWithStreamingResponse,
    AsyncSectorsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .holdings import (
    HoldingsResource,
    AsyncHoldingsResource,
    HoldingsResourceWithRawResponse,
    AsyncHoldingsResourceWithRawResponse,
    HoldingsResourceWithStreamingResponse,
    AsyncHoldingsResourceWithStreamingResponse,
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
from ...types.etf_list_response import EtfListResponse

__all__ = ["EtfResource", "AsyncEtfResource"]


class EtfResource(SyncAPIResource):
    @cached_property
    def tide(self) -> TideResource:
        return TideResource(self._client)

    @cached_property
    def sectors(self) -> SectorsResource:
        return SectorsResource(self._client)

    @cached_property
    def holdings(self) -> HoldingsResource:
        return HoldingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EtfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return EtfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EtfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return EtfResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EtfListResponse:
        """Retrieve a list of ETFs available."""
        return self._get(
            "/api/etf/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EtfListResponse,
        )


class AsyncEtfResource(AsyncAPIResource):
    @cached_property
    def tide(self) -> AsyncTideResource:
        return AsyncTideResource(self._client)

    @cached_property
    def sectors(self) -> AsyncSectorsResource:
        return AsyncSectorsResource(self._client)

    @cached_property
    def holdings(self) -> AsyncHoldingsResource:
        return AsyncHoldingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEtfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEtfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEtfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncEtfResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EtfListResponse:
        """Retrieve a list of ETFs available."""
        return await self._get(
            "/api/etf/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EtfListResponse,
        )


class EtfResourceWithRawResponse:
    def __init__(self, etf: EtfResource) -> None:
        self._etf = etf

        self.list = to_raw_response_wrapper(
            etf.list,
        )

    @cached_property
    def tide(self) -> TideResourceWithRawResponse:
        return TideResourceWithRawResponse(self._etf.tide)

    @cached_property
    def sectors(self) -> SectorsResourceWithRawResponse:
        return SectorsResourceWithRawResponse(self._etf.sectors)

    @cached_property
    def holdings(self) -> HoldingsResourceWithRawResponse:
        return HoldingsResourceWithRawResponse(self._etf.holdings)


class AsyncEtfResourceWithRawResponse:
    def __init__(self, etf: AsyncEtfResource) -> None:
        self._etf = etf

        self.list = async_to_raw_response_wrapper(
            etf.list,
        )

    @cached_property
    def tide(self) -> AsyncTideResourceWithRawResponse:
        return AsyncTideResourceWithRawResponse(self._etf.tide)

    @cached_property
    def sectors(self) -> AsyncSectorsResourceWithRawResponse:
        return AsyncSectorsResourceWithRawResponse(self._etf.sectors)

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithRawResponse:
        return AsyncHoldingsResourceWithRawResponse(self._etf.holdings)


class EtfResourceWithStreamingResponse:
    def __init__(self, etf: EtfResource) -> None:
        self._etf = etf

        self.list = to_streamed_response_wrapper(
            etf.list,
        )

    @cached_property
    def tide(self) -> TideResourceWithStreamingResponse:
        return TideResourceWithStreamingResponse(self._etf.tide)

    @cached_property
    def sectors(self) -> SectorsResourceWithStreamingResponse:
        return SectorsResourceWithStreamingResponse(self._etf.sectors)

    @cached_property
    def holdings(self) -> HoldingsResourceWithStreamingResponse:
        return HoldingsResourceWithStreamingResponse(self._etf.holdings)


class AsyncEtfResourceWithStreamingResponse:
    def __init__(self, etf: AsyncEtfResource) -> None:
        self._etf = etf

        self.list = async_to_streamed_response_wrapper(
            etf.list,
        )

    @cached_property
    def tide(self) -> AsyncTideResourceWithStreamingResponse:
        return AsyncTideResourceWithStreamingResponse(self._etf.tide)

    @cached_property
    def sectors(self) -> AsyncSectorsResourceWithStreamingResponse:
        return AsyncSectorsResourceWithStreamingResponse(self._etf.sectors)

    @cached_property
    def holdings(self) -> AsyncHoldingsResourceWithStreamingResponse:
        return AsyncHoldingsResourceWithStreamingResponse(self._etf.holdings)
