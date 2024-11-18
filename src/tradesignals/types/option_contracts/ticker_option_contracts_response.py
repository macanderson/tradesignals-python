# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .ticker_option_contract import TickerOptionContract

__all__ = ["TickerOptionContractsResponse"]


class TickerOptionContractsResponse(BaseModel):
    data: Optional[List[TickerOptionContract]] = None
