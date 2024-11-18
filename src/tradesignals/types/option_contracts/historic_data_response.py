# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel

__all__ = ["HistoricDataResponse", "Chain"]


class Chain(BaseModel):
    ask_volume: Optional[int] = None
    """The amount of volume that happened on the ask side."""

    avg_price: Optional[str] = None
    """The volume weighted average fill price of the contract."""

    bid_volume: Optional[int] = None
    """The amount of volume that happened on the bid side."""

    cross_volume: Optional[int] = None
    """The amount of cross volume (transactions with the cross trade code)."""

    date: Optional[datetime.date] = None
    """A trading date in ISO format."""

    floor_volume: Optional[int] = None
    """The amount of floor volume (transactions with the floor trade code)."""

    high_price: Optional[str] = None
    """The highest fill on the contract."""

    implied_volatility: Optional[str] = None
    """The implied volatility for the last transaction."""

    iv_high: Optional[str] = None
    """The highest implied volatility for the contract."""

    iv_low: Optional[str] = None
    """The lowest implied volatility for the contract."""

    last_price: Optional[str] = None
    """The last fill on the contract."""

    last_tape_time: Optional[datetime.datetime] = None
    """The last time there was a transaction for the given contract."""

    low_price: Optional[str] = None
    """The lowest fill on the contract."""

    mid_volume: Optional[int] = None
    """The amount of volume that happened in the middle of the ask and bid."""

    multi_leg_volume: Optional[int] = None
    """The amount of volume as part of a multileg trade."""

    no_side_volume: Optional[int] = None
    """Volume on no identifiable side (e.g., late, out-of-sequence transactions)."""

    open_interest: Optional[int] = None
    """The open interest for the contract."""

    stock_multi_leg_volume: Optional[int] = None
    """Volume as part of stock transactions and possibly other option contracts."""

    sweep_volume: Optional[int] = None
    """Sweep volume (transactions with the sweep trade code)."""

    total_premium: Optional[str] = None
    """The total option premium."""

    trades: Optional[int] = None
    """The total number of transactions for this contract."""

    volume: Optional[int] = None
    """The contract volume."""


class HistoricDataResponse(BaseModel):
    chains: Optional[List[Chain]] = None
