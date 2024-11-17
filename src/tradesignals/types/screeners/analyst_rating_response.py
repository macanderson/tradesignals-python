# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .analyst_rating_entry import AnalystRatingEntry

__all__ = ["AnalystRatingResponse"]


class AnalystRatingResponse(BaseModel):
    data: Optional[List[AnalystRatingEntry]] = None
