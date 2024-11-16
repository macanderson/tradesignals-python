# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EconomicCalendarListResponse", "Event"]


class Event(BaseModel):
    actual: Optional[str] = None

    country: Optional[str] = None

    date_time: Optional[datetime] = FieldInfo(alias="dateTime", default=None)

    event: Optional[str] = None

    forecast: Optional[str] = None

    previous: Optional[str] = None


class EconomicCalendarListResponse(BaseModel):
    events: Optional[List[Event]] = None
