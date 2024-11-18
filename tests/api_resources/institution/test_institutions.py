# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.institution import InstitutionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstitutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        institution = client.institution.institutions.list()
        assert_matches_type(Optional[InstitutionListResponse], institution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        institution = client.institution.institutions.list(
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
        assert_matches_type(Optional[InstitutionListResponse], institution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.institution.institutions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        institution = response.parse()
        assert_matches_type(Optional[InstitutionListResponse], institution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.institution.institutions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            institution = response.parse()
            assert_matches_type(Optional[InstitutionListResponse], institution, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInstitutions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        institution = await async_client.institution.institutions.list()
        assert_matches_type(Optional[InstitutionListResponse], institution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        institution = await async_client.institution.institutions.list(
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
        assert_matches_type(Optional[InstitutionListResponse], institution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.institution.institutions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        institution = await response.parse()
        assert_matches_type(Optional[InstitutionListResponse], institution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.institution.institutions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            institution = await response.parse()
            assert_matches_type(Optional[InstitutionListResponse], institution, path=["response"])

        assert cast(Any, response.is_closed) is True
