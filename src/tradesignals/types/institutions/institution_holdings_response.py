# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .institution_holding import InstitutionHolding

__all__ = ["InstitutionHoldingsResponse"]


class InstitutionHoldingsResponse(BaseModel):
    data: Optional[List[InstitutionHolding]] = None
