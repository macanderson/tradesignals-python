# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SectorRetrieveResponse", "Etf"]


class Etf(BaseModel):
    dividend_yield: Optional[float] = FieldInfo(alias="dividendYield", default=None)

    etf_name: Optional[str] = FieldInfo(alias="etfName", default=None)

    etf_symbol: Optional[str] = FieldInfo(alias="etfSymbol", default=None)

    expense_ratio: Optional[float] = FieldInfo(alias="expenseRatio", default=None)

    inception_date: Optional[date] = FieldInfo(alias="inceptionDate", default=None)

    net_assets: Optional[float] = FieldInfo(alias="netAssets", default=None)


class SectorRetrieveResponse(BaseModel):
    etfs: Optional[List[Etf]] = None

    sector: Optional[str] = None
