# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Info"]


class Info(BaseModel):
    aum: Optional[str] = None
    """The total assets under management (AUM) of the ETF."""

    avg30_volume: Optional[str] = None
    """The avg stock volume for the stock last 30 days."""

    call_vol: Optional[int] = None
    """The sum of the size of all the call transactions that executed."""

    description: Optional[str] = None
    """Information about the ETF."""

    domicile: Optional[str] = None
    """The domicile of the ETF."""

    etf_company: Optional[str] = None
    """The company which oversees the ETF."""

    expense_ratio: Optional[str] = None
    """The expense ratio of the ETF."""

    has_options: Optional[bool] = None
    """Boolean flag whether the company has options."""

    holdings_count: Optional[int] = None
    """The amount of holdings the ETF has."""

    inception_date: Optional[str] = None
    """The inception date of the ETF as an ISO date."""

    name: Optional[str] = None
    """The full name of the ETF."""

    opt_vol: Optional[int] = None
    """The total options volume traded for the last trading day."""

    put_vol: Optional[int] = None
    """The sum of the size of all the put transactions that executed."""

    stock_vol: Optional[int] = None
    """The volume of the ticker for the trading day."""

    website: Optional[str] = None
    """A link to the website of the ETF."""
