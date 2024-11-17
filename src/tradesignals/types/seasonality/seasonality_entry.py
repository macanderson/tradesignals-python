# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SeasonalityEntry"]


class SeasonalityEntry(BaseModel):
    avg_change: Optional[float] = None

    max_change: Optional[float] = None

    median_change: Optional[float] = None

    min_change: Optional[float] = None

    month: Optional[int] = None

    positive_closes: Optional[int] = None

    positive_months_perc: Optional[float] = None

    ticker: Optional[str] = None

    years: Optional[float] = None
