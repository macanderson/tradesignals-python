# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.option_contracts import ExpiryBreakdownListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExpiryBreakdown:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        expiry_breakdown = client.option_contracts.expiry_breakdown.list(
            ticker="AAPL",
        )
        assert_matches_type(Optional[ExpiryBreakdownListResponse], expiry_breakdown, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        expiry_breakdown = client.option_contracts.expiry_breakdown.list(
            ticker="AAPL",
            date=parse_date("2024-01-18"),
        )
        assert_matches_type(Optional[ExpiryBreakdownListResponse], expiry_breakdown, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.option_contracts.expiry_breakdown.with_raw_response.list(
            ticker="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expiry_breakdown = response.parse()
        assert_matches_type(Optional[ExpiryBreakdownListResponse], expiry_breakdown, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.option_contracts.expiry_breakdown.with_streaming_response.list(
            ticker="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expiry_breakdown = response.parse()
            assert_matches_type(Optional[ExpiryBreakdownListResponse], expiry_breakdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            client.option_contracts.expiry_breakdown.with_raw_response.list(
                ticker="",
            )


class TestAsyncExpiryBreakdown:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        expiry_breakdown = await async_client.option_contracts.expiry_breakdown.list(
            ticker="AAPL",
        )
        assert_matches_type(Optional[ExpiryBreakdownListResponse], expiry_breakdown, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        expiry_breakdown = await async_client.option_contracts.expiry_breakdown.list(
            ticker="AAPL",
            date=parse_date("2024-01-18"),
        )
        assert_matches_type(Optional[ExpiryBreakdownListResponse], expiry_breakdown, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.option_contracts.expiry_breakdown.with_raw_response.list(
            ticker="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expiry_breakdown = await response.parse()
        assert_matches_type(Optional[ExpiryBreakdownListResponse], expiry_breakdown, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.option_contracts.expiry_breakdown.with_streaming_response.list(
            ticker="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expiry_breakdown = await response.parse()
            assert_matches_type(Optional[ExpiryBreakdownListResponse], expiry_breakdown, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            await async_client.option_contracts.expiry_breakdown.with_raw_response.list(
                ticker="",
            )