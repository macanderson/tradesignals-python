# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["OptionExpirationData"]


class OptionExpirationData(BaseModel):
    chains: Optional[int] = None
    """The total amount of chains for that expiry."""

    expiry: Optional[date] = None
    """The contract expiry date in ISO format."""

    open_interest: Optional[int] = None
    """The total open interest for that expiry."""

    volume: Optional[int] = None
    """The total volume for that expiry."""
