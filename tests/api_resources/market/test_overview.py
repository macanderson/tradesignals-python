# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals.types.market import OverviewRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOverview:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TradesignalsIo) -> None:
        overview = client.market.overview.retrieve()
        assert_matches_type(OverviewRetrieveResponse, overview, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TradesignalsIo) -> None:
        response = client.market.overview.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overview = response.parse()
        assert_matches_type(OverviewRetrieveResponse, overview, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TradesignalsIo) -> None:
        with client.market.overview.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overview = response.parse()
            assert_matches_type(OverviewRetrieveResponse, overview, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOverview:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        overview = await async_client.market.overview.retrieve()
        assert_matches_type(OverviewRetrieveResponse, overview, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.market.overview.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overview = await response.parse()
        assert_matches_type(OverviewRetrieveResponse, overview, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.market.overview.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overview = await response.parse()
            assert_matches_type(OverviewRetrieveResponse, overview, path=["response"])

        assert cast(Any, response.is_closed) is True
