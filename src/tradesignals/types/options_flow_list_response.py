# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OptionsFlowListResponse", "Data"]


class Data(BaseModel):
    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)

    open_interest: Optional[int] = FieldInfo(alias="openInterest", default=None)

    option_type: Optional[Literal["CALL", "PUT"]] = FieldInfo(alias="optionType", default=None)

    premium: Optional[float] = None

    strike_price: Optional[float] = FieldInfo(alias="strikePrice", default=None)

    symbol: Optional[str] = None

    timestamp: Optional[datetime] = None

    volume: Optional[int] = None


class OptionsFlowListResponse(BaseModel):
    data: Optional[List[Data]] = None
