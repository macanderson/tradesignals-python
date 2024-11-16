# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["DividendRetrieveResponse", "Dividend"]


class Dividend(BaseModel):
    declared_date: Optional[date] = None

    dividend_amount: Optional[float] = None

    ex_dividend_date: Optional[date] = None

    payment_date: Optional[date] = None

    record_date: Optional[date] = None


class DividendRetrieveResponse(BaseModel):
    dividends: Optional[List[Dividend]] = None

    symbol: Optional[str] = None
