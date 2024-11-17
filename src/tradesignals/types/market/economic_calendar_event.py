# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EconomicCalendarEvent"]


class EconomicCalendarEvent(BaseModel):
    event: Optional[str] = None
    """The event or reason, such as a fed speaker or economic report/indicator."""

    forecast: Optional[str] = None
    """The forecast if the event is an economic report/indicator."""

    prev: Optional[str] = None
    """
    The previous value of the preceding period if the event is an economic
    report/indicator.
    """

    reported_period: Optional[str] = None
    """The period being reported for the economic report/indicator."""

    time: Optional[datetime] = None
    """The time at which the event will start as a UTC timestamp."""

    type: Optional[Literal["fed-speaker", "fomc", "report"]] = None
    """The type of the event."""
