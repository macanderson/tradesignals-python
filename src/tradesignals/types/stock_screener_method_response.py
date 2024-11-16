# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["StockScreenerMethodResponse", "Result"]


class Result(BaseModel):
    company_name: Optional[str] = None

    industry: Optional[str] = None

    market_cap: Optional[float] = None

    price: Optional[float] = None

    sector: Optional[str] = None

    symbol: Optional[str] = None

    volume: Optional[int] = None


class StockScreenerMethodResponse(BaseModel):
    results: Optional[List[Result]] = None
