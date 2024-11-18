# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OhlcEntry"]


class OhlcEntry(BaseModel):
    close: Optional[str] = None
    """The closing price of the candle."""

    end_time: Optional[datetime] = None
    """The end time of the candle as a UTC timestamp."""

    high: Optional[str] = None
    """The highest price of the candle."""

    low: Optional[str] = None
    """The lowest price of the candle."""

    market_time: Optional[Literal["r", "po", "pr"]] = None
    """The market time.

    PR = premarket, r = regular trading hours, po = postmarket. - pr - r - po
    """

    open: Optional[str] = None
    """The opening price of the candle."""

    start_time: Optional[datetime] = None
    """The start time of the candle as a UTC timestamp."""

    total_volume: Optional[int] = None
    """The total volume of the ticker for the full trading day till now."""

    volume: Optional[int] = None
    """The volume of the candle."""
