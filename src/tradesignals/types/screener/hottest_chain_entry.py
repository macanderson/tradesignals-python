# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HottestChainEntry"]


class HottestChainEntry(BaseModel):
    ask_side_volume: Optional[int] = None

    avg_price: Optional[str] = None

    bid_side_volume: Optional[int] = None

    chain_prev_close: Optional[str] = None

    close: Optional[str] = None

    cross_volume: Optional[int] = None

    floor_volume: Optional[int] = None

    high: Optional[str] = None

    low: Optional[str] = None

    option_symbol: Optional[str] = None

    premium: Optional[str] = None

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

    stock_price: Optional[str] = None

    trades: Optional[int] = None

    volume: Optional[int] = None
