# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals.types import CorrelationRetrieveResponse
from tradesignals._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCorrelations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TradesignalsIo) -> None:
        correlation = client.correlations.retrieve(
            symbols="symbols",
        )
        assert_matches_type(CorrelationRetrieveResponse, correlation, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TradesignalsIo) -> None:
        correlation = client.correlations.retrieve(
            symbols="symbols",
            end_date=parse_date("2019-12-27"),
            interval="1d",
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(CorrelationRetrieveResponse, correlation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TradesignalsIo) -> None:
        response = client.correlations.with_raw_response.retrieve(
            symbols="symbols",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        correlation = response.parse()
        assert_matches_type(CorrelationRetrieveResponse, correlation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TradesignalsIo) -> None:
        with client.correlations.with_streaming_response.retrieve(
            symbols="symbols",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            correlation = response.parse()
            assert_matches_type(CorrelationRetrieveResponse, correlation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCorrelations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        correlation = await async_client.correlations.retrieve(
            symbols="symbols",
        )
        assert_matches_type(CorrelationRetrieveResponse, correlation, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        correlation = await async_client.correlations.retrieve(
            symbols="symbols",
            end_date=parse_date("2019-12-27"),
            interval="1d",
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(CorrelationRetrieveResponse, correlation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.correlations.with_raw_response.retrieve(
            symbols="symbols",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        correlation = await response.parse()
        assert_matches_type(CorrelationRetrieveResponse, correlation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.correlations.with_streaming_response.retrieve(
            symbols="symbols",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            correlation = await response.parse()
            assert_matches_type(CorrelationRetrieveResponse, correlation, path=["response"])

        assert cast(Any, response.is_closed) is True
