# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .market_tide import MarketTide

__all__ = ["MarketTideResponse"]


class MarketTideResponse(BaseModel):
    data: Optional[List[MarketTide]] = None
