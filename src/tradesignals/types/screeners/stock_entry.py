# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StockEntry"]


class StockEntry(BaseModel):
    avg_30_day_call_volume: Optional[str] = None

    avg_30_day_put_volume: Optional[str] = None

    call_premium: Optional[str] = None

    call_volume: Optional[int] = None

    close: Optional[str] = None

    implied_move: Optional[str] = None

    implied_move_perc: Optional[str] = None

    iv_rank: Optional[str] = None

    marketcap: Optional[str] = None

    next_dividend_date: Optional[date] = None

    next_earnings_date: Optional[date] = None

    put_premium: Optional[str] = None

    put_volume: Optional[int] = None

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

    ticker: Optional[str] = None

    total_open_interest: Optional[int] = None

    volatility: Optional[str] = None

    week_52_high: Optional[str] = None

    week_52_low: Optional[str] = None
