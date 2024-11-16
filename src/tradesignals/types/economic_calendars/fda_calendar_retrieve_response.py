# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FdaCalendarRetrieveResponse", "Event"]


class Event(BaseModel):
    date: Optional[datetime.date] = None

    drug_name: Optional[str] = FieldInfo(alias="drugName", default=None)

    event: Optional[str] = None

    status: Optional[str] = None

    symbol: Optional[str] = None


class FdaCalendarRetrieveResponse(BaseModel):
    events: Optional[List[Event]] = None
