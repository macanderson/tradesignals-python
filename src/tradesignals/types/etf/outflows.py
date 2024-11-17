# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ..._models import BaseModel

__all__ = ["Outflows"]


class Outflows(BaseModel):
    change: Optional[int] = None
    """The net in/outflow measured as volume."""

    change_prem: Optional[str] = None
    """The net in/outflow measured as premium."""

    close: Optional[str] = None
    """The latest stock price of the ticker."""

    date: Optional[datetime.date] = None
    """An ISO date."""

    is_fomc: Optional[bool] = None
    """If the date has an FOMC announcement."""

    volume: Optional[int] = None
    """The volume of the ticker for the trading day."""
