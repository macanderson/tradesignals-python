# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FinancialRetrieveResponse", "Data"]


class Data(BaseModel):
    fiscal_date: Optional[date] = None

    gross_profit: Optional[float] = None

    net_income: Optional[float] = None

    operating_income: Optional[float] = None

    total_revenue: Optional[float] = None


class FinancialRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None

    period: Optional[Literal["annual", "quarterly"]] = None

    statement_type: Optional[Literal["income", "balance", "cashflow"]] = None

    symbol: Optional[str] = None
