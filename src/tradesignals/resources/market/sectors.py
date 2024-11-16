# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import make_request_options
from ...types.market import sector_list_params
from ...types.market.sector_list_response import SectorListResponse

__all__ = ["SectorsResource", "AsyncSectorsResource"]


class SectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return SectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return SectorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        time_frame: Literal["daily", "weekly", "monthly", "yearly"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SectorListResponse:
        """Retrieve performance data for market sectors.

        Filter by optional time frame.

        Args:
          time_frame: Time frame for sector performance (e.g., 'daily', 'weekly').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/market/sectors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"time_frame": time_frame}, sector_list_params.SectorListParams),
            ),
            cast_to=SectorListResponse,
        )


class AsyncSectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncSectorsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        time_frame: Literal["daily", "weekly", "monthly", "yearly"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SectorListResponse:
        """Retrieve performance data for market sectors.

        Filter by optional time frame.

        Args:
          time_frame: Time frame for sector performance (e.g., 'daily', 'weekly').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/market/sectors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"time_frame": time_frame}, sector_list_params.SectorListParams),
            ),
            cast_to=SectorListResponse,
        )


class SectorsResourceWithRawResponse:
    def __init__(self, sectors: SectorsResource) -> None:
        self._sectors = sectors

        self.list = to_raw_response_wrapper(
            sectors.list,
        )


class AsyncSectorsResourceWithRawResponse:
    def __init__(self, sectors: AsyncSectorsResource) -> None:
        self._sectors = sectors

        self.list = async_to_raw_response_wrapper(
            sectors.list,
        )


class SectorsResourceWithStreamingResponse:
    def __init__(self, sectors: SectorsResource) -> None:
        self._sectors = sectors

        self.list = to_streamed_response_wrapper(
            sectors.list,
        )


class AsyncSectorsResourceWithStreamingResponse:
    def __init__(self, sectors: AsyncSectorsResource) -> None:
        self._sectors = sectors

        self.list = async_to_streamed_response_wrapper(
            sectors.list,
        )
