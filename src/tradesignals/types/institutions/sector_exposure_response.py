# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .sector_exposure import SectorExposure

__all__ = ["SectorExposureResponse"]


class SectorExposureResponse(BaseModel):
    data: Optional[List[SectorExposure]] = None
