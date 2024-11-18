# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .economic_calendar_event import EconomicCalendarEvent

__all__ = ["EconomicCalendarResponse"]


class EconomicCalendarResponse(BaseModel):
    data: Optional[List[EconomicCalendarEvent]] = None
