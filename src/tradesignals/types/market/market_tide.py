# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ..._models import BaseModel

__all__ = ["MarketTide"]


class MarketTide(BaseModel):
    date: Optional[datetime.date] = None
    """The trading date."""

    net_call_premium: Optional[str] = None
    """Defined as (call premium ask side) - (call premium bid side)."""

    net_put_premium: Optional[str] = None
    """Defined as (put premium ask side) - (put premium bid side)."""

    net_volume: Optional[int] = None
    """
    Defined as (call volume ask side) - (call volume bid side) - ((put volume ask
    side) - (put volume bid side)).
    """

    timestamp: Optional[datetime.datetime] = None
    """The start time of the tick as a timestamp with timezone."""
