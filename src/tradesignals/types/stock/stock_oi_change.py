# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["StockOiChange"]


class StockOiChange(BaseModel):
    avg_price: Optional[str] = None

    curr_date: Optional[date] = None

    curr_oi: Optional[int] = None

    last_ask: Optional[str] = None

    last_bid: Optional[str] = None

    last_date: Optional[date] = None

    last_fill: Optional[str] = None

    last_oi: Optional[int] = None

    oi_change: Optional[str] = None

    oi_diff_plain: Optional[int] = None

    option_symbol: Optional[str] = None

    percentage_of_total: Optional[str] = None

    prev_ask_volume: Optional[int] = None

    prev_bid_volume: Optional[int] = None

    prev_mid_volume: Optional[int] = None

    prev_multi_leg_volume: Optional[int] = None

    prev_neutral_volume: Optional[int] = None

    prev_stock_multi_leg_volume: Optional[int] = None

    prev_total_premium: Optional[str] = None

    rnk: Optional[int] = None

    trades: Optional[int] = None

    underlying_symbol: Optional[str] = None

    volume: Optional[int] = None
