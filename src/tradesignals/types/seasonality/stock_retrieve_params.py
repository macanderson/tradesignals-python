# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StockRetrieveParams"]


class StockRetrieveParams(TypedDict, total=False):
    time_frame: Annotated[Literal["daily", "weekly", "monthly", "yearly"], PropertyInfo(alias="timeFrame")]
    """Time frame for seasonality data (e.g., 'monthly', 'weekly')."""
