# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .year_month_entry import YearMonthEntry

__all__ = ["YearMonthResponse"]


class YearMonthResponse(BaseModel):
    data: Optional[List[YearMonthEntry]] = None
