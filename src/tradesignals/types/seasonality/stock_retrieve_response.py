# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StockRetrieveResponse", "SeasonalityData"]


class SeasonalityData(BaseModel):
    average_return: Optional[float] = None

    period: Optional[str] = None

    positive_periods: Optional[int] = None

    total_periods: Optional[int] = None


class StockRetrieveResponse(BaseModel):
    seasonality_data: Optional[List[SeasonalityData]] = None

    symbol: Optional[str] = None

    time_frame: Optional[Literal["daily", "weekly", "monthly", "yearly"]] = None
