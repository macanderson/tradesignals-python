# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals._utils import parse_date
from tradesignals.types.darkpool import TickerDarkpoolTradeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTickerDarkpoolTrades:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TradesignalsIo) -> None:
        ticker_darkpool_trade = client.darkpool.ticker_darkpool_trades.list(
            ticker="ticker",
        )
        assert_matches_type(Optional[TickerDarkpoolTradeListResponse], ticker_darkpool_trade, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TradesignalsIo) -> None:
        ticker_darkpool_trade = client.darkpool.ticker_darkpool_trades.list(
            ticker="ticker",
            date=parse_date("2019-12-27"),
            limit=0,
            newer_than="newer_than",
            older_than="older_than",
        )
        assert_matches_type(Optional[TickerDarkpoolTradeListResponse], ticker_darkpool_trade, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TradesignalsIo) -> None:
        response = client.darkpool.ticker_darkpool_trades.with_raw_response.list(
            ticker="ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticker_darkpool_trade = response.parse()
        assert_matches_type(Optional[TickerDarkpoolTradeListResponse], ticker_darkpool_trade, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TradesignalsIo) -> None:
        with client.darkpool.ticker_darkpool_trades.with_streaming_response.list(
            ticker="ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticker_darkpool_trade = response.parse()
            assert_matches_type(Optional[TickerDarkpoolTradeListResponse], ticker_darkpool_trade, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: TradesignalsIo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            client.darkpool.ticker_darkpool_trades.with_raw_response.list(
                ticker="",
            )


class TestAsyncTickerDarkpoolTrades:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignalsIo) -> None:
        ticker_darkpool_trade = await async_client.darkpool.ticker_darkpool_trades.list(
            ticker="ticker",
        )
        assert_matches_type(Optional[TickerDarkpoolTradeListResponse], ticker_darkpool_trade, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        ticker_darkpool_trade = await async_client.darkpool.ticker_darkpool_trades.list(
            ticker="ticker",
            date=parse_date("2019-12-27"),
            limit=0,
            newer_than="newer_than",
            older_than="older_than",
        )
        assert_matches_type(Optional[TickerDarkpoolTradeListResponse], ticker_darkpool_trade, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.darkpool.ticker_darkpool_trades.with_raw_response.list(
            ticker="ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticker_darkpool_trade = await response.parse()
        assert_matches_type(Optional[TickerDarkpoolTradeListResponse], ticker_darkpool_trade, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.darkpool.ticker_darkpool_trades.with_streaming_response.list(
            ticker="ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticker_darkpool_trade = await response.parse()
            assert_matches_type(Optional[TickerDarkpoolTradeListResponse], ticker_darkpool_trade, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTradesignalsIo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            await async_client.darkpool.ticker_darkpool_trades.with_raw_response.list(
                ticker="",
            )
