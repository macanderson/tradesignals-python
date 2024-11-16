# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel

__all__ = ["InstitutionalActivityListResponse", "Data"]


class Data(BaseModel):
    change: Optional[float] = None

    date: Optional[datetime.date] = None

    institution: Optional[str] = None

    shares: Optional[int] = None

    symbol: Optional[str] = None

    value: Optional[float] = None


class InstitutionalActivityListResponse(BaseModel):
    data: Optional[List[Data]] = None
