# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["OiChange"]


class OiChange(BaseModel):
    avg_price: Optional[str] = None
    """The average price of the option contract."""

    curr_date: Optional[date] = None
    """The current trading date."""

    curr_oi: Optional[int] = None
    """The current open interest."""

    last_ask: Optional[str] = None
    """The last ask price."""

    last_bid: Optional[str] = None
    """The last bid price."""

    last_date: Optional[date] = None
    """The previous trading date."""

    last_fill: Optional[str] = None
    """The last fill price."""

    last_oi: Optional[int] = None
    """The previous open interest."""

    oi_change: Optional[str] = None
    """The percentage change in open interest."""

    oi_diff_plain: Optional[int] = None
    """The absolute change in open interest."""

    option_symbol: Optional[str] = None
    """The option symbol of the contract."""

    percentage_of_total: Optional[str] = None
    """The percentage of the total open interest change."""

    prev_ask_volume: Optional[int] = None
    """The previous ask volume."""

    prev_bid_volume: Optional[int] = None
    """The previous bid volume."""

    prev_mid_volume: Optional[int] = None
    """The previous midpoint volume."""

    prev_multi_leg_volume: Optional[int] = None
    """The previous multi-leg volume."""

    prev_neutral_volume: Optional[int] = None
    """The previous neutral volume."""

    prev_stock_multi_leg_volume: Optional[int] = None
    """The previous stock multi-leg volume."""

    prev_total_premium: Optional[str] = None
    """The previous total premium."""

    rnk: Optional[int] = None
    """The rank based on OI change."""

    trades: Optional[int] = None
    """The number of trades."""

    underlying_symbol: Optional[str] = None
    """The underlying symbol of the option contract."""

    volume: Optional[int] = None
    """The total volume."""
