# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["EquityOwnership"]


class EquityOwnership(BaseModel):
    avg_price: Optional[str] = None
    """Average price of the security."""

    filing_date: Optional[date] = None
    """Filing date for the ownership data."""

    first_buy: Optional[date] = None
    """Date of the first purchase."""

    historical_units: Optional[List[int]] = None
    """Historical unit counts (max length 8)."""

    inst_share_value: Optional[str] = None
    """Rounded total share value in the institution's portfolio."""

    inst_value: Optional[str] = None
    """Rounded total value of the institution's portfolio."""

    name: Optional[str] = None
    """Institution's name."""

    people: Optional[List[str]] = None
    """Persons of interest in the institution."""

    report_date: Optional[date] = None
    """Report date for the ownership data."""

    shares_outstanding: Optional[str] = None
    """Total outstanding shares for the ticker."""

    short_name: Optional[str] = None
    """Institution's short name."""

    tags: Optional[List[str]] = None
    """Tags related to the institution."""

    units: Optional[int] = None
    """Number of units held."""

    units_change: Optional[int] = None
    """Change in units held."""

    value: Optional[int] = None
    """Rounded total value on the reporting date."""
