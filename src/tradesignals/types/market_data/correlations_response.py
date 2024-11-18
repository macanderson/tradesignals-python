# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .correlation import Correlation

__all__ = ["CorrelationsResponse"]


class CorrelationsResponse(BaseModel):
    data: Optional[List[Correlation]] = None
