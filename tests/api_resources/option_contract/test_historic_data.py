# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.option_contract import HistoricDataRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistoricData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Tradesignals) -> None:
        historic_data = client.option_contract.historic_data.retrieve(
            id="TSLA230526P00167500",
        )
        assert_matches_type(Optional[HistoricDataRetrieveResponse], historic_data, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Tradesignals) -> None:
        historic_data = client.option_contract.historic_data.retrieve(
            id="TSLA230526P00167500",
            limit=10,
        )
        assert_matches_type(Optional[HistoricDataRetrieveResponse], historic_data, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Tradesignals) -> None:
        response = client.option_contract.historic_data.with_raw_response.retrieve(
            id="TSLA230526P00167500",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        historic_data = response.parse()
        assert_matches_type(Optional[HistoricDataRetrieveResponse], historic_data, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Tradesignals) -> None:
        with client.option_contract.historic_data.with_streaming_response.retrieve(
            id="TSLA230526P00167500",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            historic_data = response.parse()
            assert_matches_type(Optional[HistoricDataRetrieveResponse], historic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.option_contract.historic_data.with_raw_response.retrieve(
                id="",
            )


class TestAsyncHistoricData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignals) -> None:
        historic_data = await async_client.option_contract.historic_data.retrieve(
            id="TSLA230526P00167500",
        )
        assert_matches_type(Optional[HistoricDataRetrieveResponse], historic_data, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignals) -> None:
        historic_data = await async_client.option_contract.historic_data.retrieve(
            id="TSLA230526P00167500",
            limit=10,
        )
        assert_matches_type(Optional[HistoricDataRetrieveResponse], historic_data, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.option_contract.historic_data.with_raw_response.retrieve(
            id="TSLA230526P00167500",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        historic_data = await response.parse()
        assert_matches_type(Optional[HistoricDataRetrieveResponse], historic_data, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        async with async_client.option_contract.historic_data.with_streaming_response.retrieve(
            id="TSLA230526P00167500",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            historic_data = await response.parse()
            assert_matches_type(Optional[HistoricDataRetrieveResponse], historic_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.option_contract.historic_data.with_raw_response.retrieve(
                id="",
            )
