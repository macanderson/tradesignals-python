# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.option_trades import FlowAlertListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFlowAlerts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        flow_alert = client.option_trades.flow_alerts.list()
        assert_matches_type(Optional[FlowAlertListResponse], flow_alert, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.option_trades.flow_alerts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow_alert = response.parse()
        assert_matches_type(Optional[FlowAlertListResponse], flow_alert, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.option_trades.flow_alerts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow_alert = response.parse()
            assert_matches_type(Optional[FlowAlertListResponse], flow_alert, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFlowAlerts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        flow_alert = await async_client.option_trades.flow_alerts.list()
        assert_matches_type(Optional[FlowAlertListResponse], flow_alert, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.option_trades.flow_alerts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        flow_alert = await response.parse()
        assert_matches_type(Optional[FlowAlertListResponse], flow_alert, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.option_trades.flow_alerts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            flow_alert = await response.parse()
            assert_matches_type(Optional[FlowAlertListResponse], flow_alert, path=["response"])

        assert cast(Any, response.is_closed) is True
