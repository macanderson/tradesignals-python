# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Weights", "Country", "Sector"]


class Country(BaseModel):
    country: Optional[str] = None
    """The country."""

    weight: Optional[str] = None
    """The country exposure in percentage."""


class Sector(BaseModel):
    sector: Optional[str] = None
    """The sector."""

    weight: Optional[str] = None
    """The sector exposure in percentage."""


class Weights(BaseModel):
    country: Optional[List[Country]] = None
    """A list of countries with their exposure by percentage."""

    sector: Optional[List[Sector]] = None
    """A list of sectors with their exposure by percentage."""
