# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.stock import OffLitPriceLevelsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOffLitPriceLevels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        off_lit_price_level = client.stock.off_lit_price_levels.list(
            ticker="AAPL",
        )
        assert_matches_type(OffLitPriceLevelsResponse, off_lit_price_level, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        off_lit_price_level = client.stock.off_lit_price_levels.list(
            ticker="AAPL",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(OffLitPriceLevelsResponse, off_lit_price_level, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.stock.off_lit_price_levels.with_raw_response.list(
            ticker="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        off_lit_price_level = response.parse()
        assert_matches_type(OffLitPriceLevelsResponse, off_lit_price_level, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.stock.off_lit_price_levels.with_streaming_response.list(
            ticker="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            off_lit_price_level = response.parse()
            assert_matches_type(OffLitPriceLevelsResponse, off_lit_price_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            client.stock.off_lit_price_levels.with_raw_response.list(
                ticker="",
            )


class TestAsyncOffLitPriceLevels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        off_lit_price_level = await async_client.stock.off_lit_price_levels.list(
            ticker="AAPL",
        )
        assert_matches_type(OffLitPriceLevelsResponse, off_lit_price_level, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        off_lit_price_level = await async_client.stock.off_lit_price_levels.list(
            ticker="AAPL",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(OffLitPriceLevelsResponse, off_lit_price_level, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.stock.off_lit_price_levels.with_raw_response.list(
            ticker="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        off_lit_price_level = await response.parse()
        assert_matches_type(OffLitPriceLevelsResponse, off_lit_price_level, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.stock.off_lit_price_levels.with_streaming_response.list(
            ticker="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            off_lit_price_level = await response.parse()
            assert_matches_type(OffLitPriceLevelsResponse, off_lit_price_level, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            await async_client.stock.off_lit_price_levels.with_raw_response.list(
                ticker="",
            )
