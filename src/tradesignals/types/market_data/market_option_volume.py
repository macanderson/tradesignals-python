# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .market_option_volume_response import MarketOptionVolumeResponse

__all__ = ["MarketOptionVolume"]


class MarketOptionVolume(BaseModel):
    data: Optional[List[MarketOptionVolumeResponse]] = None
