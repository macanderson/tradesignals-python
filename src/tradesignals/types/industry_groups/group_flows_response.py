# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .group_greek_flow import GroupGreekFlow

__all__ = ["GroupFlowsResponse"]


class GroupFlowsResponse(BaseModel):
    data: Optional[List[GroupGreekFlow]] = None
