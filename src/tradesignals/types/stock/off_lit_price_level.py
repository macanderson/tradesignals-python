# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["OffLitPriceLevel"]


class OffLitPriceLevel(BaseModel):
    lit_vol: Optional[int] = None
    """
    The lit volume (this only represents stock trades executed on exchanges operated
    by Nasdaq).
    """

    off_vol: Optional[int] = None
    """The off-lit stock volume (this only represents the FINRA operated exchanges)."""

    price: Optional[str] = None
    """The price level."""
