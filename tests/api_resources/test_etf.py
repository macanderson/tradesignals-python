# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals.types import EtfListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEtf:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TradesignalsIo) -> None:
        etf = client.etf.list()
        assert_matches_type(EtfListResponse, etf, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TradesignalsIo) -> None:
        response = client.etf.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        etf = response.parse()
        assert_matches_type(EtfListResponse, etf, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TradesignalsIo) -> None:
        with client.etf.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            etf = response.parse()
            assert_matches_type(EtfListResponse, etf, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEtf:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignalsIo) -> None:
        etf = await async_client.etf.list()
        assert_matches_type(EtfListResponse, etf, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.etf.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        etf = await response.parse()
        assert_matches_type(EtfListResponse, etf, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.etf.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            etf = await response.parse()
            assert_matches_type(EtfListResponse, etf, path=["response"])

        assert cast(Any, response.is_closed) is True
