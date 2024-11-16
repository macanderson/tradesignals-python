# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GreekFlowListResponse", "Data"]


class Data(BaseModel):
    delta: Optional[float] = None

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)

    gamma: Optional[float] = None

    option_type: Optional[Literal["CALL", "PUT"]] = FieldInfo(alias="optionType", default=None)

    premium: Optional[float] = None

    rho: Optional[float] = None

    strike_price: Optional[float] = FieldInfo(alias="strikePrice", default=None)

    symbol: Optional[str] = None

    theta: Optional[float] = None

    timestamp: Optional[datetime] = None

    vega: Optional[float] = None


class GreekFlowListResponse(BaseModel):
    data: Optional[List[Data]] = None
