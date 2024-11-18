# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Institution"]


class Institution(BaseModel):
    buy_value: Optional[str] = None
    """Rounded total buy value in the institution's portfolio."""

    call_holdings: Optional[str] = None
    """Number of call units in the institution's portfolio."""

    call_value: Optional[str] = None
    """Rounded total call value in the institution's portfolio."""

    cik: Optional[str] = None
    """The institution's CIK."""

    date: Optional[datetime.date] = None
    """End date of the report period in ISO format."""

    debt_holdings: Optional[str] = None
    """Number of debt units in the institution's portfolio."""

    debt_value: Optional[str] = None
    """Rounded total debt value in the institution's portfolio."""

    filing_date: Optional[datetime.date] = None
    """Latest filing date in ISO format."""

    fund_holdings: Optional[str] = None
    """Number of fund units in the institution's portfolio."""

    fund_value: Optional[str] = None
    """Rounded total fund value in the institution's portfolio."""

    is_hedge_fund: Optional[bool] = None
    """Indicates whether the institution is a hedge fund."""

    name: Optional[str] = None
    """The institution's name."""

    people: Optional[List[str]] = None
    """Persons of interest in the institution."""

    pfd_holdings: Optional[str] = None
    """Number of preferred share units in the institution's portfolio."""

    pfd_value: Optional[str] = None
    """Rounded total preferred share value in the institution's portfolio."""

    put_holdings: Optional[str] = None
    """Number of put units in the institution's portfolio."""

    put_value: Optional[str] = None
    """Rounded total put value in the institution's portfolio."""

    sell_value: Optional[str] = None
    """Rounded total sell value in the institution's portfolio."""

    share_value: Optional[str] = None
    """Rounded total share value in the institution's portfolio."""

    short_name: Optional[str] = None
    """The institution's short name."""

    tags: Optional[List[str]] = None
    """Tags related to the institution."""

    total_value: Optional[str] = None
    """Rounded total value of the institution's portfolio."""

    warrant_holdings: Optional[str] = None
    """Number of warrant units in the institution's portfolio."""

    warrant_value: Optional[str] = None
    """Rounded total warrant value in the institution's portfolio."""
