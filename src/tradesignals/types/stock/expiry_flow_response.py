# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel
from .expiry_flow import ExpiryFlow

__all__ = ["ExpiryFlowResponse"]


class ExpiryFlowResponse(BaseModel):
    data: Optional[List[ExpiryFlow]] = None

    date: Optional[datetime.date] = None
