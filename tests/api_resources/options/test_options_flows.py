# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.options import (
    OptionsFlowListResponse,
    OptionsFlowRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOptionsFlows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Tradesignals) -> None:
        options_flow = client.options.options_flows.retrieve(
            symbol="AAPL",
        )
        assert_matches_type(OptionsFlowRetrieveResponse, options_flow, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Tradesignals) -> None:
        options_flow = client.options.options_flows.retrieve(
            symbol="AAPL",
            date=parse_date("2019-12-27"),
            max_premium=10,
            min_premium=1,
        )
        assert_matches_type(OptionsFlowRetrieveResponse, options_flow, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Tradesignals) -> None:
        response = client.options.options_flows.with_raw_response.retrieve(
            symbol="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        options_flow = response.parse()
        assert_matches_type(OptionsFlowRetrieveResponse, options_flow, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Tradesignals) -> None:
        with client.options.options_flows.with_streaming_response.retrieve(
            symbol="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            options_flow = response.parse()
            assert_matches_type(OptionsFlowRetrieveResponse, options_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            client.options.options_flows.with_raw_response.retrieve(
                symbol="",
            )

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        options_flow = client.options.options_flows.list()
        assert_matches_type(OptionsFlowListResponse, options_flow, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        options_flow = client.options.options_flows.list(
            date=parse_date("2019-12-27"),
            max_premium=10,
            min_premium=1,
            symbol="AAPL",
        )
        assert_matches_type(OptionsFlowListResponse, options_flow, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.options.options_flows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        options_flow = response.parse()
        assert_matches_type(OptionsFlowListResponse, options_flow, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.options.options_flows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            options_flow = response.parse()
            assert_matches_type(OptionsFlowListResponse, options_flow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOptionsFlows:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignals) -> None:
        options_flow = await async_client.options.options_flows.retrieve(
            symbol="AAPL",
        )
        assert_matches_type(OptionsFlowRetrieveResponse, options_flow, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignals) -> None:
        options_flow = await async_client.options.options_flows.retrieve(
            symbol="AAPL",
            date=parse_date("2019-12-27"),
            max_premium=10,
            min_premium=1,
        )
        assert_matches_type(OptionsFlowRetrieveResponse, options_flow, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.options.options_flows.with_raw_response.retrieve(
            symbol="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        options_flow = await response.parse()
        assert_matches_type(OptionsFlowRetrieveResponse, options_flow, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        async with async_client.options.options_flows.with_streaming_response.retrieve(
            symbol="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            options_flow = await response.parse()
            assert_matches_type(OptionsFlowRetrieveResponse, options_flow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            await async_client.options.options_flows.with_raw_response.retrieve(
                symbol="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        options_flow = await async_client.options.options_flows.list()
        assert_matches_type(OptionsFlowListResponse, options_flow, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        options_flow = await async_client.options.options_flows.list(
            date=parse_date("2019-12-27"),
            max_premium=10,
            min_premium=1,
            symbol="AAPL",
        )
        assert_matches_type(OptionsFlowListResponse, options_flow, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.options.options_flows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        options_flow = await response.parse()
        assert_matches_type(OptionsFlowListResponse, options_flow, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.options.options_flows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            options_flow = await response.parse()
            assert_matches_type(OptionsFlowListResponse, options_flow, path=["response"])

        assert cast(Any, response.is_closed) is True