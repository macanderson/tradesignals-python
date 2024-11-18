# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .fda_calendar_event import FdaCalendarEvent

__all__ = ["FdaCalendarResponse"]


class FdaCalendarResponse(BaseModel):
    data: Optional[List[FdaCalendarEvent]] = None
