# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TotalVolumeListResponse", "Symbol"]


class Symbol(BaseModel):
    symbol: Optional[str] = None

    volume: Optional[int] = None


class TotalVolumeListResponse(BaseModel):
    date: Optional[datetime.date] = None

    symbols: Optional[List[Symbol]] = None

    total_volume: Optional[int] = FieldInfo(alias="totalVolume", default=None)
