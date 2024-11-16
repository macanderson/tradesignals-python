# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EtfHolding"]


class EtfHolding(BaseModel):
    avg30_volume: Optional[str] = None
    """The average stock volume for the stock over the last 30 days."""

    bearish_premium: Optional[str] = None
    """
    The bearish premium is defined as (call premium bid side) + (put premium ask
    side).
    """

    bullish_premium: Optional[str] = None
    """
    The bullish premium is defined as (call premium ask side) + (put premium bid
    side).
    """

    call_premium: Optional[str] = None
    """The sum of the premium of all the call transactions that executed."""

    call_volume: Optional[int] = None
    """The sum of the size of all the call transactions that executed."""

    close: Optional[str] = None
    """The closing price of the candle."""

    has_options: Optional[bool] = None
    """Boolean flag indicating whether the company has options."""

    high: Optional[str] = None
    """The highest price of the candle."""

    low: Optional[str] = None
    """The lowest price of the candle."""

    name: Optional[str] = None
    """The name of the company."""

    open: Optional[str] = None
    """The opening price of the candle."""

    prev_price: Optional[str] = None
    """The previous trading day's stock price of the ticker."""

    put_premium: Optional[str] = None
    """The sum of the premium of all the put transactions that executed."""

    put_volume: Optional[int] = None
    """The sum of the size of all the put transactions that executed."""

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
    """The financial sector of the ticker.

    Empty if unknown or not applicable such as ETF/Index.
    """

    ticker: Optional[str] = None
    """The stock ticker."""

    volume: Optional[int] = None
    """The volume of the ticker for the trading day."""

    week_52_high: Optional[str] = None
    """The 52-week high stock price of the ticker."""

    week_52_low: Optional[str] = None
    """The 52-week low stock price of the ticker."""
