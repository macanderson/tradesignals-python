# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .seasonality_entry import SeasonalityEntry

__all__ = ["MarketSeasonalityResponse"]


class MarketSeasonalityResponse(BaseModel):
    data: Optional[List[SeasonalityEntry]] = None
