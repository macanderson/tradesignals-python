# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .congress_trader_transaction import CongressTraderTransaction

__all__ = ["CongressTraderResponse"]


class CongressTraderResponse(BaseModel):
    data: Optional[List[CongressTraderTransaction]] = None
