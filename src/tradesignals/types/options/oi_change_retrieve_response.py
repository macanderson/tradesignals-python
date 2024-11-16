# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OiChangeRetrieveResponse", "Data"]


class Data(BaseModel):
    date: Optional[datetime.date] = None

    expiration_date: Optional[datetime.date] = FieldInfo(alias="expirationDate", default=None)

    oi_change: Optional[int] = FieldInfo(alias="oiChange", default=None)

    option_type: Optional[Literal["CALL", "PUT"]] = FieldInfo(alias="optionType", default=None)

    strike_price: Optional[float] = FieldInfo(alias="strikePrice", default=None)


class OiChangeRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None

    symbol: Optional[str] = None
