# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TideRetrieveResponse", "Etf"]


class Etf(BaseModel):
    etf_symbol: Optional[str] = FieldInfo(alias="etfSymbol", default=None)

    inflow: Optional[float] = None

    net_flow: Optional[float] = FieldInfo(alias="netFlow", default=None)

    outflow: Optional[float] = None


class TideRetrieveResponse(BaseModel):
    date: Optional[datetime.date] = None

    etfs: Optional[List[Etf]] = None

    inflows: Optional[float] = None

    net_flow: Optional[float] = FieldInfo(alias="netFlow", default=None)

    outflows: Optional[float] = None
