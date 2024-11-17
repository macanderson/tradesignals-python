# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .expiry_breakdown_entry import ExpiryBreakdownEntry

__all__ = ["ExpiryBreakdownResponse"]


class ExpiryBreakdownResponse(BaseModel):
    data: Optional[List[ExpiryBreakdownEntry]] = None
