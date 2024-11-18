# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.screener import StockScreenerListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStockScreener:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        stock_screener = client.screener.stock_screener.list()
        assert_matches_type(Optional[StockScreenerListResponse], stock_screener, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        stock_screener = client.screener.stock_screener.list(
            has_dividends=True,
            is_s_p_500=True,
            issue_types=["Common Stock", "ETF", "Index"],
            max_marketcap=0,
            min_volume=0,
            order="premium",
            order_direction="asc",
        )
        assert_matches_type(Optional[StockScreenerListResponse], stock_screener, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.screener.stock_screener.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock_screener = response.parse()
        assert_matches_type(Optional[StockScreenerListResponse], stock_screener, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.screener.stock_screener.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock_screener = response.parse()
            assert_matches_type(Optional[StockScreenerListResponse], stock_screener, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStockScreener:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        stock_screener = await async_client.screener.stock_screener.list()
        assert_matches_type(Optional[StockScreenerListResponse], stock_screener, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        stock_screener = await async_client.screener.stock_screener.list(
            has_dividends=True,
            is_s_p_500=True,
            issue_types=["Common Stock", "ETF", "Index"],
            max_marketcap=0,
            min_volume=0,
            order="premium",
            order_direction="asc",
        )
        assert_matches_type(Optional[StockScreenerListResponse], stock_screener, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.screener.stock_screener.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock_screener = await response.parse()
        assert_matches_type(Optional[StockScreenerListResponse], stock_screener, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.screener.stock_screener.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock_screener = await response.parse()
            assert_matches_type(Optional[StockScreenerListResponse], stock_screener, path=["response"])

        assert cast(Any, response.is_closed) is True
