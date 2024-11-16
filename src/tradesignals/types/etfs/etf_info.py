# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .etf_info_response import EtfInfoResponse

__all__ = ["EtfInfo"]


class EtfInfo(BaseModel):
    data: Optional[List[EtfInfoResponse]] = None
