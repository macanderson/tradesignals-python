# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .insider_buy_sell import InsiderBuySell

__all__ = ["InsiderBuySellsResponse"]


class InsiderBuySellsResponse(BaseModel):
    data: Optional[List[InsiderBuySell]] = None
