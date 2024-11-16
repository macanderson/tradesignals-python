# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .darkpool_trade import DarkpoolTrade

__all__ = ["DarkpoolTradesResponse"]


class DarkpoolTradesResponse(BaseModel):
    data: Optional[List[DarkpoolTrade]] = None
