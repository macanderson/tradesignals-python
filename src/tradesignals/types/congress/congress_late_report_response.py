# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .congress_late_report import CongressLateReport

__all__ = ["CongressLateReportResponse"]


class CongressLateReportResponse(BaseModel):
    data: Optional[List[CongressLateReport]] = None
