# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel

__all__ = ["HistoricalRetrieveResponse", "Data"]


class Data(BaseModel):
    close: Optional[float] = None

    date: Optional[datetime.date] = None

    high: Optional[float] = None

    low: Optional[float] = None

    open: Optional[float] = None

    open_interest: Optional[int] = None

    option_symbol: Optional[str] = None

    volume: Optional[int] = None


class HistoricalRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None
