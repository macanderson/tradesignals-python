# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EtfListResponse"]


class EtfListResponse(BaseModel):
    data: Optional[List[str]] = None
