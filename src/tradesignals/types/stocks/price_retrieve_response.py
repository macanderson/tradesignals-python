# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PriceRetrieveResponse"]


class PriceRetrieveResponse(BaseModel):
    price: Optional[float] = None

    symbol: Optional[str] = None

    timestamp: Optional[datetime] = None
