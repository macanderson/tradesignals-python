# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals._utils import parse_date
from tradesignals.types.options import OiChangeRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOiChange:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TradesignalsIo) -> None:
        oi_change = client.options.oi_change.retrieve(
            symbol="AAPL",
        )
        assert_matches_type(OiChangeRetrieveResponse, oi_change, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TradesignalsIo) -> None:
        oi_change = client.options.oi_change.retrieve(
            symbol="AAPL",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(OiChangeRetrieveResponse, oi_change, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TradesignalsIo) -> None:
        response = client.options.oi_change.with_raw_response.retrieve(
            symbol="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oi_change = response.parse()
        assert_matches_type(OiChangeRetrieveResponse, oi_change, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TradesignalsIo) -> None:
        with client.options.oi_change.with_streaming_response.retrieve(
            symbol="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oi_change = response.parse()
            assert_matches_type(OiChangeRetrieveResponse, oi_change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: TradesignalsIo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            client.options.oi_change.with_raw_response.retrieve(
                symbol="",
            )


class TestAsyncOiChange:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        oi_change = await async_client.options.oi_change.retrieve(
            symbol="AAPL",
        )
        assert_matches_type(OiChangeRetrieveResponse, oi_change, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        oi_change = await async_client.options.oi_change.retrieve(
            symbol="AAPL",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(OiChangeRetrieveResponse, oi_change, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.options.oi_change.with_raw_response.retrieve(
            symbol="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oi_change = await response.parse()
        assert_matches_type(OiChangeRetrieveResponse, oi_change, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.options.oi_change.with_streaming_response.retrieve(
            symbol="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oi_change = await response.parse()
            assert_matches_type(OiChangeRetrieveResponse, oi_change, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            await async_client.options.oi_change.with_raw_response.retrieve(
                symbol="",
            )
