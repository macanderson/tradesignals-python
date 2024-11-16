# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .etf_holding import EtfHolding

__all__ = ["EtfHoldingsResponse"]


class EtfHoldingsResponse(BaseModel):
    data: Optional[List[EtfHolding]] = None
