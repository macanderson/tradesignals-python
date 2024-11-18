# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["PremarketEarningsData"]


class PremarketEarningsData(BaseModel):
    close: Optional[str] = None
    """The stock's closing price."""

    close_date: Optional[date] = None
    """The date of the stock's closing price."""

    continent: Optional[str] = None
    """The continent where the company operates."""

    country_code: Optional[str] = None
    """The country's ISO code."""

    country_name: Optional[str] = None
    """The country's full name."""

    ending_fiscal_quarter: Optional[date] = None
    """The ending date of the fiscal quarter."""

    eps_mean_est: Optional[str] = None
    """The mean estimated earnings per share (EPS)."""

    full_name: Optional[str] = None
    """The full name of the company."""

    has_options: Optional[bool] = None
    """Indicates whether options are available for the stock."""

    implied_move: Optional[str] = None
    """The implied move in the stock's price based on market data."""

    is_s_p_500: Optional[bool] = None
    """Indicates if the company is part of the S&P 500 index."""

    marketcap: Optional[str] = None
    """The market capitalization of the company."""

    prev: Optional[str] = None
    """The previous trading day's closing price."""

    prev_date: Optional[date] = None
    """The date of the previous trading day."""

    report_date: Optional[date] = None
    """The report date for earnings."""

    report_time: Optional[str] = None
    """The time of the earnings report (e.g., premarket, postmarket)."""

    sector: Optional[str] = None
    """The company's sector."""

    source: Optional[str] = None
    """The source of the earnings information."""

    street_mean_est: Optional[str] = None
    """The mean estimated earnings per share (EPS) from analysts."""

    symbol: Optional[str] = None
    """The stock ticker symbol."""
