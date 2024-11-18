# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Optional

from ..._models import BaseModel

__all__ = ["NetPremTick"]


class NetPremTick(BaseModel):
    date: Optional[datetime.date] = None

    net_call_premium: Optional[str] = None

    net_call_volume: Optional[int] = None

    net_put_premium: Optional[str] = None

    net_put_volume: Optional[int] = None

    tape_time: Optional[datetime.datetime] = None
