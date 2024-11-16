# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HistoricalRetrieveParams"]


class HistoricalRetrieveParams(TypedDict, total=False):
    end_date: Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]
    """End date for the historical data."""

    expiration: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Option expiration date to filter the data."""

    option_type: Annotated[Literal["CALL", "PUT"], PropertyInfo(alias="optionType")]
    """Option type (CALL or PUT)."""

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """Start date for the historical data."""

    strike: float
    """Option strike price to filter the data."""
