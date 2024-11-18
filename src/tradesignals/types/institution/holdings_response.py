# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .holdings import Holdings
from ..._models import BaseModel

__all__ = ["HoldingsResponse"]


class HoldingsResponse(BaseModel):
    data: Optional[List[Holdings]] = None
