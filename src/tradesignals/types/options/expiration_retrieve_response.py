# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["ExpirationRetrieveResponse"]


class ExpirationRetrieveResponse(BaseModel):
    expirations: Optional[List[date]] = None

    symbol: Optional[str] = None
