# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FlowListParams"]


class FlowListParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """Date to filter the options flow data. ISO 8601 format."""

    max_premium: Annotated[float, PropertyInfo(alias="maxPremium")]
    """Maximum premium to filter the options flow data."""

    min_premium: Annotated[float, PropertyInfo(alias="minPremium")]
    """Minimum premium to filter the options flow data."""

    symbol: str
    """Stock symbol to filter the options flow data."""
