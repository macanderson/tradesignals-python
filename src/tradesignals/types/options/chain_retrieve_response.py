# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChainRetrieveResponse", "OptionChain"]


class OptionChain(BaseModel):
    ask: Optional[float] = None
    """The current ask price for the option contract."""

    bid: Optional[float] = None
    """The current bid price for the option contract."""

    expiration_date: Optional[date] = None
    """The expiration date of the option contract (YYYY-MM-DD)."""

    last_price: Optional[float] = None
    """The last traded price of the option contract."""

    open_interest: Optional[int] = None
    """The open interest of the option contract."""

    option_symbol: Optional[str] = None
    """The unique identifier for the option contract."""

    option_type: Optional[Literal["CALL", "PUT"]] = None
    """The type of the option contract."""

    strike_price: Optional[float] = None
    """The strike price of the option contract."""

    volume: Optional[int] = None
    """The trading volume of the option contract."""


class ChainRetrieveResponse(BaseModel):
    option_chain: Optional[List[OptionChain]] = None
    """A list of option contracts for the specified symbol."""

    symbol: Optional[str] = None
    """The stock symbol for which the option chain is retrieved."""
