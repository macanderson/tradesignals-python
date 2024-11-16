# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["TradeListResponse", "Trade"]


class Trade(BaseModel):
    amount: Optional[str] = None

    asset_description: Optional[str] = None

    comment: Optional[str] = None

    member_name: Optional[str] = None

    owner: Optional[str] = None

    ticker: Optional[str] = None

    transaction_date: Optional[date] = None

    transaction_type: Optional[str] = None


class TradeListResponse(BaseModel):
    trades: Optional[List[Trade]] = None
