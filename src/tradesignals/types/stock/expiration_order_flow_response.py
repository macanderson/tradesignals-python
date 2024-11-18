# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel
from .expiration_order_flow import ExpirationOrderFlow

__all__ = ["ExpirationOrderFlowResponse"]


class ExpirationOrderFlowResponse(BaseModel):
    data: Optional[List[ExpirationOrderFlow]] = None

    date: Optional[datetime.date] = None
