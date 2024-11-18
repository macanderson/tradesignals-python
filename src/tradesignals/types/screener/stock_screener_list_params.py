# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["StockScreenerListParams"]


class StockScreenerListParams(TypedDict, total=False):
    has_dividends: bool

    is_s_p_500: bool

    issue_types: List[Literal["Common Stock", "ETF", "Index", "ADR"]]

    max_marketcap: int

    min_volume: int

    order: Literal["premium", "call_volume", "put_volume", "marketcap"]

    order_direction: Literal["asc", "desc"]
