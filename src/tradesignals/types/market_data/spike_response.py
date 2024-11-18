# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .spike_entry import SpikeEntry

__all__ = ["SpikeResponse"]


class SpikeResponse(BaseModel):
    data: Optional[List[SpikeEntry]] = None
