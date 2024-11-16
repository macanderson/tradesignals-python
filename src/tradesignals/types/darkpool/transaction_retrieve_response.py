# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TransactionRetrieveResponse", "Transaction"]


class Transaction(BaseModel):
    price: Optional[float] = None

    symbol: Optional[str] = None

    trade_time: Optional[datetime] = None

    venue: Optional[str] = None

    volume: Optional[int] = None


class TransactionRetrieveResponse(BaseModel):
    transactions: Optional[List[Transaction]] = None
