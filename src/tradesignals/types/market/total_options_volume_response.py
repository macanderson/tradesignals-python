# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .total_options_volume_entry import TotalOptionsVolumeEntry

__all__ = ["TotalOptionsVolumeResponse"]


class TotalOptionsVolumeResponse(BaseModel):
    data: Optional[List[TotalOptionsVolumeEntry]] = None
