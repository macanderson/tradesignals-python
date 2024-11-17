# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

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
    "ENVIRONMENTS",
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

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.unusualwhales.com",
    "test": "https://test.tradesignals.io",
}


class Tradesignals(SyncAPIClient):
    institutions: resources.InstitutionsResource
    earnings: resources.EarningsResource
    congress: resources.CongressResource
    industry_groups: resources.IndustryGroupsResource
    etf: resources.EtfResource
    darkpool: resources.DarkpoolResource
    with_raw_response: TradesignalsWithRawResponse
    with_streaming_response: TradesignalsWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "test"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "test"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
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

        self._environment = environment

        base_url_env = os.environ.get("TRADESIGNALS_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TRADESIGNALS_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

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

        self.institutions = resources.InstitutionsResource(self)
        self.earnings = resources.EarningsResource(self)
        self.congress = resources.CongressResource(self)
        self.industry_groups = resources.IndustryGroupsResource(self)
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
        environment: Literal["production", "test"] | None = None,
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
            environment=environment or self._environment,
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
    institutions: resources.AsyncInstitutionsResource
    earnings: resources.AsyncEarningsResource
    congress: resources.AsyncCongressResource
    industry_groups: resources.AsyncIndustryGroupsResource
    etf: resources.AsyncEtfResource
    darkpool: resources.AsyncDarkpoolResource
    with_raw_response: AsyncTradesignalsWithRawResponse
    with_streaming_response: AsyncTradesignalsWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "test"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "test"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
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

        self._environment = environment

        base_url_env = os.environ.get("TRADESIGNALS_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `TRADESIGNALS_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

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

        self.institutions = resources.AsyncInstitutionsResource(self)
        self.earnings = resources.AsyncEarningsResource(self)
        self.congress = resources.AsyncCongressResource(self)
        self.industry_groups = resources.AsyncIndustryGroupsResource(self)
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
        environment: Literal["production", "test"] | None = None,
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
            environment=environment or self._environment,
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
        self.institutions = resources.InstitutionsResourceWithRawResponse(client.institutions)
        self.earnings = resources.EarningsResourceWithRawResponse(client.earnings)
        self.congress = resources.CongressResourceWithRawResponse(client.congress)
        self.industry_groups = resources.IndustryGroupsResourceWithRawResponse(client.industry_groups)
        self.etf = resources.EtfResourceWithRawResponse(client.etf)
        self.darkpool = resources.DarkpoolResourceWithRawResponse(client.darkpool)


class AsyncTradesignalsWithRawResponse:
    def __init__(self, client: AsyncTradesignals) -> None:
        self.institutions = resources.AsyncInstitutionsResourceWithRawResponse(client.institutions)
        self.earnings = resources.AsyncEarningsResourceWithRawResponse(client.earnings)
        self.congress = resources.AsyncCongressResourceWithRawResponse(client.congress)
        self.industry_groups = resources.AsyncIndustryGroupsResourceWithRawResponse(client.industry_groups)
        self.etf = resources.AsyncEtfResourceWithRawResponse(client.etf)
        self.darkpool = resources.AsyncDarkpoolResourceWithRawResponse(client.darkpool)


class TradesignalsWithStreamedResponse:
    def __init__(self, client: Tradesignals) -> None:
        self.institutions = resources.InstitutionsResourceWithStreamingResponse(client.institutions)
        self.earnings = resources.EarningsResourceWithStreamingResponse(client.earnings)
        self.congress = resources.CongressResourceWithStreamingResponse(client.congress)
        self.industry_groups = resources.IndustryGroupsResourceWithStreamingResponse(client.industry_groups)
        self.etf = resources.EtfResourceWithStreamingResponse(client.etf)
        self.darkpool = resources.DarkpoolResourceWithStreamingResponse(client.darkpool)


class AsyncTradesignalsWithStreamedResponse:
    def __init__(self, client: AsyncTradesignals) -> None:
        self.institutions = resources.AsyncInstitutionsResourceWithStreamingResponse(client.institutions)
        self.earnings = resources.AsyncEarningsResourceWithStreamingResponse(client.earnings)
        self.congress = resources.AsyncCongressResourceWithStreamingResponse(client.congress)
        self.industry_groups = resources.AsyncIndustryGroupsResourceWithStreamingResponse(client.industry_groups)
        self.etf = resources.AsyncEtfResourceWithStreamingResponse(client.etf)
        self.darkpool = resources.AsyncDarkpoolResourceWithStreamingResponse(client.darkpool)


Client = Tradesignals

AsyncClient = AsyncTradesignals
