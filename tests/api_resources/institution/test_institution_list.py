# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.institution import InstitutionListListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstitutionList:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        institution_list = client.institution.institution_list.list()
        assert_matches_type(Optional[InstitutionListListResponse], institution_list, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        institution_list = client.institution.institution_list.list(
            limit=10,
            max_share_value="10.0",
            max_total_value="10.0",
            min_share_value="0.5",
            min_total_value="0.5",
            name="VANGUARD GROUP INC",
            order="name",
            order_direction="desc",
            page=1,
            tags=["activist"],
        )
        assert_matches_type(Optional[InstitutionListListResponse], institution_list, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.institution.institution_list.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        institution_list = response.parse()
        assert_matches_type(Optional[InstitutionListListResponse], institution_list, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.institution.institution_list.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            institution_list = response.parse()
            assert_matches_type(Optional[InstitutionListListResponse], institution_list, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInstitutionList:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        institution_list = await async_client.institution.institution_list.list()
        assert_matches_type(Optional[InstitutionListListResponse], institution_list, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        institution_list = await async_client.institution.institution_list.list(
            limit=10,
            max_share_value="10.0",
            max_total_value="10.0",
            min_share_value="0.5",
            min_total_value="0.5",
            name="VANGUARD GROUP INC",
            order="name",
            order_direction="desc",
            page=1,
            tags=["activist"],
        )
        assert_matches_type(Optional[InstitutionListListResponse], institution_list, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.institution.institution_list.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        institution_list = await response.parse()
        assert_matches_type(Optional[InstitutionListListResponse], institution_list, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.institution.institution_list.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            institution_list = await response.parse()
            assert_matches_type(Optional[InstitutionListListResponse], institution_list, path=["response"])

        assert cast(Any, response.is_closed) is True
