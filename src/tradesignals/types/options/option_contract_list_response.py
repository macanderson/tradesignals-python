# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OptionContractListResponse", "Contract"]


class Contract(BaseModel):
    expiration_date: Optional[date] = None

    option_symbol: Optional[str] = None

    option_type: Optional[Literal["CALL", "PUT"]] = None

    strike_price: Optional[float] = None


class OptionContractListResponse(BaseModel):
    contracts: Optional[List[Contract]] = None
