# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals.types.stocks import ScreenerRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScreener:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TradesignalsIo) -> None:
        screener = client.stocks.screener.retrieve()
        assert_matches_type(ScreenerRetrieveResponse, screener, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TradesignalsIo) -> None:
        screener = client.stocks.screener.retrieve(
            industry="industry",
            market_cap_max=0,
            market_cap_min=0,
            price_max=0,
            price_min=0,
            sector="sector",
            volume_max=0,
            volume_min=0,
        )
        assert_matches_type(ScreenerRetrieveResponse, screener, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TradesignalsIo) -> None:
        response = client.stocks.screener.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screener = response.parse()
        assert_matches_type(ScreenerRetrieveResponse, screener, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TradesignalsIo) -> None:
        with client.stocks.screener.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screener = response.parse()
            assert_matches_type(ScreenerRetrieveResponse, screener, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScreener:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        screener = await async_client.stocks.screener.retrieve()
        assert_matches_type(ScreenerRetrieveResponse, screener, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        screener = await async_client.stocks.screener.retrieve(
            industry="industry",
            market_cap_max=0,
            market_cap_min=0,
            price_max=0,
            price_min=0,
            sector="sector",
            volume_max=0,
            volume_min=0,
        )
        assert_matches_type(ScreenerRetrieveResponse, screener, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.stocks.screener.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screener = await response.parse()
        assert_matches_type(ScreenerRetrieveResponse, screener, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.stocks.screener.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screener = await response.parse()
            assert_matches_type(ScreenerRetrieveResponse, screener, path=["response"])

        assert cast(Any, response.is_closed) is True
