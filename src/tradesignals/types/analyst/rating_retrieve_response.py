# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel

__all__ = ["RatingRetrieveResponse", "Rating"]


class Rating(BaseModel):
    analyst: Optional[str] = None

    date: Optional[datetime.date] = None

    price_target: Optional[float] = None

    rating: Optional[str] = None


class RatingRetrieveResponse(BaseModel):
    ratings: Optional[List[Rating]] = None

    symbol: Optional[str] = None
