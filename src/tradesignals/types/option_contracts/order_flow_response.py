# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .order_flow import OrderFlow

__all__ = ["OrderFlowResponse"]


class OrderFlowResponse(BaseModel):
    data: Optional[List[OrderFlow]] = None
