# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TradeListResponse", "Trade"]


class Trade(BaseModel):
    date: Optional[datetime.date] = None

    institution_name: Optional[str] = None

    shares: Optional[int] = None

    ticker: Optional[str] = None

    value: Optional[float] = None


class TradeListResponse(BaseModel):
    trades: Optional[List[Trade]] = None
