# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .stock_entry import StockEntry

__all__ = ["StockScreenerResponse"]


class StockScreenerResponse(BaseModel):
    data: Optional[List[StockEntry]] = None
