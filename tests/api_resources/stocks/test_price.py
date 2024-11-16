# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.stocks import PriceRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Tradesignals) -> None:
        price = client.stocks.price.retrieve(
            "symbol",
        )
        assert_matches_type(PriceRetrieveResponse, price, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Tradesignals) -> None:
        response = client.stocks.price.with_raw_response.retrieve(
            "symbol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceRetrieveResponse, price, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Tradesignals) -> None:
        with client.stocks.price.with_streaming_response.retrieve(
            "symbol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(PriceRetrieveResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            client.stocks.price.with_raw_response.retrieve(
                "",
            )


class TestAsyncPrice:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignals) -> None:
        price = await async_client.stocks.price.retrieve(
            "symbol",
        )
        assert_matches_type(PriceRetrieveResponse, price, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.stocks.price.with_raw_response.retrieve(
            "symbol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = await response.parse()
        assert_matches_type(PriceRetrieveResponse, price, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        async with async_client.stocks.price.with_streaming_response.retrieve(
            "symbol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(PriceRetrieveResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            await async_client.stocks.price.with_raw_response.retrieve(
                "",
            )
