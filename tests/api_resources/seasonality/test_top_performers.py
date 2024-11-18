# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.seasonality import TopPerformerListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopPerformers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        top_performer = client.seasonality.top_performers.list(
            month=5,
        )
        assert_matches_type(Optional[TopPerformerListResponse], top_performer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        top_performer = client.seasonality.top_performers.list(
            month=5,
            limit=1,
            min_oi=0,
            min_years=1,
            order="ticker",
            order_direction="asc",
            s_p_500_nasdaq_only=True,
            ticker_for_sector="ticker_for_sector",
        )
        assert_matches_type(Optional[TopPerformerListResponse], top_performer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.seasonality.top_performers.with_raw_response.list(
            month=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_performer = response.parse()
        assert_matches_type(Optional[TopPerformerListResponse], top_performer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.seasonality.top_performers.with_streaming_response.list(
            month=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_performer = response.parse()
            assert_matches_type(Optional[TopPerformerListResponse], top_performer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTopPerformers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        top_performer = await async_client.seasonality.top_performers.list(
            month=5,
        )
        assert_matches_type(Optional[TopPerformerListResponse], top_performer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        top_performer = await async_client.seasonality.top_performers.list(
            month=5,
            limit=1,
            min_oi=0,
            min_years=1,
            order="ticker",
            order_direction="asc",
            s_p_500_nasdaq_only=True,
            ticker_for_sector="ticker_for_sector",
        )
        assert_matches_type(Optional[TopPerformerListResponse], top_performer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.seasonality.top_performers.with_raw_response.list(
            month=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_performer = await response.parse()
        assert_matches_type(Optional[TopPerformerListResponse], top_performer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.seasonality.top_performers.with_streaming_response.list(
            month=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_performer = await response.parse()
            assert_matches_type(Optional[TopPerformerListResponse], top_performer, path=["response"])

        assert cast(Any, response.is_closed) is True
