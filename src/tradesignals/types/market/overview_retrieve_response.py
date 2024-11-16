# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["OverviewRetrieveResponse", "MajorIndex"]


class MajorIndex(BaseModel):
    change: Optional[float] = None

    name: Optional[str] = None

    percent_change: Optional[float] = None

    price: Optional[float] = None

    symbol: Optional[str] = None


class OverviewRetrieveResponse(BaseModel):
    major_indices: Optional[List[MajorIndex]] = None

    market_status: Optional[str] = None
