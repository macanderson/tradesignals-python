# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MoverListResponse", "Gainer", "Loser"]


class Gainer(BaseModel):
    change: Optional[float] = None

    company_name: Optional[str] = None

    percent_change: Optional[float] = None

    price: Optional[float] = None

    symbol: Optional[str] = None


class Loser(BaseModel):
    change: Optional[float] = None

    company_name: Optional[str] = None

    percent_change: Optional[float] = None

    price: Optional[float] = None

    symbol: Optional[str] = None


class MoverListResponse(BaseModel):
    gainers: Optional[List[Gainer]] = None

    losers: Optional[List[Loser]] = None
