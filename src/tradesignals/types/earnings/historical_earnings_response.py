# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .historical_earnings_data import HistoricalEarningsData

__all__ = ["HistoricalEarningsResponse"]


class HistoricalEarningsResponse(BaseModel):
    data: Optional[List[HistoricalEarningsData]] = None
