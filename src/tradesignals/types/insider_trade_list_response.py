# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InsiderTradeListResponse", "Trade"]


class Trade(BaseModel):
    date: Optional[datetime.date] = None

    insider: Optional[str] = None

    shares_traded: Optional[int] = FieldInfo(alias="sharesTraded", default=None)

    symbol: Optional[str] = None

    trade_price: Optional[float] = FieldInfo(alias="tradePrice", default=None)

    transaction_type: Optional[Literal["Buy", "Sell"]] = FieldInfo(alias="transactionType", default=None)


class InsiderTradeListResponse(BaseModel):
    trades: Optional[List[Trade]] = None
