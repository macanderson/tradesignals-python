# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFinancials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Tradesignals) -> None:
        financial = client.stocks.financials.retrieve(
            symbol="symbol",
            statement_type="income",
        )
        assert_matches_type(object, financial, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Tradesignals) -> None:
        financial = client.stocks.financials.retrieve(
            symbol="symbol",
            statement_type="income",
            period="annual",
        )
        assert_matches_type(object, financial, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Tradesignals) -> None:
        response = client.stocks.financials.with_raw_response.retrieve(
            symbol="symbol",
            statement_type="income",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial = response.parse()
        assert_matches_type(object, financial, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Tradesignals) -> None:
        with client.stocks.financials.with_streaming_response.retrieve(
            symbol="symbol",
            statement_type="income",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial = response.parse()
            assert_matches_type(object, financial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            client.stocks.financials.with_raw_response.retrieve(
                symbol="",
                statement_type="income",
            )


class TestAsyncFinancials:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignals) -> None:
        financial = await async_client.stocks.financials.retrieve(
            symbol="symbol",
            statement_type="income",
        )
        assert_matches_type(object, financial, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignals) -> None:
        financial = await async_client.stocks.financials.retrieve(
            symbol="symbol",
            statement_type="income",
            period="annual",
        )
        assert_matches_type(object, financial, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.stocks.financials.with_raw_response.retrieve(
            symbol="symbol",
            statement_type="income",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial = await response.parse()
        assert_matches_type(object, financial, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        async with async_client.stocks.financials.with_streaming_response.retrieve(
            symbol="symbol",
            statement_type="income",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial = await response.parse()
            assert_matches_type(object, financial, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            await async_client.stocks.financials.with_raw_response.retrieve(
                symbol="",
                statement_type="income",
            )
