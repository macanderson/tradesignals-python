# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TradesByTickerListParams"]


class TradesByTickerListParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """Date to filter darkpool transactions."""

    limit: int
    """How many items to return. Default is 100. Max is 200. Minimum is 1."""

    newer_than: str
    """
    The unix time in milliseconds or seconds at which no older results will be
    returned. Can be used with newer_than to paginate by time. Also accepts an ISO
    date example "2024-01-25".
    """

    older_than: str
    """
    The unix time in milliseconds or seconds at which no newer results will be
    returned. Can be used with newer_than to paginate by time. Also accepts an ISO
    date example "2024-01-25".
    """
