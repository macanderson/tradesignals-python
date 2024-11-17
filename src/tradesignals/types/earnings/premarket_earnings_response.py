# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .premarket_earnings_data import PremarketEarningsData

__all__ = ["PremarketEarningsResponse"]


class PremarketEarningsResponse(BaseModel):
    data: Optional[List[PremarketEarningsData]] = None
