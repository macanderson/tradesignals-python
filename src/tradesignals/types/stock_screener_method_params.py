# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StockScreenerMethodParams"]


class StockScreenerMethodParams(TypedDict, total=False):
    industry: str
    """Industry to filter stocks."""

    market_cap_max: Annotated[float, PropertyInfo(alias="marketCapMax")]
    """Maximum market capitalization."""

    market_cap_min: Annotated[float, PropertyInfo(alias="marketCapMin")]
    """Minimum market capitalization."""

    price_max: Annotated[float, PropertyInfo(alias="priceMax")]
    """Maximum stock price."""

    price_min: Annotated[float, PropertyInfo(alias="priceMin")]
    """Minimum stock price."""

    sector: str
    """Sector to filter stocks."""

    volume_max: Annotated[float, PropertyInfo(alias="volumeMax")]
    """Maximum trading volume."""

    volume_min: Annotated[float, PropertyInfo(alias="volumeMin")]
    """Minimum trading volume."""
