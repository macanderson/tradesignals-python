# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AtmChainEntry"]


class AtmChainEntry(BaseModel):
    ask_side_volume: Optional[int] = None

    avg_price: Optional[str] = None

    bid_side_volume: Optional[int] = None

    chain_prev_close: Optional[str] = None

    close: Optional[str] = None

    cross_volume: Optional[int] = None

    er_time: Optional[Literal["unknown", "afterhours", "premarket"]] = None

    floor_volume: Optional[int] = None

    high: Optional[str] = None

    last_fill: Optional[datetime] = None

    low: Optional[str] = None

    mid_volume: Optional[int] = None

    multileg_volume: Optional[int] = None

    next_earnings_date: Optional[date] = None

    no_side_volume: Optional[int] = None

    open: Optional[str] = None

    open_interest: Optional[int] = None

    option_symbol: Optional[str] = None

    premium: Optional[str] = None

    sector: Optional[
        Literal[
            "Basic Materials",
            "Communication Services",
            "Consumer Cyclical",
            "Consumer Defensive",
            "Energy",
            "Financial Services",
            "Healthcare",
            "Industrials",
            "Real Estate",
            "Technology",
            "Utilities",
        ]
    ] = None

    stock_multi_leg_volume: Optional[int] = None

    stock_price: Optional[str] = None

    sweep_volume: Optional[int] = None

    ticker_vol: Optional[int] = None

    total_ask_changes: Optional[int] = None

    total_bid_changes: Optional[int] = None

    trades: Optional[int] = None

    volume: Optional[int] = None
