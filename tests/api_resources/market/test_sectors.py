# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals.types.market import SectorListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TradesignalsIo) -> None:
        sector = client.market.sectors.list()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TradesignalsIo) -> None:
        sector = client.market.sectors.list(
            time_frame="daily",
        )
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TradesignalsIo) -> None:
        response = client.market.sectors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sector = response.parse()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TradesignalsIo) -> None:
        with client.market.sectors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sector = response.parse()
            assert_matches_type(SectorListResponse, sector, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSectors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignalsIo) -> None:
        sector = await async_client.market.sectors.list()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        sector = await async_client.market.sectors.list(
            time_frame="daily",
        )
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.market.sectors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sector = await response.parse()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.market.sectors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sector = await response.parse()
            assert_matches_type(SectorListResponse, sector, path=["response"])

        assert cast(Any, response.is_closed) is True
