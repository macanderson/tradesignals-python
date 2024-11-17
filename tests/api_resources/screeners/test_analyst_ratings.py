# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.screeners import AnalystRatingListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalystRatings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        analyst_rating = client.screeners.analyst_ratings.list()
        assert_matches_type(Optional[AnalystRatingListResponse], analyst_rating, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        analyst_rating = client.screeners.analyst_ratings.list(
            action="initiated",
            limit=1,
            recommendation="buy",
            ticker="ticker",
        )
        assert_matches_type(Optional[AnalystRatingListResponse], analyst_rating, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.screeners.analyst_ratings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analyst_rating = response.parse()
        assert_matches_type(Optional[AnalystRatingListResponse], analyst_rating, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.screeners.analyst_ratings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analyst_rating = response.parse()
            assert_matches_type(Optional[AnalystRatingListResponse], analyst_rating, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnalystRatings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        analyst_rating = await async_client.screeners.analyst_ratings.list()
        assert_matches_type(Optional[AnalystRatingListResponse], analyst_rating, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        analyst_rating = await async_client.screeners.analyst_ratings.list(
            action="initiated",
            limit=1,
            recommendation="buy",
            ticker="ticker",
        )
        assert_matches_type(Optional[AnalystRatingListResponse], analyst_rating, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.screeners.analyst_ratings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analyst_rating = await response.parse()
        assert_matches_type(Optional[AnalystRatingListResponse], analyst_rating, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.screeners.analyst_ratings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analyst_rating = await response.parse()
            assert_matches_type(Optional[AnalystRatingListResponse], analyst_rating, path=["response"])

        assert cast(Any, response.is_closed) is True
