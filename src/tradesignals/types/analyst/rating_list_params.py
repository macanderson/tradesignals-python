# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RatingListParams"]


class RatingListParams(TypedDict, total=False):
    action: Literal["initiated", "reiterated", "downgraded", "upgraded", "maintained"]

    limit: int

    recommendation: Literal["buy", "hold", "sell"]

    ticker: str
