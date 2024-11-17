# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["FdaCalendarEvent"]


class FdaCalendarEvent(BaseModel):
    catalyst: Optional[str] = None
    """The kind of upcoming date causing the event."""

    description: Optional[str] = None
    """The description of the event."""

    drug: Optional[str] = None
    """The name of the drug."""

    end_date: Optional[date] = None
    """The event end date in ISO date format."""

    indication: Optional[str] = None
    """The sickness or symptom the drug is used to treat."""

    start_date: Optional[date] = None
    """The event start date in ISO date format."""

    status: Optional[str] = None
    """The status of the drug admission."""

    ticker: Optional[str] = None
    """The ticker of the company applying for drug admission."""
