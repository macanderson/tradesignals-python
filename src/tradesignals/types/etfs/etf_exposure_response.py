# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .etf_exposure_data import EtfExposureData

__all__ = ["EtfExposureResponse"]


class EtfExposureResponse(BaseModel):
    data: Optional[List[EtfExposureData]] = None
