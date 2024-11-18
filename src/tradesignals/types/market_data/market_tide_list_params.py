# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketTideListParams"]


class MarketTideListParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A trading date in the format of YYYY-MM-DD. Defaults to the last trading date."""

    interval_5m: bool
    """Return data in 5-minute intervals."""

    otm_only: bool
    """Only include out-of-the-money transactions."""
