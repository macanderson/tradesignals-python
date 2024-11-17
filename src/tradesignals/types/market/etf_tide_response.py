# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .etf_tide_entry import EtfTideEntry

__all__ = ["EtfTideResponse"]


class EtfTideResponse(BaseModel):
    data: Optional[List[EtfTideEntry]] = None
