# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InsiderTradeListParams"]


class InsiderTradeListParams(TypedDict, total=False):
    limit: int
    """How many items to return.

    If no limit is given, returns all matching data. Minimum value is 1.
    """
