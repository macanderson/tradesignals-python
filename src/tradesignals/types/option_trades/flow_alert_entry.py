# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FlowAlertEntry"]


class FlowAlertEntry(BaseModel):
    alert_rule: Optional[str] = None
    """The name of the alert rule."""

    all_opening_trades: Optional[bool] = None

    created_at: Optional[datetime] = None
    """A UTC timestamp."""

    expiry: Optional[date] = None
    """The contract expiry date in ISO format."""

    expiry_count: Optional[int] = None
    """The amount of expiries belonging to the trade.

    This is only greater than 1 if it is a multileg trade.
    """

    has_floor: Optional[bool] = None

    has_multileg: Optional[bool] = None
    """Whether the trade is a multileg trade."""

    has_singleleg: Optional[bool] = None
    """Whether the trade is a singleleg trade."""

    has_sweep: Optional[bool] = None
    """Whether the trade is a sweep."""

    open_interest: Optional[float] = None

    option_chain: Optional[str] = None
    """The option symbol of the contract."""

    price: Optional[float] = None
    """The fill price of the trade."""

    strike: Optional[str] = None
    """The contract strike."""

    ticker: Optional[str] = None
    """The stock ticker."""

    total_ask_side_prem: Optional[float] = None
    """The total ask-side premium."""

    total_bid_side_prem: Optional[float] = None
    """The total bid-side premium."""

    total_premium: Optional[float] = None
    """The total premium."""

    total_size: Optional[int] = None
    """The total size."""

    trade_count: Optional[int] = None
    """The number of trades."""

    type: Optional[Literal["call", "put"]] = None
    """The contract type."""

    underlying_price: Optional[float] = None
    """The price of the underlying asset."""

    volume: Optional[int] = None
    """The trade volume."""

    volume_oi_ratio: Optional[float] = None
    """The volume to open interest ratio."""
