# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.earnings import HistoricalEarningsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPastTicker:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Tradesignals) -> None:
        past_ticker = client.earnings.past_ticker.retrieve(
            "ticker",
        )
        assert_matches_type(HistoricalEarningsResponse, past_ticker, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Tradesignals) -> None:
        response = client.earnings.past_ticker.with_raw_response.retrieve(
            "ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        past_ticker = response.parse()
        assert_matches_type(HistoricalEarningsResponse, past_ticker, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Tradesignals) -> None:
        with client.earnings.past_ticker.with_streaming_response.retrieve(
            "ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            past_ticker = response.parse()
            assert_matches_type(HistoricalEarningsResponse, past_ticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            client.earnings.past_ticker.with_raw_response.retrieve(
                "",
            )


class TestAsyncPastTicker:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignals) -> None:
        past_ticker = await async_client.earnings.past_ticker.retrieve(
            "ticker",
        )
        assert_matches_type(HistoricalEarningsResponse, past_ticker, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.earnings.past_ticker.with_raw_response.retrieve(
            "ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        past_ticker = await response.parse()
        assert_matches_type(HistoricalEarningsResponse, past_ticker, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        async with async_client.earnings.past_ticker.with_streaming_response.retrieve(
            "ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            past_ticker = await response.parse()
            assert_matches_type(HistoricalEarningsResponse, past_ticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            await async_client.earnings.past_ticker.with_raw_response.retrieve(
                "",
            )
