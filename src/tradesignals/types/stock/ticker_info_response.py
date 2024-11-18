# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TickerInfoResponse"]


class TickerInfoResponse(BaseModel):
    announce_time: Optional[Literal["unkown", "afterhours", "premarket"]] = None

    avg30_volume: Optional[str] = None

    full_name: Optional[str] = None

    has_dividend: Optional[bool] = None

    has_earnings_history: Optional[bool] = None

    has_investment_arm: Optional[bool] = None

    has_options: Optional[bool] = None

    issue_type: Optional[Literal["Common Stock", "ETF", "Index", "ADR"]] = None

    marketcap: Optional[str] = None

    next_earnings_date: Optional[date] = None

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

    short_description: Optional[str] = None
