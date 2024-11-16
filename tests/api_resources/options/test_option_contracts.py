# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals._utils import parse_date
from tradesignals.types.options import OptionContractListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptionContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TradesignalsIo) -> None:
        option_contract = client.options.option_contracts.list(
            symbol="symbol",
        )
        assert_matches_type(OptionContractListResponse, option_contract, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TradesignalsIo) -> None:
        option_contract = client.options.option_contracts.list(
            symbol="symbol",
            expiration=parse_date("2019-12-27"),
            option_type="CALL",
            strike=0,
        )
        assert_matches_type(OptionContractListResponse, option_contract, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TradesignalsIo) -> None:
        response = client.options.option_contracts.with_raw_response.list(
            symbol="symbol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option_contract = response.parse()
        assert_matches_type(OptionContractListResponse, option_contract, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TradesignalsIo) -> None:
        with client.options.option_contracts.with_streaming_response.list(
            symbol="symbol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option_contract = response.parse()
            assert_matches_type(OptionContractListResponse, option_contract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOptionContracts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignalsIo) -> None:
        option_contract = await async_client.options.option_contracts.list(
            symbol="symbol",
        )
        assert_matches_type(OptionContractListResponse, option_contract, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        option_contract = await async_client.options.option_contracts.list(
            symbol="symbol",
            expiration=parse_date("2019-12-27"),
            option_type="CALL",
            strike=0,
        )
        assert_matches_type(OptionContractListResponse, option_contract, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.options.option_contracts.with_raw_response.list(
            symbol="symbol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        option_contract = await response.parse()
        assert_matches_type(OptionContractListResponse, option_contract, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.options.option_contracts.with_streaming_response.list(
            symbol="symbol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            option_contract = await response.parse()
            assert_matches_type(OptionContractListResponse, option_contract, path=["response"])

        assert cast(Any, response.is_closed) is True
