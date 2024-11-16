# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals._utils import parse_date
from tradesignals.types.stocks import HistoricalRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistorical:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TradesignalsIo) -> None:
        historical = client.stocks.historical.retrieve(
            symbol="symbol",
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(HistoricalRetrieveResponse, historical, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TradesignalsIo) -> None:
        historical = client.stocks.historical.retrieve(
            symbol="symbol",
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            interval="1m",
        )
        assert_matches_type(HistoricalRetrieveResponse, historical, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TradesignalsIo) -> None:
        response = client.stocks.historical.with_raw_response.retrieve(
            symbol="symbol",
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        historical = response.parse()
        assert_matches_type(HistoricalRetrieveResponse, historical, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TradesignalsIo) -> None:
        with client.stocks.historical.with_streaming_response.retrieve(
            symbol="symbol",
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            historical = response.parse()
            assert_matches_type(HistoricalRetrieveResponse, historical, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: TradesignalsIo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            client.stocks.historical.with_raw_response.retrieve(
                symbol="",
                end_date=parse_date("2019-12-27"),
                start_date=parse_date("2019-12-27"),
            )


class TestAsyncHistorical:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        historical = await async_client.stocks.historical.retrieve(
            symbol="symbol",
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(HistoricalRetrieveResponse, historical, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        historical = await async_client.stocks.historical.retrieve(
            symbol="symbol",
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            interval="1m",
        )
        assert_matches_type(HistoricalRetrieveResponse, historical, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.stocks.historical.with_raw_response.retrieve(
            symbol="symbol",
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        historical = await response.parse()
        assert_matches_type(HistoricalRetrieveResponse, historical, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.stocks.historical.with_streaming_response.retrieve(
            symbol="symbol",
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            historical = await response.parse()
            assert_matches_type(HistoricalRetrieveResponse, historical, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            await async_client.stocks.historical.with_raw_response.retrieve(
                symbol="",
                end_date=parse_date("2019-12-27"),
                start_date=parse_date("2019-12-27"),
            )
