# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel

__all__ = ["HistoricalRetrieveResponse", "HistoricalData"]


class HistoricalData(BaseModel):
    adjusted_close: Optional[float] = None

    close: Optional[float] = None

    date: Optional[datetime.date] = None

    high: Optional[float] = None

    low: Optional[float] = None

    open: Optional[float] = None

    volume: Optional[int] = None


class HistoricalRetrieveResponse(BaseModel):
    historical_data: Optional[List[HistoricalData]] = None

    symbol: Optional[str] = None
