# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.congress import CongressionalTraderReport

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrader:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Tradesignals) -> None:
        trader = client.congress.trader.retrieve()
        assert_matches_type(CongressionalTraderReport, trader, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Tradesignals) -> None:
        trader = client.congress.trader.retrieve(
            date=parse_date("2019-12-27"),
            limit=10,
            name="Adam+Kinzinger",
        )
        assert_matches_type(CongressionalTraderReport, trader, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Tradesignals) -> None:
        response = client.congress.trader.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trader = response.parse()
        assert_matches_type(CongressionalTraderReport, trader, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Tradesignals) -> None:
        with client.congress.trader.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trader = response.parse()
            assert_matches_type(CongressionalTraderReport, trader, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrader:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignals) -> None:
        trader = await async_client.congress.trader.retrieve()
        assert_matches_type(CongressionalTraderReport, trader, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignals) -> None:
        trader = await async_client.congress.trader.retrieve(
            date=parse_date("2019-12-27"),
            limit=10,
            name="Adam+Kinzinger",
        )
        assert_matches_type(CongressionalTraderReport, trader, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.congress.trader.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trader = await response.parse()
        assert_matches_type(CongressionalTraderReport, trader, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        async with async_client.congress.trader.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trader = await response.parse()
            assert_matches_type(CongressionalTraderReport, trader, path=["response"])

        assert cast(Any, response.is_closed) is True
