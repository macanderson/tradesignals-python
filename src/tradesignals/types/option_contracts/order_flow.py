# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OrderFlow"]


class OrderFlow(BaseModel):
    id: Optional[str] = None
    """The ID of the option trade."""

    delta: Optional[str] = None
    """Delta value for the option trade."""

    executed_at: Optional[datetime] = None
    """The time the option trade was executed."""

    expiry: Optional[date] = None
    """The contract expiry date."""

    implied_volatility: Optional[str] = None
    """Implied volatility of the option trade."""

    nbbo_ask: Optional[str] = None
    """National Best Bid and Offer (NBBO) ask price."""

    nbbo_bid: Optional[str] = None
    """National Best Bid and Offer (NBBO) bid price."""

    open_interest: Optional[int] = None
    """The open interest for the contract."""

    option_type: Optional[Literal["call", "put"]] = None
    """The option type of the contract."""

    premium: Optional[str] = None
    """The premium of the option trade."""

    price: Optional[str] = None
    """The fill price of the option trade."""

    sector: Optional[str] = None
    """The financial sector of the ticker."""

    size: Optional[int] = None
    """The size of the option trade."""

    strike: Optional[str] = None
    """The contract strike price."""

    tags: Optional[List[str]] = None
    """Tags related to the trade."""

    underlying_symbol: Optional[str] = None
    """The underlying symbol of the contract."""

    upstream_condition_detail: Optional[str] = None
    """The upstream condition detail/trade code."""

    volume: Optional[int] = None
    """The number of contracts traded till this point."""
