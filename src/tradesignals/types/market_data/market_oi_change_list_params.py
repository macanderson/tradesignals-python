# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketOiChangeListParams"]


class MarketOiChangeListParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A trading date in the format of YYYY-MM-DD. Defaults to the last trading date."""

    limit: int
    """How many items to return. Default is 100. Max is 200. Min is 1."""

    order: Literal["desc", "asc"]
    """Whether to sort descending or ascending. Default is descending."""
