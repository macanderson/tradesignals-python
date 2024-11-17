# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals.types.etf import ExposureRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExposure:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Tradesignals) -> None:
        exposure = client.etf.exposure.retrieve(
            "AAPL",
        )
        assert_matches_type(Optional[ExposureRetrieveResponse], exposure, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Tradesignals) -> None:
        response = client.etf.exposure.with_raw_response.retrieve(
            "AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exposure = response.parse()
        assert_matches_type(Optional[ExposureRetrieveResponse], exposure, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Tradesignals) -> None:
        with client.etf.exposure.with_streaming_response.retrieve(
            "AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exposure = response.parse()
            assert_matches_type(Optional[ExposureRetrieveResponse], exposure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            client.etf.exposure.with_raw_response.retrieve(
                "",
            )


class TestAsyncExposure:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignals) -> None:
        exposure = await async_client.etf.exposure.retrieve(
            "AAPL",
        )
        assert_matches_type(Optional[ExposureRetrieveResponse], exposure, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.etf.exposure.with_raw_response.retrieve(
            "AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exposure = await response.parse()
        assert_matches_type(Optional[ExposureRetrieveResponse], exposure, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        async with async_client.etf.exposure.with_streaming_response.retrieve(
            "AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exposure = await response.parse()
            assert_matches_type(Optional[ExposureRetrieveResponse], exposure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticker` but received ''"):
            await async_client.etf.exposure.with_raw_response.retrieve(
                "",
            )
