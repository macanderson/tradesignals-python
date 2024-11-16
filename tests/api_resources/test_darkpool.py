# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals.types import (
    DarkpoolListResponse,
    DarkpoolRetrieveResponse,
)
from tradesignals._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDarkpool:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TradesignalsIo) -> None:
        darkpool = client.darkpool.retrieve(
            symbol="symbol",
        )
        assert_matches_type(DarkpoolRetrieveResponse, darkpool, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TradesignalsIo) -> None:
        darkpool = client.darkpool.retrieve(
            symbol="symbol",
            date=parse_date("2019-12-27"),
            limit=0,
            newer_than="newer_than",
            older_than="older_than",
        )
        assert_matches_type(DarkpoolRetrieveResponse, darkpool, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TradesignalsIo) -> None:
        response = client.darkpool.with_raw_response.retrieve(
            symbol="symbol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        darkpool = response.parse()
        assert_matches_type(DarkpoolRetrieveResponse, darkpool, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TradesignalsIo) -> None:
        with client.darkpool.with_streaming_response.retrieve(
            symbol="symbol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            darkpool = response.parse()
            assert_matches_type(DarkpoolRetrieveResponse, darkpool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: TradesignalsIo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            client.darkpool.with_raw_response.retrieve(
                symbol="",
            )

    @parametrize
    def test_method_list(self, client: TradesignalsIo) -> None:
        darkpool = client.darkpool.list()
        assert_matches_type(DarkpoolListResponse, darkpool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TradesignalsIo) -> None:
        darkpool = client.darkpool.list(
            date=parse_date("2019-12-27"),
            limit=0,
        )
        assert_matches_type(DarkpoolListResponse, darkpool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TradesignalsIo) -> None:
        response = client.darkpool.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        darkpool = response.parse()
        assert_matches_type(DarkpoolListResponse, darkpool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TradesignalsIo) -> None:
        with client.darkpool.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            darkpool = response.parse()
            assert_matches_type(DarkpoolListResponse, darkpool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDarkpool:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        darkpool = await async_client.darkpool.retrieve(
            symbol="symbol",
        )
        assert_matches_type(DarkpoolRetrieveResponse, darkpool, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        darkpool = await async_client.darkpool.retrieve(
            symbol="symbol",
            date=parse_date("2019-12-27"),
            limit=0,
            newer_than="newer_than",
            older_than="older_than",
        )
        assert_matches_type(DarkpoolRetrieveResponse, darkpool, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.darkpool.with_raw_response.retrieve(
            symbol="symbol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        darkpool = await response.parse()
        assert_matches_type(DarkpoolRetrieveResponse, darkpool, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.darkpool.with_streaming_response.retrieve(
            symbol="symbol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            darkpool = await response.parse()
            assert_matches_type(DarkpoolRetrieveResponse, darkpool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            await async_client.darkpool.with_raw_response.retrieve(
                symbol="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignalsIo) -> None:
        darkpool = await async_client.darkpool.list()
        assert_matches_type(DarkpoolListResponse, darkpool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        darkpool = await async_client.darkpool.list(
            date=parse_date("2019-12-27"),
            limit=0,
        )
        assert_matches_type(DarkpoolListResponse, darkpool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.darkpool.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        darkpool = await response.parse()
        assert_matches_type(DarkpoolListResponse, darkpool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.darkpool.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            darkpool = await response.parse()
            assert_matches_type(DarkpoolListResponse, darkpool, path=["response"])

        assert cast(Any, response.is_closed) is True
