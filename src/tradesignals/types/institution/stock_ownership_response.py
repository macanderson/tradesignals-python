# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .stock_ownership import StockOwnership

__all__ = ["StockOwnershipResponse"]


class StockOwnershipResponse(BaseModel):
    data: Optional[List[StockOwnership]] = None
