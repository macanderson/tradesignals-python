# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.option_contract import OptionChainListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptionChains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        option_chain = client.option_contract.option_chains.list(
            ticker="AAPL",
        )
        assert_matches_type(Optional[OptionChainListResponse], option_chain, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        option_chain = client.option_contract.option_chains.list(
            ticker="AAPL",
            exclude_zero_dte=True,
            exclude_zero_oi_chains=True,
            exclude_zero_vol_chains=True,
            expiry=parse_date("2024-02-02"),
            limit=10,
            maybe_otm_only=True,
            option_type="call",
            vol_greater_oi=True,
        )
        assert_matches_type(Optional[OptionChainListResponse], option_chain, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.option_contract.option_chains.with_raw_response.list(
            ticker="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option_chain = response.parse()
        assert_matches_type(Optional[OptionChainListResponse], option_chain, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.option_contract.option_chains.with_streaming_response.list(
            ticker="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option_chain = response.parse()
            assert_matches_type(Optional[OptionChainListResponse], option_chain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            client.option_contract.option_chains.with_raw_response.list(
                ticker="",
            )


class TestAsyncOptionChains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        option_chain = await async_client.option_contract.option_chains.list(
            ticker="AAPL",
        )
        assert_matches_type(Optional[OptionChainListResponse], option_chain, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        option_chain = await async_client.option_contract.option_chains.list(
            ticker="AAPL",
            exclude_zero_dte=True,
            exclude_zero_oi_chains=True,
            exclude_zero_vol_chains=True,
            expiry=parse_date("2024-02-02"),
            limit=10,
            maybe_otm_only=True,
            option_type="call",
            vol_greater_oi=True,
        )
        assert_matches_type(Optional[OptionChainListResponse], option_chain, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.option_contract.option_chains.with_raw_response.list(
            ticker="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option_chain = await response.parse()
        assert_matches_type(Optional[OptionChainListResponse], option_chain, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.option_contract.option_chains.with_streaming_response.list(
            ticker="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option_chain = await response.parse()
            assert_matches_type(Optional[OptionChainListResponse], option_chain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            await async_client.option_contract.option_chains.with_raw_response.list(
                ticker="",
            )
