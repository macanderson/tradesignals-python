# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["Activity"]


class Activity(BaseModel):
    avg_price: Optional[str] = None
    """Average price of the security."""

    buy_price: Optional[str] = None
    """Buy price of the security."""

    close: Optional[str] = None
    """The latest stock price of the ticker."""

    filing_date: Optional[date] = None
    """Filing date for the activity."""

    price_on_filing: Optional[str] = None
    """The security price on the filing date."""

    price_on_report: Optional[str] = None
    """The security price on the report date."""

    put_call: Optional[str] = None
    """Whether the holding is a put or a call (null if neither)."""

    report_date: Optional[date] = None
    """Report date for the activity."""

    security_type: Optional[str] = None
    """Type of the security (e.g., Share, Fund)."""

    sell_price: Optional[str] = None
    """Sell price of the security."""

    shares_outstanding: Optional[str] = None
    """Total outstanding shares for the ticker."""

    ticker: Optional[str] = None
    """Stock ticker symbol."""

    units: Optional[int] = None
    """Number of units involved in the activity."""

    units_change: Optional[int] = None
    """Change in units held."""
