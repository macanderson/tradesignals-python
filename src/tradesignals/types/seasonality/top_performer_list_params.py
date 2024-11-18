# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TopPerformerListParams"]


class TopPerformerListParams(TypedDict, total=False):
    limit: int

    min_oi: int

    min_years: int

    order: Literal[
        "ticker",
        "month",
        "positive_closes",
        "years",
        "positive_months_perc",
        "median_change",
        "avg_change",
        "max_change",
        "min_change",
    ]

    order_direction: Literal["asc", "desc"]

    s_p_500_nasdaq_only: bool

    ticker_for_sector: str
