# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MaxPainEntry"]


class MaxPainEntry(BaseModel):
    date: Optional[datetime.date] = None

    values: Optional[List[List[str]]] = None
