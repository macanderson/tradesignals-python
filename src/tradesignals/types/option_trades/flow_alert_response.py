# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .flow_alert_entry import FlowAlertEntry

__all__ = ["FlowAlertResponse"]


class FlowAlertResponse(BaseModel):
    data: Optional[List[FlowAlertEntry]] = None
