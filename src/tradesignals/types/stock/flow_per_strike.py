# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ..._models import BaseModel

__all__ = ["FlowPerStrike"]


class FlowPerStrike(BaseModel):
    call_premium: Optional[str] = None

    call_premium_ask_side: Optional[str] = None

    call_premium_bid_side: Optional[str] = None

    call_trades: Optional[int] = None

    call_volume: Optional[int] = None

    call_volume_ask_side: Optional[int] = None

    call_volume_bid_side: Optional[int] = None

    date: Optional[datetime.date] = None

    put_premium: Optional[str] = None

    put_premium_ask_side: Optional[str] = None

    put_premium_bid_side: Optional[str] = None

    put_trades: Optional[int] = None

    put_volume: Optional[int] = None

    put_volume_ask_side: Optional[int] = None

    put_volume_bid_side: Optional[int] = None

    strike: Optional[str] = None

    ticker: Optional[str] = None

    timestamp: Optional[datetime.datetime] = None
