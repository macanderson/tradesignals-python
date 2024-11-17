# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .sector_etf_entry import SectorEtfEntry

__all__ = ["SectorEtfsResponse"]


class SectorEtfsResponse(BaseModel):
    data: Optional[List[SectorEtfEntry]] = None
