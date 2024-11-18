# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ..._models import BaseModel

__all__ = ["TickerOptionsVolume"]


class TickerOptionsVolume(BaseModel):
    avg_3_day_call_volume: Optional[str] = None
    """Avg 3 day call volume."""

    avg_3_day_put_volume: Optional[str] = None
    """Avg 3 day put volume."""

    avg_30_day_call_volume: Optional[str] = None
    """Avg 30 day call volume."""

    avg_30_day_put_volume: Optional[str] = None
    """Avg 30 day put volume."""

    avg_7_day_call_volume: Optional[str] = None
    """Avg 7 day call volume."""

    avg_7_day_put_volume: Optional[str] = None
    """Avg 7 day put volume."""

    bearish_premium: Optional[str] = None
    """The bearish premium (call bid + put ask)."""

    bullish_premium: Optional[str] = None
    """The bullish premium (call ask + put bid)."""

    call_open_interest: Optional[int] = None
    """The sum of open interest for all call options."""

    call_premium: Optional[str] = None
    """The sum of premium for all call transactions."""

    call_volume: Optional[int] = None
    """The total call volume."""

    call_volume_ask_side: Optional[int] = None
    """The call volume on the ask side."""

    call_volume_bid_side: Optional[int] = None
    """The call volume on the bid side."""

    date: Optional[datetime.date] = None
    """The trading date."""

    net_call_premium: Optional[str] = None
    """Net call premium (ask - bid)."""

    net_put_premium: Optional[str] = None
    """Net put premium (ask - bid)."""

    put_open_interest: Optional[int] = None
    """The sum of open interest for all put options."""

    put_premium: Optional[str] = None
    """The sum of premium for all put transactions."""

    put_volume: Optional[int] = None
    """The total put volume."""

    put_volume_ask_side: Optional[int] = None
    """The put volume on the ask side."""

    put_volume_bid_side: Optional[int] = None
    """The put volume on the bid side."""
