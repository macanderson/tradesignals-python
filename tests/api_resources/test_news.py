# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals.types import NewsListResponse
from tradesignals._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TradesignalsIo) -> None:
        news = client.news.list()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TradesignalsIo) -> None:
        news = client.news.list(
            date=parse_date("2019-12-27"),
            symbols="symbols",
        )
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TradesignalsIo) -> None:
        response = client.news.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = response.parse()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TradesignalsIo) -> None:
        with client.news.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = response.parse()
            assert_matches_type(NewsListResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignalsIo) -> None:
        news = await async_client.news.list()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        news = await async_client.news.list(
            date=parse_date("2019-12-27"),
            symbols="symbols",
        )
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.news.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = await response.parse()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.news.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = await response.parse()
            assert_matches_type(NewsListResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True
