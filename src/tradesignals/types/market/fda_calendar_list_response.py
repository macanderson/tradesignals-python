# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .fda_calendar_event import FdaCalendarEvent

__all__ = ["FdaCalendarListResponse"]

FdaCalendarListResponse: TypeAlias = List[FdaCalendarEvent]
