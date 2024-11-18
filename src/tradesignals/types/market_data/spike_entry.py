# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SpikeEntry"]


class SpikeEntry(BaseModel):
    time: Optional[datetime] = None
    """The timestamp for the SPIKE value."""

    value: Optional[str] = None
    """The SPIKE value."""
