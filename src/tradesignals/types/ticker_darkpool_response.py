# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .ticker_darkpool_trade import TickerDarkpoolTrade

__all__ = ["TickerDarkpoolResponse"]


class TickerDarkpoolResponse(BaseModel):
    data: Optional[List[TickerDarkpoolTrade]] = None
