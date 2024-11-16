# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types import OptionsTotalVolumeListResponse
from tradesignals._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptionsTotalVolumes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        options_total_volume = client.options_total_volumes.list()
        assert_matches_type(OptionsTotalVolumeListResponse, options_total_volume, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        options_total_volume = client.options_total_volumes.list(
            date=parse_date("2019-12-27"),
            symbol="AAPL",
        )
        assert_matches_type(OptionsTotalVolumeListResponse, options_total_volume, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.options_total_volumes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        options_total_volume = response.parse()
        assert_matches_type(OptionsTotalVolumeListResponse, options_total_volume, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.options_total_volumes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            options_total_volume = response.parse()
            assert_matches_type(OptionsTotalVolumeListResponse, options_total_volume, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOptionsTotalVolumes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        options_total_volume = await async_client.options_total_volumes.list()
        assert_matches_type(OptionsTotalVolumeListResponse, options_total_volume, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        options_total_volume = await async_client.options_total_volumes.list(
            date=parse_date("2019-12-27"),
            symbol="AAPL",
        )
        assert_matches_type(OptionsTotalVolumeListResponse, options_total_volume, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.options_total_volumes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        options_total_volume = await response.parse()
        assert_matches_type(OptionsTotalVolumeListResponse, options_total_volume, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.options_total_volumes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            options_total_volume = await response.parse()
            assert_matches_type(OptionsTotalVolumeListResponse, options_total_volume, path=["response"])

        assert cast(Any, response.is_closed) is True
