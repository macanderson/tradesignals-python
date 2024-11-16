# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ExpiryListResponse"]


class ExpiryListResponse(BaseModel):
    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)

    symbol: Optional[str] = None

    total_delta: Optional[float] = FieldInfo(alias="totalDelta", default=None)

    total_gamma: Optional[float] = FieldInfo(alias="totalGamma", default=None)

    total_premium: Optional[float] = FieldInfo(alias="totalPremium", default=None)

    total_rho: Optional[float] = FieldInfo(alias="totalRho", default=None)

    total_theta: Optional[float] = FieldInfo(alias="totalTheta", default=None)

    total_vega: Optional[float] = FieldInfo(alias="totalVega", default=None)
