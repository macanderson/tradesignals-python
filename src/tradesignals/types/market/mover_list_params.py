# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MoverListParams"]


class MoverListParams(TypedDict, total=False):
    limit: int
    """Number of records to retrieve."""

    type: Literal["gainers", "losers"]
    """Type of movers to retrieve ('gainers' or 'losers')."""
