# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["InstitutionListParams"]


class InstitutionListParams(TypedDict, total=False):
    limit: int
    """How many items to return. Default 500. Max 500. Min 1."""

    max_share_value: str
    """The maximum share value for the query."""

    max_total_value: str
    """The maximum total value for the query."""

    min_share_value: str
    """The minimum share value for the query."""

    min_total_value: str
    """The minimum total value for the query."""

    name: str
    """A large entity that manages funds and investments for others.

    Queryable by name or CIK.
    """

    order: Literal[
        "name",
        "call_value",
        "put_value",
        "share_value",
        "call_holdings",
        "put_holdings",
        "share_holdings",
        "total_value",
        "warrant_value",
        "fund_value",
        "pfd_value",
        "debt_value",
        "total_holdings",
        "warrant_holdings",
        "fund_holdings",
        "pfd_holdings",
        "debt_holdings",
        "percent_of_total",
        "date",
        "buy_value",
        "sell_value",
    ]
    """Optional columns to order the result by."""

    order_direction: Literal["desc", "asc"]
    """Whether to sort descending or ascending. Default is descending."""

    page: int
    """Page number (use with limit). Starts on page 0."""

    tags: List[str]
    """An array of institution tags."""
