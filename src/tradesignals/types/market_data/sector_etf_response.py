# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .sector_etf_data import SectorEtfData

__all__ = ["SectorEtfResponse"]


class SectorEtfResponse(BaseModel):
    data: Optional[List[SectorEtfData]] = None
