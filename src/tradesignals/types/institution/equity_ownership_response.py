# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .equity_ownership import EquityOwnership

__all__ = ["EquityOwnershipResponse"]


class EquityOwnershipResponse(BaseModel):
    data: Optional[List[EquityOwnership]] = None
