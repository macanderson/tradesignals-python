# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["SectorExposure"]


class SectorExposure(BaseModel):
    positions: Optional[int] = None
    """Number of positions in the sector."""

    positions_closed: Optional[int] = None
    """Number of closed positions in the sector."""

    positions_decreased: Optional[int] = None
    """Number of decreased positions in the sector."""

    positions_increased: Optional[int] = None
    """Number of increased positions in the sector."""

    report_date: Optional[date] = None
    """Report date for the exposure."""

    sector: Optional[str] = None
    """Name of the sector."""

    value: Optional[int] = None
    """Rounded total value of the sector on the reporting date."""
