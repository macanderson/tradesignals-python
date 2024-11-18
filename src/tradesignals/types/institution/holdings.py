# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Holdings"]


class Holdings(BaseModel):
    avg_price: Optional[str] = None
    """Average price of the security."""

    close: Optional[str] = None
    """The latest stock price of the ticker."""

    date: Optional[datetime.date] = None
    """The date for the holding."""

    first_buy: Optional[datetime.date] = None
    """The date of the first purchase."""

    full_name: Optional[str] = None
    """Full name of the company."""

    historical_units: Optional[List[int]] = None
    """Historical unit counts (max length 8)."""

    price_first_buy: Optional[str] = None
    """Close price of the ticker on the first buy date."""

    put_call: Optional[str] = None
    """Whether the holding is a put or a call (null if neither)."""

    sector: Optional[str] = None
    """Sector of the company."""

    security_type: Optional[str] = None
    """Type of the security (e.g., Share, Fund)."""

    shares_outstanding: Optional[str] = None
    """Total outstanding shares for the ticker."""

    ticker: Optional[str] = None
    """Stock ticker symbol."""

    units: Optional[int] = None
    """Number of units held."""

    units_change: Optional[int] = None
    """Change in units held."""

    value: Optional[int] = None
    """The rounded total value on the reporting date."""
