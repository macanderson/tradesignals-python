# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.market_data import MarketOiChangeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarketOiChange:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        market_oi_change = client.market_data.market_oi_change.list()
        assert_matches_type(Optional[MarketOiChangeListResponse], market_oi_change, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        market_oi_change = client.market_data.market_oi_change.list(
            date=parse_date("2024-01-18"),
            limit=10,
            order="desc",
        )
        assert_matches_type(Optional[MarketOiChangeListResponse], market_oi_change, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.market_data.market_oi_change.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_oi_change = response.parse()
        assert_matches_type(Optional[MarketOiChangeListResponse], market_oi_change, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.market_data.market_oi_change.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_oi_change = response.parse()
            assert_matches_type(Optional[MarketOiChangeListResponse], market_oi_change, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarketOiChange:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        market_oi_change = await async_client.market_data.market_oi_change.list()
        assert_matches_type(Optional[MarketOiChangeListResponse], market_oi_change, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        market_oi_change = await async_client.market_data.market_oi_change.list(
            date=parse_date("2024-01-18"),
            limit=10,
            order="desc",
        )
        assert_matches_type(Optional[MarketOiChangeListResponse], market_oi_change, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.market_data.market_oi_change.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market_oi_change = await response.parse()
        assert_matches_type(Optional[MarketOiChangeListResponse], market_oi_change, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.market_data.market_oi_change.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market_oi_change = await response.parse()
            assert_matches_type(Optional[MarketOiChangeListResponse], market_oi_change, path=["response"])

        assert cast(Any, response.is_closed) is True
