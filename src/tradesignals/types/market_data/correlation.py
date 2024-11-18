# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["Correlation"]


class Correlation(BaseModel):
    correlation: Optional[float] = None
    """The correlation value."""

    fst: Optional[str] = None
    """The first stock ticker."""

    max_date: Optional[date] = None
    """The latest date of the data points considered."""

    min_date: Optional[date] = None
    """The earliest date of the data points considered."""

    rows: Optional[int] = None
    """The number of data points considered."""

    snd: Optional[str] = None
    """The second stock ticker."""
