# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .congress_recent_report import CongressRecentReport

__all__ = ["CongressRecentReportsResponse"]


class CongressRecentReportsResponse(BaseModel):
    data: Optional[List[CongressRecentReport]] = None
