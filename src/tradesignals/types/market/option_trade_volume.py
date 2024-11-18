# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .option_trade_volume_response import OptionTradeVolumeResponse

__all__ = ["OptionTradeVolume"]


class OptionTradeVolume(BaseModel):
    data: Optional[List[OptionTradeVolumeResponse]] = None
