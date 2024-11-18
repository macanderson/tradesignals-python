# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SectorEtfData"]


class SectorEtfData(BaseModel):
    bearish_premium: Optional[str] = None
    """Bearish premium defined as (call premium bid side) + (put premium ask side)."""

    bullish_premium: Optional[str] = None
    """Bullish premium defined as (call premium ask side) + (put premium bid side)."""

    call_premium: Optional[str] = None
    """The total call premium."""

    call_volume: Optional[int] = None
    """The call volume for the ETF."""

    full_name: Optional[str] = None
    """The full name of the SPDR sector ETF."""

    marketcap: Optional[str] = None
    """The market cap or AUM of the ETF."""

    put_premium: Optional[str] = None
    """The total put premium."""

    put_volume: Optional[int] = None
    """The put volume for the ETF."""

    ticker: Optional[str] = None
    """The ETF ticker."""

    volume: Optional[int] = None
    """The trading volume of the ETF."""
