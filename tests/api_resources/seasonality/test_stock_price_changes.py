# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.seasonality import StockPriceChangeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStockPriceChanges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        stock_price_change = client.seasonality.stock_price_changes.list(
            "ticker",
        )
        assert_matches_type(Optional[StockPriceChangeListResponse], stock_price_change, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.seasonality.stock_price_changes.with_raw_response.list(
            "ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock_price_change = response.parse()
        assert_matches_type(Optional[StockPriceChangeListResponse], stock_price_change, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.seasonality.stock_price_changes.with_streaming_response.list(
            "ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock_price_change = response.parse()
            assert_matches_type(Optional[StockPriceChangeListResponse], stock_price_change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            client.seasonality.stock_price_changes.with_raw_response.list(
                "",
            )


class TestAsyncStockPriceChanges:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        stock_price_change = await async_client.seasonality.stock_price_changes.list(
            "ticker",
        )
        assert_matches_type(Optional[StockPriceChangeListResponse], stock_price_change, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.seasonality.stock_price_changes.with_raw_response.list(
            "ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stock_price_change = await response.parse()
        assert_matches_type(Optional[StockPriceChangeListResponse], stock_price_change, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.seasonality.stock_price_changes.with_streaming_response.list(
            "ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stock_price_change = await response.parse()
            assert_matches_type(Optional[StockPriceChangeListResponse], stock_price_change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            await async_client.seasonality.stock_price_changes.with_raw_response.list(
                "",
            )
