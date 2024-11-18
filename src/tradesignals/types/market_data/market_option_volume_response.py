# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ..._models import BaseModel

__all__ = ["MarketOptionVolumeResponse"]


class MarketOptionVolumeResponse(BaseModel):
    call_premium: Optional[str] = None
    """Total call premium."""

    call_volume: Optional[int] = None
    """Total call transactions volume."""

    date: Optional[datetime.date] = None
    """The trading date."""

    put_premium: Optional[str] = None
    """Total put premium."""

    put_volume: Optional[int] = None
    """Total put transactions volume."""
