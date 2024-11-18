# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AnalystRatingEntry"]


class AnalystRatingEntry(BaseModel):
    action: Optional[
        Literal["initiated", "reiterated", "downgraded", "upgraded", "maintained", "target raised", "target lowered"]
    ] = None

    analyst_name: Optional[str] = None

    firm: Optional[str] = None

    recommendation: Optional[Literal["buy", "hold", "sell"]] = None

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

    target: Optional[str] = None

    ticker: Optional[str] = None

    timestamp: Optional[datetime] = None
