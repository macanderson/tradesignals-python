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
from ...types.stocks import financial_retrieve_params
from ...types.stocks.financial_retrieve_response import FinancialRetrieveResponse

__all__ = ["FinancialsResource", "AsyncFinancialsResource"]


class FinancialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FinancialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return FinancialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinancialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return FinancialsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        statement_type: Literal["income", "balance", "cashflow"],
        period: Literal["annual", "quarterly"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialRetrieveResponse:
        """Retrieve financial statements for a specific stock symbol.

        Filter by statement
        type.

        Args:
          statement_type: Type of financial statement ('income', 'balance', 'cashflow').

          period: Period type ('annual', 'quarterly').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/api/stocks/financials/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "statement_type": statement_type,
                        "period": period,
                    },
                    financial_retrieve_params.FinancialRetrieveParams,
                ),
            ),
            cast_to=FinancialRetrieveResponse,
        )


class AsyncFinancialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFinancialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFinancialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinancialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncFinancialsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        statement_type: Literal["income", "balance", "cashflow"],
        period: Literal["annual", "quarterly"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialRetrieveResponse:
        """Retrieve financial statements for a specific stock symbol.

        Filter by statement
        type.

        Args:
          statement_type: Type of financial statement ('income', 'balance', 'cashflow').

          period: Period type ('annual', 'quarterly').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/api/stocks/financials/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "statement_type": statement_type,
                        "period": period,
                    },
                    financial_retrieve_params.FinancialRetrieveParams,
                ),
            ),
            cast_to=FinancialRetrieveResponse,
        )


class FinancialsResourceWithRawResponse:
    def __init__(self, financials: FinancialsResource) -> None:
        self._financials = financials

        self.retrieve = to_raw_response_wrapper(
            financials.retrieve,
        )


class AsyncFinancialsResourceWithRawResponse:
    def __init__(self, financials: AsyncFinancialsResource) -> None:
        self._financials = financials

        self.retrieve = async_to_raw_response_wrapper(
            financials.retrieve,
        )


class FinancialsResourceWithStreamingResponse:
    def __init__(self, financials: FinancialsResource) -> None:
        self._financials = financials

        self.retrieve = to_streamed_response_wrapper(
            financials.retrieve,
        )


class AsyncFinancialsResourceWithStreamingResponse:
    def __init__(self, financials: AsyncFinancialsResource) -> None:
        self._financials = financials

        self.retrieve = async_to_streamed_response_wrapper(
            financials.retrieve,
        )
