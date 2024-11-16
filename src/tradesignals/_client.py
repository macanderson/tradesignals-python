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
    spike_detections: resources.SpikeDetectionsResource
    economic_calendars: resources.EconomicCalendarsResource
    etf: resources.EtfResource
    options: resources.OptionsResource
    stocks: resources.StocksResource
    news: resources.NewsResource
    insider_trades: resources.InsiderTradesResource
    institutions: resources.InstitutionsResource
    darkpool: resources.DarkpoolResource
    seasonality: resources.SeasonalityResource
    analyst: resources.AnalystResource
    market: resources.MarketResource
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
        """Construct a new synchronous tradesignals client instance.

        This automatically infers the `api_key` argument from the `UNUSUALWHALES_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("UNUSUALWHALES_API_KEY")
        if api_key is None:
            raise TradesignalsError(
                "The api_key client option must be set either by passing api_key to the client or by setting the UNUSUALWHALES_API_KEY environment variable"
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

        self.spike_detections = resources.SpikeDetectionsResource(self)
        self.economic_calendars = resources.EconomicCalendarsResource(self)
        self.etf = resources.EtfResource(self)
        self.options = resources.OptionsResource(self)
        self.stocks = resources.StocksResource(self)
        self.news = resources.NewsResource(self)
        self.insider_trades = resources.InsiderTradesResource(self)
        self.institutions = resources.InstitutionsResource(self)
        self.darkpool = resources.DarkpoolResource(self)
        self.seasonality = resources.SeasonalityResource(self)
        self.analyst = resources.AnalystResource(self)
        self.market = resources.MarketResource(self)
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
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
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
    spike_detections: resources.AsyncSpikeDetectionsResource
    economic_calendars: resources.AsyncEconomicCalendarsResource
    etf: resources.AsyncEtfResource
    options: resources.AsyncOptionsResource
    stocks: resources.AsyncStocksResource
    news: resources.AsyncNewsResource
    insider_trades: resources.AsyncInsiderTradesResource
    institutions: resources.AsyncInstitutionsResource
    darkpool: resources.AsyncDarkpoolResource
    seasonality: resources.AsyncSeasonalityResource
    analyst: resources.AsyncAnalystResource
    market: resources.AsyncMarketResource
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
        """Construct a new async tradesignals client instance.

        This automatically infers the `api_key` argument from the `UNUSUALWHALES_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("UNUSUALWHALES_API_KEY")
        if api_key is None:
            raise TradesignalsError(
                "The api_key client option must be set either by passing api_key to the client or by setting the UNUSUALWHALES_API_KEY environment variable"
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

        self.spike_detections = resources.AsyncSpikeDetectionsResource(self)
        self.economic_calendars = resources.AsyncEconomicCalendarsResource(self)
        self.etf = resources.AsyncEtfResource(self)
        self.options = resources.AsyncOptionsResource(self)
        self.stocks = resources.AsyncStocksResource(self)
        self.news = resources.AsyncNewsResource(self)
        self.insider_trades = resources.AsyncInsiderTradesResource(self)
        self.institutions = resources.AsyncInstitutionsResource(self)
        self.darkpool = resources.AsyncDarkpoolResource(self)
        self.seasonality = resources.AsyncSeasonalityResource(self)
        self.analyst = resources.AsyncAnalystResource(self)
        self.market = resources.AsyncMarketResource(self)
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
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
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
        self.spike_detections = resources.SpikeDetectionsResourceWithRawResponse(client.spike_detections)
        self.economic_calendars = resources.EconomicCalendarsResourceWithRawResponse(client.economic_calendars)
        self.etf = resources.EtfResourceWithRawResponse(client.etf)
        self.options = resources.OptionsResourceWithRawResponse(client.options)
        self.stocks = resources.StocksResourceWithRawResponse(client.stocks)
        self.news = resources.NewsResourceWithRawResponse(client.news)
        self.insider_trades = resources.InsiderTradesResourceWithRawResponse(client.insider_trades)
        self.institutions = resources.InstitutionsResourceWithRawResponse(client.institutions)
        self.darkpool = resources.DarkpoolResourceWithRawResponse(client.darkpool)
        self.seasonality = resources.SeasonalityResourceWithRawResponse(client.seasonality)
        self.analyst = resources.AnalystResourceWithRawResponse(client.analyst)
        self.market = resources.MarketResourceWithRawResponse(client.market)


class AsyncTradesignalsWithRawResponse:
    def __init__(self, client: AsyncTradesignals) -> None:
        self.spike_detections = resources.AsyncSpikeDetectionsResourceWithRawResponse(client.spike_detections)
        self.economic_calendars = resources.AsyncEconomicCalendarsResourceWithRawResponse(client.economic_calendars)
        self.etf = resources.AsyncEtfResourceWithRawResponse(client.etf)
        self.options = resources.AsyncOptionsResourceWithRawResponse(client.options)
        self.stocks = resources.AsyncStocksResourceWithRawResponse(client.stocks)
        self.news = resources.AsyncNewsResourceWithRawResponse(client.news)
        self.insider_trades = resources.AsyncInsiderTradesResourceWithRawResponse(client.insider_trades)
        self.institutions = resources.AsyncInstitutionsResourceWithRawResponse(client.institutions)
        self.darkpool = resources.AsyncDarkpoolResourceWithRawResponse(client.darkpool)
        self.seasonality = resources.AsyncSeasonalityResourceWithRawResponse(client.seasonality)
        self.analyst = resources.AsyncAnalystResourceWithRawResponse(client.analyst)
        self.market = resources.AsyncMarketResourceWithRawResponse(client.market)


class TradesignalsWithStreamedResponse:
    def __init__(self, client: Tradesignals) -> None:
        self.spike_detections = resources.SpikeDetectionsResourceWithStreamingResponse(client.spike_detections)
        self.economic_calendars = resources.EconomicCalendarsResourceWithStreamingResponse(client.economic_calendars)
        self.etf = resources.EtfResourceWithStreamingResponse(client.etf)
        self.options = resources.OptionsResourceWithStreamingResponse(client.options)
        self.stocks = resources.StocksResourceWithStreamingResponse(client.stocks)
        self.news = resources.NewsResourceWithStreamingResponse(client.news)
        self.insider_trades = resources.InsiderTradesResourceWithStreamingResponse(client.insider_trades)
        self.institutions = resources.InstitutionsResourceWithStreamingResponse(client.institutions)
        self.darkpool = resources.DarkpoolResourceWithStreamingResponse(client.darkpool)
        self.seasonality = resources.SeasonalityResourceWithStreamingResponse(client.seasonality)
        self.analyst = resources.AnalystResourceWithStreamingResponse(client.analyst)
        self.market = resources.MarketResourceWithStreamingResponse(client.market)


class AsyncTradesignalsWithStreamedResponse:
    def __init__(self, client: AsyncTradesignals) -> None:
        self.spike_detections = resources.AsyncSpikeDetectionsResourceWithStreamingResponse(client.spike_detections)
        self.economic_calendars = resources.AsyncEconomicCalendarsResourceWithStreamingResponse(
            client.economic_calendars
        )
        self.etf = resources.AsyncEtfResourceWithStreamingResponse(client.etf)
        self.options = resources.AsyncOptionsResourceWithStreamingResponse(client.options)
        self.stocks = resources.AsyncStocksResourceWithStreamingResponse(client.stocks)
        self.news = resources.AsyncNewsResourceWithStreamingResponse(client.news)
        self.insider_trades = resources.AsyncInsiderTradesResourceWithStreamingResponse(client.insider_trades)
        self.institutions = resources.AsyncInstitutionsResourceWithStreamingResponse(client.institutions)
        self.darkpool = resources.AsyncDarkpoolResourceWithStreamingResponse(client.darkpool)
        self.seasonality = resources.AsyncSeasonalityResourceWithStreamingResponse(client.seasonality)
        self.analyst = resources.AsyncAnalystResourceWithStreamingResponse(client.analyst)
        self.market = resources.AsyncMarketResourceWithStreamingResponse(client.market)


Client = Tradesignals

AsyncClient = AsyncTradesignals