# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EquityOwnershipListParams"]


class EquityOwnershipListParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A trading date in the format of YYYY-MM-DD.

    Defaults to the last trading date if not provided.
    """

    limit: int
    """How many items to return. Default 500. Max 500. Min 1."""

    order: Literal[
        "name",
        "short_name",
        "first_buy",
        "units",
        "units_change",
        "units_changed",
        "value",
        "avg_price",
        "perc_outstanding",
        "perc_units_changed",
        "activity",
        "perc_inst_value",
        "perc_share_value",
    ]
    """Optional columns to order the result by."""

    order_direction: Literal["desc", "asc"]
    """Whether to sort descending or ascending. Default is descending."""

    page: int
    """Page number (use with limit). Starts on page 0."""

    tags: List[str]
    """An array of institution tags."""
