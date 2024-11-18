# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MonthPerformerEntry"]


class MonthPerformerEntry(BaseModel):
    avg_change: Optional[float] = None

    marketcap: Optional[str] = None

    max_change: Optional[float] = None

    median_change: Optional[float] = None

    min_change: Optional[float] = None

    month: Optional[int] = None

    positive_closes: Optional[int] = None

    positive_months_perc: Optional[float] = None

    sector: Optional[
        Literal[
            "Basic Materials",
            "Communication Services",
            "Consumer Cyclical",
            "Consumer Defensive",
            "Energy",
            "Financial Services",
            "Healthcare",
            "Industrials",
            "Real Estate",
            "Technology",
            "Utilities",
        ]
    ] = None

    ticker: Optional[str] = None

    years: Optional[float] = None
