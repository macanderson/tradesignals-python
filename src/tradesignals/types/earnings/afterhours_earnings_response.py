# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .afterhours_earnings_data import AfterhoursEarningsData

__all__ = ["AfterhoursEarningsResponse"]


class AfterhoursEarningsResponse(BaseModel):
    data: Optional[List[AfterhoursEarningsData]] = None
