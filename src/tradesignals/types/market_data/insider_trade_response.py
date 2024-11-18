# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .insider_trade import InsiderTrade

__all__ = ["InsiderTradeResponse"]


class InsiderTradeResponse(BaseModel):
    data: Optional[List[InsiderTrade]] = None
