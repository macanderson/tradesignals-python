# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FdaCalendarRetrieveParams"]


class FdaCalendarRetrieveParams(TypedDict, total=False):
    end_date: Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]
    """End date for the FDA calendar data."""

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """Start date for the FDA calendar data."""

    symbol: str
    """Stock symbol to filter FDA events."""
