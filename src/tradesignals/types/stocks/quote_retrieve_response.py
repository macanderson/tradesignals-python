# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["QuoteRetrieveResponse"]


class QuoteRetrieveResponse(BaseModel):
    high: Optional[float] = None

    low: Optional[float] = None

    open: Optional[float] = None

    previous_close: Optional[float] = None

    price: Optional[float] = None

    symbol: Optional[str] = None

    timestamp: Optional[datetime] = None

    volume: Optional[int] = None
