# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OrderFlowRetrieveParams"]


class OrderFlowRetrieveParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """A trading date in the format YYYY-MM-DD. Defaults to the last trading date."""

    limit: int
    """The number of items to return. Minimum is 1."""

    min_premium: int
    """The minimum premium requested trades should have. Defaults to 0."""

    side: Literal["ALL", "ASK", "BID", "MID"]
    """The side of a stock trade. Defaults to ALL."""
