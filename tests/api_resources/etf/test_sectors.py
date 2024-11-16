# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals._utils import parse_date
from tradesignals.types.etf import SectorListResponse, SectorRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TradesignalsIo) -> None:
        sector = client.etf.sectors.retrieve()
        assert_matches_type(SectorRetrieveResponse, sector, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TradesignalsIo) -> None:
        sector = client.etf.sectors.retrieve(
            date=parse_date("2019-12-27"),
            sector="Technology",
        )
        assert_matches_type(SectorRetrieveResponse, sector, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TradesignalsIo) -> None:
        response = client.etf.sectors.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sector = response.parse()
        assert_matches_type(SectorRetrieveResponse, sector, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TradesignalsIo) -> None:
        with client.etf.sectors.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sector = response.parse()
            assert_matches_type(SectorRetrieveResponse, sector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: TradesignalsIo) -> None:
        sector = client.etf.sectors.list()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TradesignalsIo) -> None:
        response = client.etf.sectors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sector = response.parse()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TradesignalsIo) -> None:
        with client.etf.sectors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sector = response.parse()
            assert_matches_type(SectorListResponse, sector, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSectors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        sector = await async_client.etf.sectors.retrieve()
        assert_matches_type(SectorRetrieveResponse, sector, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        sector = await async_client.etf.sectors.retrieve(
            date=parse_date("2019-12-27"),
            sector="Technology",
        )
        assert_matches_type(SectorRetrieveResponse, sector, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.etf.sectors.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sector = await response.parse()
        assert_matches_type(SectorRetrieveResponse, sector, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.etf.sectors.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sector = await response.parse()
            assert_matches_type(SectorRetrieveResponse, sector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignalsIo) -> None:
        sector = await async_client.etf.sectors.list()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.etf.sectors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sector = await response.parse()
        assert_matches_type(SectorListResponse, sector, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.etf.sectors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sector = await response.parse()
            assert_matches_type(SectorListResponse, sector, path=["response"])

        assert cast(Any, response.is_closed) is True
