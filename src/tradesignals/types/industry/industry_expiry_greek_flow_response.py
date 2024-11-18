# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .industry_expiry_greek_flow import IndustryExpiryGreekFlow

__all__ = ["IndustryExpiryGreekFlowResponse"]


class IndustryExpiryGreekFlowResponse(BaseModel):
    data: Optional[List[IndustryExpiryGreekFlow]] = None
