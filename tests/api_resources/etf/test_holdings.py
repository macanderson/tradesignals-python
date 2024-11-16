# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals._utils import parse_date
from tradesignals.types.etf import HoldingListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHoldings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TradesignalsIo) -> None:
        holding = client.etf.holdings.list(
            etf="etf",
        )
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TradesignalsIo) -> None:
        holding = client.etf.holdings.list(
            etf="etf",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TradesignalsIo) -> None:
        response = client.etf.holdings.with_raw_response.list(
            etf="etf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        holding = response.parse()
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TradesignalsIo) -> None:
        with client.etf.holdings.with_streaming_response.list(
            etf="etf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            holding = response.parse()
            assert_matches_type(HoldingListResponse, holding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHoldings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignalsIo) -> None:
        holding = await async_client.etf.holdings.list(
            etf="etf",
        )
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        holding = await async_client.etf.holdings.list(
            etf="etf",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.etf.holdings.with_raw_response.list(
            etf="etf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        holding = await response.parse()
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.etf.holdings.with_streaming_response.list(
            etf="etf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            holding = await response.parse()
            assert_matches_type(HoldingListResponse, holding, path=["response"])

        assert cast(Any, response.is_closed) is True
