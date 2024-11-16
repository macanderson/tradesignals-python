# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .etf_in_outflow import EtfInOutflow

__all__ = ["EtfInOutflowResponse"]


class EtfInOutflowResponse(BaseModel):
    data: Optional[List[EtfInOutflow]] = None
