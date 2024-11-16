# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ContractRetrieveResponse", "Greeks"]


class Greeks(BaseModel):
    delta: Optional[float] = None

    gamma: Optional[float] = None

    option_symbol: Optional[str] = None

    rho: Optional[float] = None

    theta: Optional[float] = None

    vega: Optional[float] = None


class ContractRetrieveResponse(BaseModel):
    ask: Optional[float] = None

    bid: Optional[float] = None

    expiration_date: Optional[date] = None

    greeks: Optional[Greeks] = None

    last_trade_price: Optional[float] = None

    open_interest: Optional[int] = None

    option_symbol: Optional[str] = None

    option_type: Optional[Literal["CALL", "PUT"]] = None

    strike_price: Optional[float] = None

    underlying_symbol: Optional[str] = None

    volume: Optional[int] = None
