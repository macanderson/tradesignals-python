# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["EarningRetrieveResponse", "EarningsHistory"]


class EarningsHistory(BaseModel):
    estimated_eps: Optional[float] = None

    fiscal_date_ending: Optional[date] = None

    reported_eps: Optional[float] = None

    surprise_percentage: Optional[float] = None


class EarningRetrieveResponse(BaseModel):
    earnings_history: Optional[List[EarningsHistory]] = None

    symbol: Optional[str] = None
