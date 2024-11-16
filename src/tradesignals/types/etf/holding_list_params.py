# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HoldingListParams"]


class HoldingListParams(TypedDict, total=False):
    etf: Required[str]
    """ETF symbol to retrieve holdings for."""

    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """Date to filter ETF holdings."""
