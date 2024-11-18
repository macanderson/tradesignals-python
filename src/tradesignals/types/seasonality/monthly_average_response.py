# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .monthly_average_entry import MonthlyAverageEntry

__all__ = ["MonthlyAverageResponse"]


class MonthlyAverageResponse(BaseModel):
    data: Optional[List[MonthlyAverageEntry]] = None
