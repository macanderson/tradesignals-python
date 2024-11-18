# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.institution import TradingActivityListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTradingActivity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        trading_activity = client.institution.trading_activity.list(
            name="VANGUARD GROUP INC",
        )
        assert_matches_type(Optional[TradingActivityListResponse], trading_activity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        trading_activity = client.institution.trading_activity.list(
            name="VANGUARD GROUP INC",
            date=parse_date("2019-12-27"),
            limit=10,
            page=1,
        )
        assert_matches_type(Optional[TradingActivityListResponse], trading_activity, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.institution.trading_activity.with_raw_response.list(
            name="VANGUARD GROUP INC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trading_activity = response.parse()
        assert_matches_type(Optional[TradingActivityListResponse], trading_activity, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.institution.trading_activity.with_streaming_response.list(
            name="VANGUARD GROUP INC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trading_activity = response.parse()
            assert_matches_type(Optional[TradingActivityListResponse], trading_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.institution.trading_activity.with_raw_response.list(
                name="",
            )


class TestAsyncTradingActivity:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        trading_activity = await async_client.institution.trading_activity.list(
            name="VANGUARD GROUP INC",
        )
        assert_matches_type(Optional[TradingActivityListResponse], trading_activity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        trading_activity = await async_client.institution.trading_activity.list(
            name="VANGUARD GROUP INC",
            date=parse_date("2019-12-27"),
            limit=10,
            page=1,
        )
        assert_matches_type(Optional[TradingActivityListResponse], trading_activity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.institution.trading_activity.with_raw_response.list(
            name="VANGUARD GROUP INC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trading_activity = await response.parse()
        assert_matches_type(Optional[TradingActivityListResponse], trading_activity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.institution.trading_activity.with_streaming_response.list(
            name="VANGUARD GROUP INC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trading_activity = await response.parse()
            assert_matches_type(Optional[TradingActivityListResponse], trading_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.institution.trading_activity.with_raw_response.list(
                name="",
            )
