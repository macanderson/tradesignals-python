# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["GreekRetrieveResponse", "Greek"]


class Greek(BaseModel):
    delta: Optional[float] = None

    gamma: Optional[float] = None

    option_symbol: Optional[str] = None

    rho: Optional[float] = None

    theta: Optional[float] = None

    vega: Optional[float] = None


class GreekRetrieveResponse(BaseModel):
    greeks: Optional[List[Greek]] = None
