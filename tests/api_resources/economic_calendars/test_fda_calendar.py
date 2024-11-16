# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import TradesignalsIo, AsyncTradesignalsIo
from tradesignals._utils import parse_date
from tradesignals.types.economic_calendars import FdaCalendarRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFdaCalendar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TradesignalsIo) -> None:
        fda_calendar = client.economic_calendars.fda_calendar.retrieve()
        assert_matches_type(FdaCalendarRetrieveResponse, fda_calendar, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TradesignalsIo) -> None:
        fda_calendar = client.economic_calendars.fda_calendar.retrieve(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            symbol="AAPL",
        )
        assert_matches_type(FdaCalendarRetrieveResponse, fda_calendar, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TradesignalsIo) -> None:
        response = client.economic_calendars.fda_calendar.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fda_calendar = response.parse()
        assert_matches_type(FdaCalendarRetrieveResponse, fda_calendar, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TradesignalsIo) -> None:
        with client.economic_calendars.fda_calendar.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fda_calendar = response.parse()
            assert_matches_type(FdaCalendarRetrieveResponse, fda_calendar, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFdaCalendar:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        fda_calendar = await async_client.economic_calendars.fda_calendar.retrieve()
        assert_matches_type(FdaCalendarRetrieveResponse, fda_calendar, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignalsIo) -> None:
        fda_calendar = await async_client.economic_calendars.fda_calendar.retrieve(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            symbol="AAPL",
        )
        assert_matches_type(FdaCalendarRetrieveResponse, fda_calendar, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        response = await async_client.economic_calendars.fda_calendar.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fda_calendar = await response.parse()
        assert_matches_type(FdaCalendarRetrieveResponse, fda_calendar, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignalsIo) -> None:
        async with async_client.economic_calendars.fda_calendar.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fda_calendar = await response.parse()
            assert_matches_type(FdaCalendarRetrieveResponse, fda_calendar, path=["response"])

        assert cast(Any, response.is_closed) is True
