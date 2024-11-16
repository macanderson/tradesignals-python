# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScreenerRetrieveParams"]


class ScreenerRetrieveParams(TypedDict, total=False):
    industry: str

    market_cap_max: Annotated[float, PropertyInfo(alias="marketCapMax")]

    market_cap_min: Annotated[float, PropertyInfo(alias="marketCapMin")]

    price_max: Annotated[float, PropertyInfo(alias="priceMax")]

    price_min: Annotated[float, PropertyInfo(alias="priceMin")]

    sector: str

    volume_max: Annotated[float, PropertyInfo(alias="volumeMax")]

    volume_min: Annotated[float, PropertyInfo(alias="volumeMin")]
