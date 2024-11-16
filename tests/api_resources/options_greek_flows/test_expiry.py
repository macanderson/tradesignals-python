# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExpiry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        expiry = client.options_greek_flows.expiry.list()
        assert_matches_type(object, expiry, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        expiry = client.options_greek_flows.expiry.list(
            date=parse_date("2019-12-27"),
            expiration=parse_date("2019-12-27"),
            symbol="AAPL",
        )
        assert_matches_type(object, expiry, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.options_greek_flows.expiry.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expiry = response.parse()
        assert_matches_type(object, expiry, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.options_greek_flows.expiry.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expiry = response.parse()
            assert_matches_type(object, expiry, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExpiry:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        expiry = await async_client.options_greek_flows.expiry.list()
        assert_matches_type(object, expiry, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        expiry = await async_client.options_greek_flows.expiry.list(
            date=parse_date("2019-12-27"),
            expiration=parse_date("2019-12-27"),
            symbol="AAPL",
        )
        assert_matches_type(object, expiry, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.options_greek_flows.expiry.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        expiry = await response.parse()
        assert_matches_type(object, expiry, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.options_greek_flows.expiry.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            expiry = await response.parse()
            assert_matches_type(object, expiry, path=["response"])

        assert cast(Any, response.is_closed) is True
