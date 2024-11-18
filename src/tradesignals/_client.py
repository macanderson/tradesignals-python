# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TradesignalsError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Tradesignals",
    "AsyncTradesignals",
    "Client",
    "AsyncClient",
]


class Tradesignals(SyncAPIClient):
    stock: resources.StockResource
    analyst: resources.AnalystResource
    seasonality: resources.SeasonalityResource
    screener: resources.ScreenerResource
    option_trades: resources.OptionTradesResource
    option_contracts: resources.OptionContractsResource
    market_data: resources.MarketDataResource
    institution: resources.InstitutionResource
    earnings: resources.EarningsResource
    congress: resources.CongressResource
    industry: resources.IndustryResource
    etf: resources.EtfResource
    darkpool: resources.DarkpoolResource
    with_raw_response: TradesignalsWithRawResponse
    with_streaming_response: TradesignalsWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Tradesignals client instance.

        This automatically infers the `api_key` argument from the `TRADESIGNALS_TOKEN` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("TRADESIGNALS_TOKEN")
        if api_key is None:
            raise TradesignalsError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TRADESIGNALS_TOKEN environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("TRADESIGNALS_BASE_URL")
        if base_url is None:
            base_url = f"https://api.unusualwhales.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.stock = resources.StockResource(self)
        self.analyst = resources.AnalystResource(self)
        self.seasonality = resources.SeasonalityResource(self)
        self.screener = resources.ScreenerResource(self)
        self.option_trades = resources.OptionTradesResource(self)
        self.option_contracts = resources.OptionContractsResource(self)
        self.market_data = resources.MarketDataResource(self)
        self.institution = resources.InstitutionResource(self)
        self.earnings = resources.EarningsResource(self)
        self.congress = resources.CongressResource(self)
        self.industry = resources.IndustryResource(self)
        self.etf = resources.EtfResource(self)
        self.darkpool = resources.DarkpoolResource(self)
        self.with_raw_response = TradesignalsWithRawResponse(self)
        self.with_streaming_response = TradesignalsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "Accepts": "text/json, text",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTradesignals(AsyncAPIClient):
    stock: resources.AsyncStockResource
    analyst: resources.AsyncAnalystResource
    seasonality: resources.AsyncSeasonalityResource
    screener: resources.AsyncScreenerResource
    option_trades: resources.AsyncOptionTradesResource
    option_contracts: resources.AsyncOptionContractsResource
    market_data: resources.AsyncMarketDataResource
    institution: resources.AsyncInstitutionResource
    earnings: resources.AsyncEarningsResource
    congress: resources.AsyncCongressResource
    industry: resources.AsyncIndustryResource
    etf: resources.AsyncEtfResource
    darkpool: resources.AsyncDarkpoolResource
    with_raw_response: AsyncTradesignalsWithRawResponse
    with_streaming_response: AsyncTradesignalsWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async Tradesignals client instance.

        This automatically infers the `api_key` argument from the `TRADESIGNALS_TOKEN` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("TRADESIGNALS_TOKEN")
        if api_key is None:
            raise TradesignalsError(
                "The api_key client option must be set either by passing api_key to the client or by setting the TRADESIGNALS_TOKEN environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("TRADESIGNALS_BASE_URL")
        if base_url is None:
            base_url = f"https://api.unusualwhales.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.stock = resources.AsyncStockResource(self)
        self.analyst = resources.AsyncAnalystResource(self)
        self.seasonality = resources.AsyncSeasonalityResource(self)
        self.screener = resources.AsyncScreenerResource(self)
        self.option_trades = resources.AsyncOptionTradesResource(self)
        self.option_contracts = resources.AsyncOptionContractsResource(self)
        self.market_data = resources.AsyncMarketDataResource(self)
        self.institution = resources.AsyncInstitutionResource(self)
        self.earnings = resources.AsyncEarningsResource(self)
        self.congress = resources.AsyncCongressResource(self)
        self.industry = resources.AsyncIndustryResource(self)
        self.etf = resources.AsyncEtfResource(self)
        self.darkpool = resources.AsyncDarkpoolResource(self)
        self.with_raw_response = AsyncTradesignalsWithRawResponse(self)
        self.with_streaming_response = AsyncTradesignalsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "Accepts": "text/json, text",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TradesignalsWithRawResponse:
    def __init__(self, client: Tradesignals) -> None:
        self.stock = resources.StockResourceWithRawResponse(client.stock)
        self.analyst = resources.AnalystResourceWithRawResponse(client.analyst)
        self.seasonality = resources.SeasonalityResourceWithRawResponse(client.seasonality)
        self.screener = resources.ScreenerResourceWithRawResponse(client.screener)
        self.option_trades = resources.OptionTradesResourceWithRawResponse(client.option_trades)
        self.option_contracts = resources.OptionContractsResourceWithRawResponse(client.option_contracts)
        self.market_data = resources.MarketDataResourceWithRawResponse(client.market_data)
        self.institution = resources.InstitutionResourceWithRawResponse(client.institution)
        self.earnings = resources.EarningsResourceWithRawResponse(client.earnings)
        self.congress = resources.CongressResourceWithRawResponse(client.congress)
        self.industry = resources.IndustryResourceWithRawResponse(client.industry)
        self.etf = resources.EtfResourceWithRawResponse(client.etf)
        self.darkpool = resources.DarkpoolResourceWithRawResponse(client.darkpool)


class AsyncTradesignalsWithRawResponse:
    def __init__(self, client: AsyncTradesignals) -> None:
        self.stock = resources.AsyncStockResourceWithRawResponse(client.stock)
        self.analyst = resources.AsyncAnalystResourceWithRawResponse(client.analyst)
        self.seasonality = resources.AsyncSeasonalityResourceWithRawResponse(client.seasonality)
        self.screener = resources.AsyncScreenerResourceWithRawResponse(client.screener)
        self.option_trades = resources.AsyncOptionTradesResourceWithRawResponse(client.option_trades)
        self.option_contracts = resources.AsyncOptionContractsResourceWithRawResponse(client.option_contracts)
        self.market_data = resources.AsyncMarketDataResourceWithRawResponse(client.market_data)
        self.institution = resources.AsyncInstitutionResourceWithRawResponse(client.institution)
        self.earnings = resources.AsyncEarningsResourceWithRawResponse(client.earnings)
        self.congress = resources.AsyncCongressResourceWithRawResponse(client.congress)
        self.industry = resources.AsyncIndustryResourceWithRawResponse(client.industry)
        self.etf = resources.AsyncEtfResourceWithRawResponse(client.etf)
        self.darkpool = resources.AsyncDarkpoolResourceWithRawResponse(client.darkpool)


class TradesignalsWithStreamedResponse:
    def __init__(self, client: Tradesignals) -> None:
        self.stock = resources.StockResourceWithStreamingResponse(client.stock)
        self.analyst = resources.AnalystResourceWithStreamingResponse(client.analyst)
        self.seasonality = resources.SeasonalityResourceWithStreamingResponse(client.seasonality)
        self.screener = resources.ScreenerResourceWithStreamingResponse(client.screener)
        self.option_trades = resources.OptionTradesResourceWithStreamingResponse(client.option_trades)
        self.option_contracts = resources.OptionContractsResourceWithStreamingResponse(client.option_contracts)
        self.market_data = resources.MarketDataResourceWithStreamingResponse(client.market_data)
        self.institution = resources.InstitutionResourceWithStreamingResponse(client.institution)
        self.earnings = resources.EarningsResourceWithStreamingResponse(client.earnings)
        self.congress = resources.CongressResourceWithStreamingResponse(client.congress)
        self.industry = resources.IndustryResourceWithStreamingResponse(client.industry)
        self.etf = resources.EtfResourceWithStreamingResponse(client.etf)
        self.darkpool = resources.DarkpoolResourceWithStreamingResponse(client.darkpool)


class AsyncTradesignalsWithStreamedResponse:
    def __init__(self, client: AsyncTradesignals) -> None:
        self.stock = resources.AsyncStockResourceWithStreamingResponse(client.stock)
        self.analyst = resources.AsyncAnalystResourceWithStreamingResponse(client.analyst)
        self.seasonality = resources.AsyncSeasonalityResourceWithStreamingResponse(client.seasonality)
        self.screener = resources.AsyncScreenerResourceWithStreamingResponse(client.screener)
        self.option_trades = resources.AsyncOptionTradesResourceWithStreamingResponse(client.option_trades)
        self.option_contracts = resources.AsyncOptionContractsResourceWithStreamingResponse(client.option_contracts)
        self.market_data = resources.AsyncMarketDataResourceWithStreamingResponse(client.market_data)
        self.institution = resources.AsyncInstitutionResourceWithStreamingResponse(client.institution)
        self.earnings = resources.AsyncEarningsResourceWithStreamingResponse(client.earnings)
        self.congress = resources.AsyncCongressResourceWithStreamingResponse(client.congress)
        self.industry = resources.AsyncIndustryResourceWithStreamingResponse(client.industry)
        self.etf = resources.AsyncEtfResourceWithStreamingResponse(client.etf)
        self.darkpool = resources.AsyncDarkpoolResourceWithStreamingResponse(client.darkpool)


Client = Tradesignals

AsyncClient = AsyncTradesignals
