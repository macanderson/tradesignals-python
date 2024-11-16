# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UpgradesDowngradeListResponse", "UpgradesDowngrade"]


class UpgradesDowngrade(BaseModel):
    action: Optional[str] = None

    analyst: Optional[str] = None

    date: Optional[datetime.date] = None

    from_rating: Optional[str] = None

    symbol: Optional[str] = None

    to_rating: Optional[str] = None


class UpgradesDowngradeListResponse(BaseModel):
    upgrades_downgrades: Optional[List[UpgradesDowngrade]] = None
