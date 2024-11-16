# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .price import (
    PriceResource,
    AsyncPriceResource,
    PriceResourceWithRawResponse,
    AsyncPriceResourceWithRawResponse,
    PriceResourceWithStreamingResponse,
    AsyncPriceResourceWithStreamingResponse,
)
from .quote import (
    QuoteResource,
    AsyncQuoteResource,
    QuoteResourceWithRawResponse,
    AsyncQuoteResourceWithRawResponse,
    QuoteResourceWithStreamingResponse,
    AsyncQuoteResourceWithStreamingResponse,
)
from .company import (
    CompanyResource,
    AsyncCompanyResource,
    CompanyResourceWithRawResponse,
    AsyncCompanyResourceWithRawResponse,
    CompanyResourceWithStreamingResponse,
    AsyncCompanyResourceWithStreamingResponse,
)
from .earnings import (
    EarningsResource,
    AsyncEarningsResource,
    EarningsResourceWithRawResponse,
    AsyncEarningsResourceWithRawResponse,
    EarningsResourceWithStreamingResponse,
    AsyncEarningsResourceWithStreamingResponse,
)
from .screener import (
    ScreenerResource,
    AsyncScreenerResource,
    ScreenerResourceWithRawResponse,
    AsyncScreenerResourceWithRawResponse,
    ScreenerResourceWithStreamingResponse,
    AsyncScreenerResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .dividends import (
    DividendsResource,
    AsyncDividendsResource,
    DividendsResourceWithRawResponse,
    AsyncDividendsResourceWithRawResponse,
    DividendsResourceWithStreamingResponse,
    AsyncDividendsResourceWithStreamingResponse,
)
from .financials import (
    FinancialsResource,
    AsyncFinancialsResource,
    FinancialsResourceWithRawResponse,
    AsyncFinancialsResourceWithRawResponse,
    FinancialsResourceWithStreamingResponse,
    AsyncFinancialsResourceWithStreamingResponse,
)
from .historical import (
    HistoricalResource,
    AsyncHistoricalResource,
    HistoricalResourceWithRawResponse,
    AsyncHistoricalResourceWithRawResponse,
    HistoricalResourceWithStreamingResponse,
    AsyncHistoricalResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["StocksResource", "AsyncStocksResource"]


class StocksResource(SyncAPIResource):
    @cached_property
    def price(self) -> PriceResource:
        return PriceResource(self._client)

    @cached_property
    def quote(self) -> QuoteResource:
        return QuoteResource(self._client)

    @cached_property
    def historical(self) -> HistoricalResource:
        return HistoricalResource(self._client)

    @cached_property
    def company(self) -> CompanyResource:
        return CompanyResource(self._client)

    @cached_property
    def financials(self) -> FinancialsResource:
        return FinancialsResource(self._client)

    @cached_property
    def earnings(self) -> EarningsResource:
        return EarningsResource(self._client)

    @cached_property
    def dividends(self) -> DividendsResource:
        return DividendsResource(self._client)

    @cached_property
    def screener(self) -> ScreenerResource:
        return ScreenerResource(self._client)

    @cached_property
    def with_raw_response(self) -> StocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return StocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return StocksResourceWithStreamingResponse(self)


class AsyncStocksResource(AsyncAPIResource):
    @cached_property
    def price(self) -> AsyncPriceResource:
        return AsyncPriceResource(self._client)

    @cached_property
    def quote(self) -> AsyncQuoteResource:
        return AsyncQuoteResource(self._client)

    @cached_property
    def historical(self) -> AsyncHistoricalResource:
        return AsyncHistoricalResource(self._client)

    @cached_property
    def company(self) -> AsyncCompanyResource:
        return AsyncCompanyResource(self._client)

    @cached_property
    def financials(self) -> AsyncFinancialsResource:
        return AsyncFinancialsResource(self._client)

    @cached_property
    def earnings(self) -> AsyncEarningsResource:
        return AsyncEarningsResource(self._client)

    @cached_property
    def dividends(self) -> AsyncDividendsResource:
        return AsyncDividendsResource(self._client)

    @cached_property
    def screener(self) -> AsyncScreenerResource:
        return AsyncScreenerResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/tradesignals-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/tradesignals-python#with_streaming_response
        """
        return AsyncStocksResourceWithStreamingResponse(self)


class StocksResourceWithRawResponse:
    def __init__(self, stocks: StocksResource) -> None:
        self._stocks = stocks

    @cached_property
    def price(self) -> PriceResourceWithRawResponse:
        return PriceResourceWithRawResponse(self._stocks.price)

    @cached_property
    def quote(self) -> QuoteResourceWithRawResponse:
        return QuoteResourceWithRawResponse(self._stocks.quote)

    @cached_property
    def historical(self) -> HistoricalResourceWithRawResponse:
        return HistoricalResourceWithRawResponse(self._stocks.historical)

    @cached_property
    def company(self) -> CompanyResourceWithRawResponse:
        return CompanyResourceWithRawResponse(self._stocks.company)

    @cached_property
    def financials(self) -> FinancialsResourceWithRawResponse:
        return FinancialsResourceWithRawResponse(self._stocks.financials)

    @cached_property
    def earnings(self) -> EarningsResourceWithRawResponse:
        return EarningsResourceWithRawResponse(self._stocks.earnings)

    @cached_property
    def dividends(self) -> DividendsResourceWithRawResponse:
        return DividendsResourceWithRawResponse(self._stocks.dividends)

    @cached_property
    def screener(self) -> ScreenerResourceWithRawResponse:
        return ScreenerResourceWithRawResponse(self._stocks.screener)


class AsyncStocksResourceWithRawResponse:
    def __init__(self, stocks: AsyncStocksResource) -> None:
        self._stocks = stocks

    @cached_property
    def price(self) -> AsyncPriceResourceWithRawResponse:
        return AsyncPriceResourceWithRawResponse(self._stocks.price)

    @cached_property
    def quote(self) -> AsyncQuoteResourceWithRawResponse:
        return AsyncQuoteResourceWithRawResponse(self._stocks.quote)

    @cached_property
    def historical(self) -> AsyncHistoricalResourceWithRawResponse:
        return AsyncHistoricalResourceWithRawResponse(self._stocks.historical)

    @cached_property
    def company(self) -> AsyncCompanyResourceWithRawResponse:
        return AsyncCompanyResourceWithRawResponse(self._stocks.company)

    @cached_property
    def financials(self) -> AsyncFinancialsResourceWithRawResponse:
        return AsyncFinancialsResourceWithRawResponse(self._stocks.financials)

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithRawResponse:
        return AsyncEarningsResourceWithRawResponse(self._stocks.earnings)

    @cached_property
    def dividends(self) -> AsyncDividendsResourceWithRawResponse:
        return AsyncDividendsResourceWithRawResponse(self._stocks.dividends)

    @cached_property
    def screener(self) -> AsyncScreenerResourceWithRawResponse:
        return AsyncScreenerResourceWithRawResponse(self._stocks.screener)


class StocksResourceWithStreamingResponse:
    def __init__(self, stocks: StocksResource) -> None:
        self._stocks = stocks

    @cached_property
    def price(self) -> PriceResourceWithStreamingResponse:
        return PriceResourceWithStreamingResponse(self._stocks.price)

    @cached_property
    def quote(self) -> QuoteResourceWithStreamingResponse:
        return QuoteResourceWithStreamingResponse(self._stocks.quote)

    @cached_property
    def historical(self) -> HistoricalResourceWithStreamingResponse:
        return HistoricalResourceWithStreamingResponse(self._stocks.historical)

    @cached_property
    def company(self) -> CompanyResourceWithStreamingResponse:
        return CompanyResourceWithStreamingResponse(self._stocks.company)

    @cached_property
    def financials(self) -> FinancialsResourceWithStreamingResponse:
        return FinancialsResourceWithStreamingResponse(self._stocks.financials)

    @cached_property
    def earnings(self) -> EarningsResourceWithStreamingResponse:
        return EarningsResourceWithStreamingResponse(self._stocks.earnings)

    @cached_property
    def dividends(self) -> DividendsResourceWithStreamingResponse:
        return DividendsResourceWithStreamingResponse(self._stocks.dividends)

    @cached_property
    def screener(self) -> ScreenerResourceWithStreamingResponse:
        return ScreenerResourceWithStreamingResponse(self._stocks.screener)


class AsyncStocksResourceWithStreamingResponse:
    def __init__(self, stocks: AsyncStocksResource) -> None:
        self._stocks = stocks

    @cached_property
    def price(self) -> AsyncPriceResourceWithStreamingResponse:
        return AsyncPriceResourceWithStreamingResponse(self._stocks.price)

    @cached_property
    def quote(self) -> AsyncQuoteResourceWithStreamingResponse:
        return AsyncQuoteResourceWithStreamingResponse(self._stocks.quote)

    @cached_property
    def historical(self) -> AsyncHistoricalResourceWithStreamingResponse:
        return AsyncHistoricalResourceWithStreamingResponse(self._stocks.historical)

    @cached_property
    def company(self) -> AsyncCompanyResourceWithStreamingResponse:
        return AsyncCompanyResourceWithStreamingResponse(self._stocks.company)

    @cached_property
    def financials(self) -> AsyncFinancialsResourceWithStreamingResponse:
        return AsyncFinancialsResourceWithStreamingResponse(self._stocks.financials)

    @cached_property
    def earnings(self) -> AsyncEarningsResourceWithStreamingResponse:
        return AsyncEarningsResourceWithStreamingResponse(self._stocks.earnings)

    @cached_property
    def dividends(self) -> AsyncDividendsResourceWithStreamingResponse:
        return AsyncDividendsResourceWithStreamingResponse(self._stocks.dividends)

    @cached_property
    def screener(self) -> AsyncScreenerResourceWithStreamingResponse:
        return AsyncScreenerResourceWithStreamingResponse(self._stocks.screener)
