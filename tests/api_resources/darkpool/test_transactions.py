# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tradesignals import Tradesignals, AsyncTradesignals
from tradesignals._utils import parse_date
from tradesignals.types.darkpool import (
    TransactionListResponse,
    TransactionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Tradesignals) -> None:
        transaction = client.darkpool.transactions.retrieve(
            symbol="symbol",
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Tradesignals) -> None:
        transaction = client.darkpool.transactions.retrieve(
            symbol="symbol",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Tradesignals) -> None:
        response = client.darkpool.transactions.with_raw_response.retrieve(
            symbol="symbol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Tradesignals) -> None:
        with client.darkpool.transactions.with_streaming_response.retrieve(
            symbol="symbol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Tradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            client.darkpool.transactions.with_raw_response.retrieve(
                symbol="",
            )

    @parametrize
    def test_method_list(self, client: Tradesignals) -> None:
        transaction = client.darkpool.transactions.list()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Tradesignals) -> None:
        transaction = client.darkpool.transactions.list(
            date=parse_date("2019-12-27"),
            symbol="symbol",
        )
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Tradesignals) -> None:
        response = client.darkpool.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Tradesignals) -> None:
        with client.darkpool.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionListResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTradesignals) -> None:
        transaction = await async_client.darkpool.transactions.retrieve(
            symbol="symbol",
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTradesignals) -> None:
        transaction = await async_client.darkpool.transactions.retrieve(
            symbol="symbol",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.darkpool.transactions.with_raw_response.retrieve(
            symbol="symbol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTradesignals) -> None:
        async with async_client.darkpool.transactions.with_streaming_response.retrieve(
            symbol="symbol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTradesignals) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            await async_client.darkpool.transactions.with_raw_response.retrieve(
                symbol="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncTradesignals) -> None:
        transaction = await async_client.darkpool.transactions.list()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTradesignals) -> None:
        transaction = await async_client.darkpool.transactions.list(
            date=parse_date("2019-12-27"),
            symbol="symbol",
        )
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTradesignals) -> None:
        response = await async_client.darkpool.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionListResponse, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTradesignals) -> None:
        async with async_client.darkpool.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionListResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
