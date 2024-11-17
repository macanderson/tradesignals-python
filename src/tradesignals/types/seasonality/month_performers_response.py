# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .month_performer_entry import MonthPerformerEntry

__all__ = ["MonthPerformersResponse"]


class MonthPerformersResponse(BaseModel):
    data: Optional[List[MonthPerformerEntry]] = None
