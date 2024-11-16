# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoricalRetrieveParams"]


class HistoricalRetrieveParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]]
    """End date for the historical data."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """Start date for the historical data."""

    interval: Literal["1m", "5m", "15m", "30m", "1h", "1d", "1wk", "1mo"]
    """Data interval (e.g., '1d', '1wk', '1mo')."""
