# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Trade"]


class Trade(BaseModel):
    canceled: Optional[bool] = None
    """Whether the trade has been cancelled."""

    executed_at: Optional[datetime] = None
    """The time with timezone when a trade was executed."""

    ext_hour_sold_codes: Optional[
        Literal["sold_out_of_sequence", "extended_hours_trade_late_or_out_of_sequence", "extended_hours_trade"]
    ] = None
    """The code describing why the trade happened outside of regular market hours.

    Null if none applies.
    """

    market_center: Optional[str] = None
    """The market center code."""

    nbbo_ask: Optional[str] = None
    """The National Best Bid and Offer ask price."""

    nbbo_ask_quantity: Optional[int] = None
    """The quantity for the NBBO ask."""

    nbbo_bid: Optional[str] = None
    """The National Best Bid and Offer bid price."""

    nbbo_bid_quantity: Optional[int] = None
    """The quantity for the NBBO bid."""

    premium: Optional[str] = None
    """The total option premium."""

    price: Optional[str] = None
    """The price of the trade."""

    sale_cond_codes: Optional[
        Literal["contingent_trade", "odd_lot_execution", "prio_reference_price", "average_price_trade"]
    ] = None
    """The sale condition code. Null if none applies."""

    size: Optional[int] = None
    """The size of the transaction."""

    ticker: Optional[str] = None
    """The stock ticker."""

    tracking_id: Optional[int] = None
    """The tracking ID of the trade."""

    trade_code: Optional[Literal["derivative_priced", "qualified_contingent_trade", "intermarket_sweep"]] = None
    """The trade code. Null if none applies."""

    trade_settlement: Optional[
        Literal["cash_settlement", "next_day_settlement", "seller_settlement", "regular_settlement"]
    ] = None
    """The kind of trade settlement."""

    volume: Optional[int] = None
    """The volume of the ticker for the trading day."""
