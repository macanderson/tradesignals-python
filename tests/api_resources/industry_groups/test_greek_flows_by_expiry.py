# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.industry_groups import GreekFlowsByExpiryListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGreekFlowsByExpiry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        greek_flows_by_expiry = client.industry_groups.greek_flows_by_expiry.list(
            expiry=parse_date("2019-12-27"),
            flow_group="airline",
        )
        assert_matches_type(Optional[GreekFlowsByExpiryListResponse], greek_flows_by_expiry, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        greek_flows_by_expiry = client.industry_groups.greek_flows_by_expiry.list(
            expiry=parse_date("2019-12-27"),
            flow_group="airline",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(Optional[GreekFlowsByExpiryListResponse], greek_flows_by_expiry, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.industry_groups.greek_flows_by_expiry.with_raw_response.list(
            expiry=parse_date("2019-12-27"),
            flow_group="airline",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        greek_flows_by_expiry = response.parse()
        assert_matches_type(Optional[GreekFlowsByExpiryListResponse], greek_flows_by_expiry, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.industry_groups.greek_flows_by_expiry.with_streaming_response.list(
            expiry=parse_date("2019-12-27"),
            flow_group="airline",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            greek_flows_by_expiry = response.parse()
            assert_matches_type(Optional[GreekFlowsByExpiryListResponse], greek_flows_by_expiry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expiry` but received ''"):
            client.industry_groups.greek_flows_by_expiry.with_raw_response.list(
                expiry="",
                flow_group="airline",
            )


class TestAsyncGreekFlowsByExpiry:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        greek_flows_by_expiry = await async_client.industry_groups.greek_flows_by_expiry.list(
            expiry=parse_date("2019-12-27"),
            flow_group="airline",
        )
        assert_matches_type(Optional[GreekFlowsByExpiryListResponse], greek_flows_by_expiry, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        greek_flows_by_expiry = await async_client.industry_groups.greek_flows_by_expiry.list(
            expiry=parse_date("2019-12-27"),
            flow_group="airline",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(Optional[GreekFlowsByExpiryListResponse], greek_flows_by_expiry, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.industry_groups.greek_flows_by_expiry.with_raw_response.list(
            expiry=parse_date("2019-12-27"),
            flow_group="airline",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        greek_flows_by_expiry = await response.parse()
        assert_matches_type(Optional[GreekFlowsByExpiryListResponse], greek_flows_by_expiry, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.industry_groups.greek_flows_by_expiry.with_streaming_response.list(
            expiry=parse_date("2019-12-27"),
            flow_group="airline",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            greek_flows_by_expiry = await response.parse()
            assert_matches_type(Optional[GreekFlowsByExpiryListResponse], greek_flows_by_expiry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `expiry` but received ''"):
            await async_client.industry_groups.greek_flows_by_expiry.with_raw_response.list(
                expiry="",
                flow_group="airline",
            )
