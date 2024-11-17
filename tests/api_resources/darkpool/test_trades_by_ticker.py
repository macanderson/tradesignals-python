# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.darkpool import TradesByTickerListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTradesByTicker:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        trades_by_ticker = client.darkpool.trades_by_ticker.list(
            ticker="ticker",
        )
        assert_matches_type(Optional[TradesByTickerListResponse], trades_by_ticker, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        trades_by_ticker = client.darkpool.trades_by_ticker.list(
            ticker="ticker",
            date=parse_date("2019-12-27"),
            limit=0,
            newer_than="newer_than",
            older_than="older_than",
        )
        assert_matches_type(Optional[TradesByTickerListResponse], trades_by_ticker, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.darkpool.trades_by_ticker.with_raw_response.list(
            ticker="ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trades_by_ticker = response.parse()
        assert_matches_type(Optional[TradesByTickerListResponse], trades_by_ticker, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.darkpool.trades_by_ticker.with_streaming_response.list(
            ticker="ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trades_by_ticker = response.parse()
            assert_matches_type(Optional[TradesByTickerListResponse], trades_by_ticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            client.darkpool.trades_by_ticker.with_raw_response.list(
                ticker="",
            )


class TestAsyncTradesByTicker:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        trades_by_ticker = await async_client.darkpool.trades_by_ticker.list(
            ticker="ticker",
        )
        assert_matches_type(Optional[TradesByTickerListResponse], trades_by_ticker, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        trades_by_ticker = await async_client.darkpool.trades_by_ticker.list(
            ticker="ticker",
            date=parse_date("2019-12-27"),
            limit=0,
            newer_than="newer_than",
            older_than="older_than",
        )
        assert_matches_type(Optional[TradesByTickerListResponse], trades_by_ticker, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.darkpool.trades_by_ticker.with_raw_response.list(
            ticker="ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trades_by_ticker = await response.parse()
        assert_matches_type(Optional[TradesByTickerListResponse], trades_by_ticker, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.darkpool.trades_by_ticker.with_streaming_response.list(
            ticker="ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trades_by_ticker = await response.parse()
            assert_matches_type(Optional[TradesByTickerListResponse], trades_by_ticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            await async_client.darkpool.trades_by_ticker.with_raw_response.list(
                ticker="",
            )
