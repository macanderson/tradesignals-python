# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.screener import OptionScreenerListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptionScreener:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        option_screener = client.screener.option_screener.list()
        assert_matches_type(Optional[OptionScreenerListResponse], option_screener, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        option_screener = client.screener.option_screener.list(
            expiry_dates=[parse_date("2019-12-27"), parse_date("2019-12-27"), parse_date("2019-12-27")],
            is_otm=True,
            issue_types=["Common Stock", "ETF", "Index"],
            max_daily_perc_change=0,
            min_volume=0,
            order="bid_ask_vol",
            order_direction="asc",
        )
        assert_matches_type(Optional[OptionScreenerListResponse], option_screener, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.screener.option_screener.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option_screener = response.parse()
        assert_matches_type(Optional[OptionScreenerListResponse], option_screener, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.screener.option_screener.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option_screener = response.parse()
            assert_matches_type(Optional[OptionScreenerListResponse], option_screener, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOptionScreener:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        option_screener = await async_client.screener.option_screener.list()
        assert_matches_type(Optional[OptionScreenerListResponse], option_screener, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        option_screener = await async_client.screener.option_screener.list(
            expiry_dates=[parse_date("2019-12-27"), parse_date("2019-12-27"), parse_date("2019-12-27")],
            is_otm=True,
            issue_types=["Common Stock", "ETF", "Index"],
            max_daily_perc_change=0,
            min_volume=0,
            order="bid_ask_vol",
            order_direction="asc",
        )
        assert_matches_type(Optional[OptionScreenerListResponse], option_screener, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.screener.option_screener.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option_screener = await response.parse()
        assert_matches_type(Optional[OptionScreenerListResponse], option_screener, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.screener.option_screener.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option_screener = await response.parse()
            assert_matches_type(Optional[OptionScreenerListResponse], option_screener, path=["response"])

        assert cast(Any, response.is_closed) is True
