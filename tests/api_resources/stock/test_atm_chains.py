# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.stock import AtmChainListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAtmChains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        atm_chain = client.stock.atm_chains.list(
            ticker="AAPL",
            expirations=["string", "string", "string"],
        )
        assert_matches_type(Optional[AtmChainListResponse], atm_chain, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.stock.atm_chains.with_raw_response.list(
            ticker="AAPL",
            expirations=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        atm_chain = response.parse()
        assert_matches_type(Optional[AtmChainListResponse], atm_chain, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.stock.atm_chains.with_streaming_response.list(
            ticker="AAPL",
            expirations=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            atm_chain = response.parse()
            assert_matches_type(Optional[AtmChainListResponse], atm_chain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            client.stock.atm_chains.with_raw_response.list(
                ticker="",
                expirations=["string", "string", "string"],
            )


class TestAsyncAtmChains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        atm_chain = await async_client.stock.atm_chains.list(
            ticker="AAPL",
            expirations=["string", "string", "string"],
        )
        assert_matches_type(Optional[AtmChainListResponse], atm_chain, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.stock.atm_chains.with_raw_response.list(
            ticker="AAPL",
            expirations=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        atm_chain = await response.parse()
        assert_matches_type(Optional[AtmChainListResponse], atm_chain, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.stock.atm_chains.with_streaming_response.list(
            ticker="AAPL",
            expirations=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            atm_chain = await response.parse()
            assert_matches_type(Optional[AtmChainListResponse], atm_chain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            await async_client.stock.atm_chains.with_raw_response.list(
                ticker="",
                expirations=["string", "string", "string"],
            )
