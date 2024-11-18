# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TickerOptionContract"]


class TickerOptionContract(BaseModel):
    ask_volume: Optional[int] = None
    """The amount of volume that happened on the ask side."""

    avg_price: Optional[str] = None
    """The volume weighted average fill price of the contract."""

    bid_volume: Optional[int] = None
    """The amount of volume that happened on the bid side."""

    cross_volume: Optional[int] = None
    """The amount of cross volume.

    Cross volume consists of all transactions that have the cross trade code.
    """

    floor_volume: Optional[int] = None
    """The amount of floor volume.

    Floor volume consists of all transactions that have the floor trade code.
    """

    high_price: Optional[str] = None
    """The highest fill on that contract."""

    implied_volatility: Optional[str] = None
    """The implied volatility for the last transaction."""

    last_price: Optional[str] = None
    """The last fill on the contract."""

    low_price: Optional[str] = None
    """The lowest fill on that contract."""

    mid_volume: Optional[int] = None
    """The amount of volume that happened in the middle of the ask and bid."""

    multi_leg_volume: Optional[int] = None
    """
    The amount of volume that happened as part of a multileg trade with another
    contract. This can be spreads, rolls, condors, butterflies, and more.
    """

    nbbo_ask: Optional[str] = None
    """The National Best Bid and Offer (NBBO) ask price."""

    nbbo_bid: Optional[str] = None
    """The National Best Bid and Offer (NBBO) bid price."""

    no_side_volume: Optional[int] = None
    """The amount of volume that happened on no identifiable side.

    This can be late, out of sequence, and/or cross transactions.
    """

    open_interest: Optional[int] = None
    """The open interest for the contract."""

    option_symbol: Optional[str] = None
    """The option symbol of the contract."""

    prev_oi: Optional[int] = None
    """The previous trading day's open interest."""

    stock_multi_leg_volume: Optional[int] = None
    """
    The amount of volume that happened as part of a stock transaction and possibly
    other option contracts. This can be covered calls and more.
    """

    sweep_volume: Optional[int] = None
    """The amount of sweep volume.

    Sweep volume consists of all transactions that have the sweep trade code.
    """

    total_premium: Optional[str] = None
    """The total option premium."""

    volume: Optional[int] = None
    """The contract volume."""
