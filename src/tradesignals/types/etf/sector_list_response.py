# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SectorListResponse"]


class SectorListResponse(BaseModel):
    sectors: Optional[List[str]] = None
