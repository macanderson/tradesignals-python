# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SpikeDetectionRetrieveResponse", "Spike"]


class Spike(BaseModel):
    price_spike: Optional[float] = FieldInfo(alias="priceSpike", default=None)

    symbol: Optional[str] = None

    timestamp: Optional[datetime] = None

    volume_spike: Optional[float] = FieldInfo(alias="volumeSpike", default=None)


class SpikeDetectionRetrieveResponse(BaseModel):
    spikes: Optional[List[Spike]] = None
