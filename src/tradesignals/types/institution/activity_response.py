# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .activity import Activity
from ..._models import BaseModel

__all__ = ["ActivityResponse"]


class ActivityResponse(BaseModel):
    data: Optional[List[Activity]] = None
