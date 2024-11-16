# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SectorListResponse", "Sector"]


class Sector(BaseModel):
    performance: Optional[float] = None

    sector_name: Optional[str] = None


class SectorListResponse(BaseModel):
    sectors: Optional[List[Sector]] = None
