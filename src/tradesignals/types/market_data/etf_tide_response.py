# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .etf_tide import EtfTide
from ..._models import BaseModel

__all__ = ["EtfTideResponse"]


class EtfTideResponse(BaseModel):
    data: Optional[List[EtfTide]] = None
