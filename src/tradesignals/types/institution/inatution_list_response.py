# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .institution import Institution

__all__ = ["InatutionListResponse"]


class InatutionListResponse(BaseModel):
    data: Optional[List[Institution]] = None
