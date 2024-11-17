# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .oi_change_entry import OiChangeEntry

__all__ = ["OiChangeResponse"]


class OiChangeResponse(BaseModel):
    data: Optional[List[OiChangeEntry]] = None
