# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ..._models import BaseModel

__all__ = ["InsiderTrade"]


class InsiderTrade(BaseModel):
    call_premium: Optional[str] = None
    """The sum of the premium of all the call transactions that executed."""

    call_volume: Optional[int] = None
    """The sum of the size of all the call transactions that executed."""

    date: Optional[datetime.date] = None
    """The trading date in ISO format."""

    put_premium: Optional[str] = None
    """The sum of the premium of all the put transactions that executed."""

    put_volume: Optional[int] = None
    """The sum of the size of all the put transactions that executed."""
